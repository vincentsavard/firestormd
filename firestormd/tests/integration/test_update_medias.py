import os
import unittest

from firestormd.media.mediarepository import MediaRepository
from firestormd.media.mediafinder import MediaFinder
from firestormd.media.memorymediadatabase import MemoryMediaDatabase
from firestormd.tests.fixtures.mediafixture import MediaFixture
from firestormd.utils import TemporarilyAddedFile, TemporarilyRemovedFile

DATA_PATH = "./firestormd/tests/data/"
MEDIA_DIRECTORY_PATH = os.path.join(DATA_PATH, "medias1")
SUBDIRECTORIES = ["subdir"]
MEDIA_PATHS = [os.path.join(MEDIA_DIRECTORY_PATH, media_path)
               for media_path in ("video1.avi", "video2.mp4", "subdir/video3.avi")]
NON_MEDIA_PATHS = [os.path.join(MEDIA_DIRECTORY_PATH, media_path)
                   for media_path in ("foo.txt",)]
ANOTHER_MEDIA_PATH = os.path.join(MEDIA_DIRECTORY_PATH, "video4.mp4")
VALID_EXTENSIONS = [".avi", ".mp4"]


class TestUpdateMedias(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.media_fixture = MediaFixture()
        cls.media_fixture.build_media_directory(MEDIA_DIRECTORY_PATH, SUBDIRECTORIES, MEDIA_PATHS)

    @classmethod
    def tearDownClass(cls):
        cls.media_fixture.delete_media_directory(MEDIA_DIRECTORY_PATH)

    def setUp(self):
        self.media_database = MemoryMediaDatabase()
        self.media_finder = MediaFinder(MEDIA_DIRECTORY_PATH, VALID_EXTENSIONS)
        self.media_repository = MediaRepository(self.media_database, self.media_finder)

    def test_when_calling_get_all_medias_before_updating_then_no_medias_are_returned(self):
        medias = self.media_repository.get_all_medias()

        self.assertEqual(len(medias), 0)

    def test_when_calling_get_all_medias_after_updating_then_some_medias_are_returned(self):
        self.media_repository.update()
        medias = self.media_repository.get_all_medias()

        self.assertEqual(len(medias), len(MEDIA_PATHS))

    def test_when_calling_update_after_removing_a_media_then_one_less_media_is_returned(self):
        a_media_filepath = MEDIA_PATHS[0]

        with TemporarilyRemovedFile(a_media_filepath):
            self.media_repository.update()
            medias = self.media_repository.get_all_medias()

            self.assertEqual(len(medias), len(MEDIA_PATHS) - 1)

    def test_when_calling_update_after_adding_a_media_then_one_more_media_is_returned(self):
        a_media_filepath = ANOTHER_MEDIA_PATH

        with TemporarilyAddedFile(a_media_filepath):
            self.media_repository.update()
            medias = self.media_repository.get_all_medias()

            self.assertEqual(len(medias), len(MEDIA_PATHS) + 1)


if __name__ == "__main__":
    unittest.main()
