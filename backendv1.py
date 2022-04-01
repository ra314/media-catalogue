# Defining the media Class
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

medias = load()