class MediaDatabase:
    def id_exists(self, media_id):
        raise NotImplementedError()

    def uri_exists(self, media_uri):
        raise NotImplementedError()

    def save(self, uri, title, year=None):
        raise NotImplementedError()

    def delete_by_uri(self, media_uri):
        raise NotImplementedError()

    def get_all_medias(self):
        raise NotImplementedError()

    def get_by_id(self, media_id):
        raise NotImplementedError()

    def calculate_next_id(self):
        raise NotImplementedError()
