from firestorm.media.mediaplayer import MediaPlayer
from firestorm.media.mediafinder import MediaFinder
from firestorm.media.mediadatabase import MemoryMediaDatabase
from firestorm.media.mediarepository import MediaRepository
from firestorm.media.drivers.mplayer import MPlayerDriver
from firestorm.service.mediaservice import MediaService

_MEDIA_EXTENSIONS = [".avi", ".mp4"]
_MEDIA_DIRECTORY = "/home/vincent/dev/projects/void/pyrite/pyrited/build/data"

_media_database = MemoryMediaDatabase()
_media_finder = MediaFinder(_MEDIA_DIRECTORY, _MEDIA_EXTENSIONS)
_media_repository = MediaRepository(_media_database, _media_finder)
_media_driver = MPlayerDriver()
_media_player = MediaPlayer(_media_driver)
media_service = MediaService(_media_repository, _media_player)
