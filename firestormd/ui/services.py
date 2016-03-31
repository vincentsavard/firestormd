import os

from firestormd.config.configuration import Configuration
from firestormd.media.mediaplayer import MediaPlayer
from firestormd.media.mediafinder import MediaFinder
from firestormd.media.mediadatabase import MemoryMediaDatabase
from firestormd.media.mediarepository import MediaRepository
from firestormd.media.drivers.clidriver import CLIDriver
from firestormd.service.mediaservice import MediaService

CONFIG_FILE = ".firestormrc"


def load_configuration():
    directories_to_look_into = [os.curdir, os.path.expanduser("~")]

    for directory in directories_to_look_into:
        if os.path.exists(os.path.join(directory, CONFIG_FILE)):
            with open(os.path.join(directory, CONFIG_FILE)) as file_handle:
                return Configuration(file_handle.read())

    return Configuration()

_CONFIG = load_configuration()

_media_database = MemoryMediaDatabase()
_media_finder = MediaFinder(_CONFIG["videos"]["directory"].value, _CONFIG["videos"]["extensions"].value)
_media_repository = MediaRepository(_media_database, _media_finder)
_media_driver = CLIDriver(_CONFIG["videos"]["driver"].value)
_media_player = MediaPlayer(_media_driver)
media_service = MediaService(_media_repository, _media_player)
