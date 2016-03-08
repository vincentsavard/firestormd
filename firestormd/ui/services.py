from firestormd.media.mediaplayer import MediaPlayer
from firestormd.media.mediafinder import MediaFinder
from firestormd.media.mediadatabase import MemoryMediaDatabase
from firestormd.media.mediarepository import MediaRepository
from firestormd.media.drivers.mplayer import MPlayerDriver
from firestormd.service.mediaservice import MediaService

_MEDIA_EXTENSIONS = [".avi", ".mp4"]
_MEDIA_DIRECTORY = "/home/vincent/dev/projects/void/pyrite/pyrited/build/data"

_media_database = MemoryMediaDatabase()
_media_finder = MediaFinder(_MEDIA_DIRECTORY, _MEDIA_EXTENSIONS)
_media_repository = MediaRepository(_media_database, _media_finder)
_media_driver = MPlayerDriver()
_media_player = MediaPlayer(_media_driver)
media_service = MediaService(_media_repository, _media_player)
