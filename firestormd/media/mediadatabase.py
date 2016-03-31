from firestormd.media.exceptions import NoMediaFoundError


class MemoryMediaDatabase:
    def __init__(self):
        self._medias = set()
        self._next_id = 1

    def id_exists(self, media_id):
        for media in self._medias:
            if media.id == media_id:
                return True
        return False

    def uri_exists(self, media_uri):
        for media in self._medias:
            if media.uri == media_uri:
                return True
        return False

    def save(self, media):
        self._medias.add(media)

    def delete_by_uri(self, media_uri):
        self._medias.remove(self.get_by_uri(media_uri))

    def get_all_medias(self):
        return set(self._medias)

    def get_by_id(self, media_id):
        for media in self._medias:
            if media.id == media_id:
                return media

        raise NoMediaFoundError("MemoryMediaDatabase.get_by_id({0})".format(media_id))

    def get_by_uri(self, media_uri):
        for media in self._medias:
            if media.uri == media_uri:
                return media

        raise NoMediaFoundError("MemoryMediaDatabase.get_by_uri({0})".format(media_uri))

    def calculate_next_id(self):
        next_id = self._next_id
        self._next_id += 1

        return next_id
