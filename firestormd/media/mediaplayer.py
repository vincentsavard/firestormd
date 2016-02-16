import enum

from firestormd.media.exceptions import NoMediaLoadedError, MediaAlreadyPlayingError, NoMediaPlayingError

class MediaPlayer:
    def __init__(self, driver):
        self._driver = driver
        self._media = None
        self._is_playing = False

    def load(self, media):
        if self._is_media_loaded():
            self._driver.stop()

        self._media = media

    def unload(self):
        if self._is_media_loaded():
            self._driver.stop()
            self._media = None
        else:
            raise NoMediaLoadedError

    def play(self):
        if not self._is_media_loaded():
            raise NoMediaLoadedError

        if self.is_playing():
            raise MediaAlreadyPlayingError("self._media={0}".format(repr(self._media)))

        self._driver.play(self._media.uri)
        self._is_playing = True

    def pause(self):
        if not self._is_media_loaded():
            raise NoMediaLoadedError

        if not self.is_playing():
            raise NoMediaPlayingError("self._media={0}".format(repr(self._media)))

        self._driver.pause()
        self._is_playing = False

    def stop(self):
        if not self._is_media_loaded():
            raise NoMediaLoadedError

        self._driver.stop()
        self._is_playing = False

    def is_playing(self):
        return self._is_playing

    def _is_media_loaded(self):
        return self._media is not None
