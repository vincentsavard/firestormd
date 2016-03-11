class Media:
    def __init__(self, id, uri):
        self._id = id
        self._uri = uri

    @property
    def id(self):
        return self._id

    @property
    def uri(self):
        return self._uri

    def to_dict(self):
        return {
            "id": self._id,
            "uri": self._uri
        }

    def __eq__(self, other_media):
        return self._id == other_media._id and self._uri == other_media._uri

    def __hash__(self):
        return hash("{0}+{1}".format(self._id, self._uri))

    def __repr__(self):
        return "Media<id={0}, uri={1}>".format(self._id, self._uri)
