import media_pb2
import backendv1

### Data IO
def load():
	with open("medias2.bin","rb") as f:
		medias = media_pb2.Catalogue()
		medias.ParseFromString(f.read())
		return medias

def unload(medias, exit_code):
	with open("medias2.bin","wb") as f:
		f.write(medias.SerializeToString())

### Importing data
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

