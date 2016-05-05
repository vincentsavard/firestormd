import os
import sqlite3

from firestormd.media.exceptions import MediaAlreadyExistsError, NoMediaFoundError
from firestormd.media.media import Media
from firestormd.media.mediadatabase import MediaDatabase


CREATE_TABLE_MEDIA_STATEMENT = """
CREATE TABLE media (
  id INTEGER,
  title VARCHAR NOT NULL,
  year INTEGER,
  uri VARCHAR UNIQUE NOT NULL,
  PRIMARY KEY(id)
)
"""


class SQLiteMediaDatabase(MediaDatabase):
    def __init__(self, database_path):
        self._database_path = database_path
        self._setup_database()

    def id_exists(self, media_id):
        with sqlite3.connect(self._database_path) as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT id FROM media WHERE id = ?", (media_id,))

            return cursor.fetchone() is not None

    def uri_exists(self, media_uri):
        with sqlite3.connect(self._database_path) as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT id FROM media WHERE uri = ?", (media_uri,))

            return cursor.fetchone() is not None

    def save(self, uri, title, year=None):
        try:
            with sqlite3.connect(self._database_path) as connection:
                connection.execute(
                    "INSERT INTO media (title, year, uri) VALUES (?, ?, ?)",
                    (title, year, uri)
                )
        except sqlite3.IntegrityError:
            raise MediaAlreadyExistsError

    def delete_by_uri(self, media_uri):
        if not self.uri_exists(media_uri):
            raise NoMediaFoundError

        with sqlite3.connect(self._database_path) as connection:
            connection.execute("DELETE FROM media WHERE uri = ?", (media_uri,))

    def get_all_medias(self):
        medias = set()

        with sqlite3.connect(self._database_path) as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT id, uri, title, year FROM media")

            for row in cursor:
                medias.add(Media(row[0], row[1], row[2], row[3]))

        return medias

    def get_by_id(self, media_id):
        if not self.id_exists(media_id):
            raise NoMediaFoundError

        with sqlite3.connect(self._database_path) as connection:
            cursor = connection.cursor()
            cursor.execute(
                "SELECT id, uri, title, year FROM media WHERE id = ?",
                (media_id,)
            )
            row = cursor.fetchone()

        return Media(row[0], row[1], row[2], row[3])

    def calculate_next_id(self):
        pass

    def _setup_database(self):
        if not os.path.isfile(self._database_path):
            with sqlite3.connect(self._database_path) as connection:
                connection.execute(CREATE_TABLE_MEDIA_STATEMENT)
