# TODO fuzzy string search
# TODO a way to set any element of a media from UI
from backendv2 import load, MediaClass
import os
from fuzzywuzzy import fuzz
import media_pb2
from datetime import datetime

def clear():
    return
    os.system('cls' if os.name == 'nt' else 'clear')

INPUT_CHARACTER = "> "

from enum import Enum
class MenuFlow(Enum):
    BACK = 1
    QUIT = 2

def choose_options(option_descriptions, options):
    if len(option_descriptions) != len(options):
        raise Exception("Descriptions size does not much options size")
    if len(options) > 8:
        raise Exception("Too many options provided")
    
    # Adding padding here to that I can index MenuFlow.Back and MenuFlow.QUIT from options later
    options = options.copy()
    options.extend(([None]*(8-len(options)))+[MenuFlow.BACK, MenuFlow.QUIT])
    def show_options():
        for i, text in enumerate(option_descriptions):
            print(f"[{i}]: {text}")
        print("[8]: Back")
        print("[9]: Quit")
    
    show_options()
    while True:
        option_index = input(INPUT_CHARACTER)
        print()

        if not option_index.isdigit():
            clear()
            show_options()
            continue
        option_index = int(option_index)
        break
    return option_index, options[option_index]

##################
### Viewing options
def view_media():
    while True:
        chosen_option = choose_options(view_media_text, view_media_funcs)[1]
        if chosen_option == MenuFlow.QUIT:
            os._exit(1)
        elif chosen_option == MenuFlow.BACK:
            return
        else:
            chosen_option()
            print()

def print_by_rating():
    global catalog
    def get_media_rating_or_default_zero(media, default=0):
        if media.HasField("rating"):
            return media.rating.value
        else:
            return default
    for media in sorted(catalog.medias, key=get_media_rating_or_default_zero, reverse=True):
        print(MediaClass(media))
	
def print_by_title():
    global catalog
    for media in sorted(catalog.medias, key=lambda media: media.name):
        print(MediaClass(media))
	
def print_by_date():
    global catalog
    default_date_timestamp = datetime.strptime("01/01/2000", "%d/%m/%Y").timestamp()
    def get_media_date_or_default(media, default=default_date_timestamp):
        if media.HasField("date_finished"):
            return media.date_finished.seconds
        else:
            return default
    for media in sorted(catalog.medias, key=get_media_date_or_default):
        print(MediaClass(media))
##################

def search_media():
    global catalog
    while True:
        print("Enter the name of the media item")
        target_name = input(INPUT_CHARACTER)
        print()

        ratio_dict = {media.name: fuzz.partial_ratio(target_name, media.name) for media in catalog.medias}
        sorted_medias = sorted(catalog.medias, key=lambda media:ratio_dict[media.name], reverse = True)[:5]

        sorted_names_and_similarity = [f"{ratio_dict[media.name]}%: {media.name}" for media in sorted_medias]
        selected_media = choose_options(sorted_names_and_similarity, sorted_medias)[1]
        if selected_media == MenuFlow.QUIT:
            os._exit(1)
        elif selected_media == MenuFlow.BACK:
            return
        print(MediaClass(selected_media))
        return

def edit_media():
    pass

def remove_media():
    pass

### Adding Media
def add_media():
    global catalog
    new_media = media_pb2.Media()

    new_media.name = input("Name: ")
    new_media.type = choose_options(media_pb2.MediaType.keys(), media_pb2.MediaType.values())[1]

    print("Press enter to skip.")
    rating = int(input("Rating (0-10): "))
    if rating:
        new_media.rating.value = rating

    print("Press enter to skip.")
    date_finished = input("Date (dd/mm/yy): ")
    if date_finished:
        new_media.date_finished = datetime.strptime(date_finished, "%d/%m/%Y")
    
    catalog.medias.append(new_media)
    print(f"{new_media.name} has been added to the collection.")

search_media_text = ["Edit media item", "Remove media item"]
search_media_funcs = [edit_media, remove_media]

view_media_text = ["Print all media items by date", "Print all media items by rating", "Print all media items by title"]
view_media_funcs = [print_by_date, print_by_rating, print_by_title]

main_menu_text = ["Search for media item", "Add media item", "View media items"]
main_menu_funcs = [search_media, add_media, view_media]

def IO_manager():
    while True:
        chosen_option = choose_options(main_menu_text, main_menu_funcs)[1]
        if chosen_option == MenuFlow.QUIT:
            os._exit(1)
        elif chosen_option == MenuFlow.BACK:
            continue
        else:
            chosen_option()
            print()

if __name__ == "__main__":
    catalog = load()
    IO_manager()