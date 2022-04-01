import media_pb2

# Defining the media Class
class MediaClass:	
	def __init__(self, media: media_pb2.Media):
		self.media = media
		
	def __str__(self):
		date = self.media.date_finished.ToDatetime().strftime('%d/%m/%Y') if self.media.HasField("date_finished") else "NA"
		rating = self.media.rating.value if self.media.HasField("rating") else "NA"
		return ("{: <5} {: <50} {: <15} {: <20}".format(rating, self.media.name, date, media_pb2.MediaType.keys()[self.media.type]))

### Data IO
def load():
	with open("medias3.bin","rb") as f:
		catalog = media_pb2.Catalogue()
		catalog.ParseFromString(f.read())
		# catalog_dict = {media.name : media for media in catalog.medias}
		return catalog

def unload(medias):
	with open("medias3.bin","wb") as f:
		f.write(medias.SerializeToString())

### Importing data
def convert_to_proto(medias):
	new_medias = media_pb2.Catalogue()
	for media in medias.values():
		new_media = media_pb2.Media()
		new_media.name = media.name
		if media.rating:
			new_media.rating.value = media.rating
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

