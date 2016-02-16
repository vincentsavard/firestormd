from firestormd.media.media import Media
from firestormd.media.mediadatabase import MemoryMediaDatabase
from firestormd.media.exceptions import MediaAlreadyExistsError, NoMediaFoundError

class MediaRepository:
    def __init__(self, media_database, media_finder):
        self._media_database = media_database
        self._media_finder = media_finder

    def add(self, media):
        if self._media_database.id_exists(media.id):
            raise MediaAlreadyExistsError("media.id={0}, media={1}".format(media.id, repr(media)))

        if self._media_database.uri_exists(media.uri):
            raise MediaAlreadyExistsError("media.uri={0}, media={1}".format(media.uri, repr(media)))
        
        self._media_database.save(media)

    def update(self):
        media_uris = set(media.uri for media in self.get_all_medias())
        media_filepaths = self._media_finder.find_medias()
        uris_to_remove = media_uris - media_filepaths
        uris_to_add = media_filepaths - media_uris

        for uri in uris_to_remove:
            self._media_database.delete_by_uri(uri)

        for uri in uris_to_add:
            self.add(self._create_media(uri))

    def get_all_medias(self):
        return self._media_database.get_all_medias()

    def get_by_id(self, media_id):
        if self._media_database.id_exists(media_id):
            return self._media_database.get_by_id(media_id)
        else:
            raise NoMediaFoundError("media_id={0}".format(media_id))

    def _create_media(self, uri):
        return Media(self._media_database.calculate_next_id(), uri)
