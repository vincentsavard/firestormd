class Media:
    def __init__(self, media_id, uri, title, year=None):
        self._id = media_id
        self._title = title
        self._year = year
        self._uri = uri

    @property
    def id(self):
        return self._id

    @property
    def title(self):
        return self._title

    @property
    def year(self):
        return self._year

    @property
    def uri(self):
        return self._uri

    def to_dict(self):
        return {
            "id": self._id,
            "title": self._title,
            "year": self._year,
            "uri": self._uri
        }

    def __eq__(self, other_media):
        return \
            self._id == other_media.id and \
            self._title == other_media.title and \
            self._year == other_media.year and \
            self._uri == other_media.uri

    def __hash__(self):
        return hash("{0}+{1}".format(self._id, self._uri))

    def __repr__(self):
        return "Media<id={0}, title={1}, uri={2}>".format(
            self._id, self._title, self._uri
        )
