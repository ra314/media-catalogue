from datetime import datetime
import media_pb2

#Defining the media Class
class media:	
	def __init__(self, name, media_type, rating, date_finished):
		self.name = name
		self.media_type = media_type
		self.rating = rating
		self.date_finished = date_finished
		#Relative ratings is a dictionary
		#The key is the name of the other media item that the object is compared to
		#The value is -1 if the other item is better, 1 if the other item is worse
		#0 if the other item is equal
		self.relative_ratings = {}
		#-1 means no generated rating is avaialable
		self.generated_rating = -1
		
	def print(self):
		date = self.date_finished.strftime('%d/%m/%Y') if self.date_finished else "Unknown"
		rating = self.rating if self.rating else -1
		generated_rating = self.generated_rating if self.generated_rating else -1
		print("{: <5} {: <8.2f} {: <50} {: <15} {: <20}".format(rating, generated_rating, self.name, date, self.media_type))
		
	def __gt__(self, media2):
		if self.rating == None: return False
		if media2.rating == None: return True
		return self.rating > media2.rating
		
	def __eq__(self, media2):
		return self.rating == media2.rating
		
	def generate_rating(self):
		if not len(self.relative_ratings): 
			self.generated_rating = -1
			return
		self.generated_rating = sum([value+1 for value in self.relative_ratings.values()])/(len(self.relative_ratings.values())*2)*10

#Defining the enum for media_type
media_type_enum = ["TV Show", "Film", "Book", "Game"]

###Importing Data
import pickle
def load():
	try: 
		medias = pickle.load(open("medias.bin", "rb"))
		return medias
	except:
		medias = {}
		return medias

def unload(exit_code):
	pickle.dump(medias,open("medias.bin","wb"))
	print("Data Saved")
	if exit_code: exit()
	
###Convert
import copy
def convert():
	for item in medias.values():
		old_item = copy.deepcopy(item)
		medias[item.name] = media(old_item.name, old_item.media_type, old_item.rating, old_item.date_finished)
		medias[item.name].relative_ratings = old_item.relative_ratings
		medias[item.name].generated_rating = old_item.generated_rating
	unload(0)

###Select Media Type
def select_media_type():
	print("TVShow 1, Film 2, Book 3, Game 4")
	media_type = media_type_enum[int(input("Media Type: "))-1]
	return media_type

###Adding Media
def add_media():
	name = input("Name: ")
	media_type = select_media_type()
	medias[name] = media(name, media_type, None, None)
	rating = input("Rating (0-10): ")
	if rating != "": medias[name].rating = int(rating)
	date_finished = input("Date: ")
	if date_finished != "": medias[name].date_finished = datetime.strptime(date_finished, "%d/%m/%Y")
	unload(0)
	
###Removing a media item
def remove_media():
	name = input("Name: ")
	for item in medias.values():
		if name in item.relative_ratings:
			del item.relative_ratings[name]
	del medias[name]
	unload(0)
	
###Renaming a media item
def rename_media():
	curr_name = input("Current Name: ")
	new_name = input("New Name: ")
	for item in medias.values():
		if curr_name in item.relative_ratings:
			item.relative_ratings[new_name] = item.relative_ratings[curr_name]
			del item.relative_ratings[curr_name]
	medias[new_name] = medias[curr_name]
	medias[new_name].name = new_name
	del medias[curr_name]
	unload(0)
	
###Printing all Media and ratings
def print_by_generated_rating():
	media_type = select_media_type()
	items = [item for item in medias.values() if item.media_type == media_type]
	for item in items: item.generate_rating()
	for item in sorted(items, key = lambda item: item.generated_rating, reverse = True): item.print()

def print_by_rating():
	for item in sorted(medias.values(), reverse = True): item.print()
	
def print_by_title():
	for item in sorted(medias.values(), key = lambda item: item.name): item.print()
	
def print_by_date():
	for item in sorted(medias.values(), key = lambda item: item.date_finished if item.date_finished else datetime.strptime("01/01/2000", "%d/%m/%Y")): item.print()
	
###Generating Ratings
import random
import itertools
def generate_ratings():
	choice = int(input("1 to be presented with random pairs, 2 to generate ratings for a certain media item: "))
	print("Left is Better 1, Equal 2, Right is Better 3, To Skip 9, Anything Else to Exit")
	print("For example John Wick vs 2001 A Space Odyssey")
	print("You would enter 1 since John wick is better")
	
	if choice == 1:
		media_type = select_media_type()	
		keys = [key for key in medias.keys() if medias[key].media_type == media_type]
		combinations = list(itertools.combinations(keys,2))
		while combinations:
			print(len(combinations))
			pair = combinations.pop(random.randint(0,len(combinations)-1))
			if generate_rating_for_pair(pair) == -1:
				break
			
	elif choice == 2:
		name = input("Type the name of the media you want to generate ratings for: ")
		if name not in medias:
			print("This name is not present in the database")
			return
		for key in medias.keys():
			if key == name: continue
			if medias[key].media_type == medias[name].media_type:
				if generate_rating_for_pair((key, name)) == -1:
					break

	unload(0)
	return

def generate_rating_for_pair(pair):
	if pair[1] in medias[pair[0]].relative_ratings:
		return
	else:
		rating = int(input(f"{pair[0]}     vs     {pair[1]}:     "))
		if rating == 9: return
		if rating not in [1,2,3]: return -1
		rating -= 2
		medias[pair[0]].relative_ratings[pair[1]] = rating * -1
		medias[pair[1]].relative_ratings[pair[0]] = rating * 1

###Importing data
medias = load()


def convert_to_proto(medias):
	new_medias = media_pb2.Catalogue()
	for media in medias.values():
		new_media = media_pb2.Media()
		new_media.name = media.name
		if media.rating:
			new_media.rating = media.rating
		if media.media_type == "Game":
			new_media.type = media_pb2.MediaType.GAME
		elif media.media_type == "TV Show":
			new_media.type = media_pb2.MediaType.TVSHOW
		elif media.media_type == "Film":
			new_media.type = media_pb2.MediaType.MOVIE
		if media.date_finished:
			new_media.date_finished.FromDatetime(media.date_finished)
		new_medias.medias.append(new_media)
	return new_medias

new_medias = convert_to_proto(medias)
with open("medias2.bin","wb") as f:
	f.write(new_medias.SerializeToString())