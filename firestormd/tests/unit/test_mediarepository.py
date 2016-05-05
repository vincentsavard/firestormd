import unittest
from unittest.mock import Mock

from firestormd.media.mediarepository import MediaRepository
from firestormd.media.memorymediadatabase import MemoryMediaDatabase
from firestormd.media.media import Media
from firestormd.media.exceptions import MediaAlreadyExistsError, NoMediaFoundError

A_MEDIA_TITLE = "title"
A_MEDIA_ID = 1
ANOTHER_MEDIA_ID = 2
A_MEDIA_URI = "media1"
ANOTHER_MEDIA_URI = "media2"
A_NON_EXISTING_ID = 42
MEDIA_PATHS = {"media1", "media2", "media3"}


class TestMediaRepository(unittest.TestCase):
    def setUp(self):
        self.media_database = MemoryMediaDatabase()
        self.media_finder = self.create_mock_media_finder()
        self.media_repository = MediaRepository(self.media_database, self.media_finder)

    def create_mock_media_finder(self):
        media_finder = Mock()
        media_finder.find_medias.return_value = MEDIA_PATHS

        return media_finder

    def test_when_calling_get_all_medias_before_adding_medias_then_no_medias_are_returned(self):
        medias = self.media_repository.get_all_medias()

        self.assertEqual(len(medias), 0)

    def test_when_calling_get_all_medias_after_adding_a_media_then_one_media_is_returned(self):
        a_media = Media(A_MEDIA_ID, A_MEDIA_URI, A_MEDIA_TITLE)
        self.media_repository.add(a_media)
        medias = self.media_repository.get_all_medias()

        self.assertEqual(len(medias), 1)

    def test_when_adding_a_media_twice_then_mediaalreadyexistserror_is_raised(self):
        a_media = Media(A_MEDIA_ID, A_MEDIA_URI, A_MEDIA_TITLE)
        self.media_repository.add(a_media)

        with self.assertRaises(MediaAlreadyExistsError):
            self.media_repository.add(a_media)

    def test_when_adding_a_media_with_an_id_that_already_exists_then_mediaalreadyexistserror_is_raised(self):
        a_media = Media(A_MEDIA_ID, A_MEDIA_URI, A_MEDIA_TITLE)
        another_media = Media(A_MEDIA_ID, ANOTHER_MEDIA_URI, A_MEDIA_TITLE)
        self.media_repository.add(a_media)

        with self.assertRaises(MediaAlreadyExistsError):
            self.media_repository.add(another_media)

    def test_when_adding_a_media_with_an_uri_that_already_exists_then_mediaalreadyexistserror_is_raised(self):
        a_media = Media(A_MEDIA_ID, A_MEDIA_URI, A_MEDIA_TITLE)
        another_media = Media(ANOTHER_MEDIA_ID, A_MEDIA_URI, A_MEDIA_TITLE)
        self.media_repository.add(a_media)

        with self.assertRaises(MediaAlreadyExistsError):
            self.media_repository.add(another_media)

    def test_given_an_existing_media_when_calling_get_by_id_then_same_media_is_returned(self):
        a_media = Media(A_MEDIA_ID, A_MEDIA_URI, A_MEDIA_TITLE)
        self.media_repository.add(a_media)

        self.assertEqual(self.media_repository.get_by_id(A_MEDIA_ID), a_media)

    def test_given_no_medias_when_calling_get_by_id_then_nomediafounderror_is_raised(self):
        with self.assertRaises(NoMediaFoundError):
            self.media_repository.get_by_id(A_NON_EXISTING_ID)

    def test_given_a_media_finder_with_medias_when_calling_update_then_same_amount_of_medias_are_returned(self):
        self.media_repository.update()
        medias = self.media_repository.get_all_medias()

        self.assertEqual(len(medias), len(MEDIA_PATHS))


if __name__ == "__main__":
    unittest.main()
