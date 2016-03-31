import unittest
from unittest.mock import Mock

from firestormd.media.mediaplayer import MediaPlayer
from firestormd.media.media import Media
from firestormd.media.exceptions import NoMediaLoadedError, MediaAlreadyPlayingError, NoMediaPlayingError

A_MEDIA = Media(1, "uri")


class TestMediaPlayer(unittest.TestCase):
    def setUp(self):
        self.media_driver = Mock()
        self.media_player = MediaPlayer(self.media_driver)

    def test_when_no_media_is_loaded_then_is_media_loaded_returns_false(self):
        self.assertFalse(self.media_player._is_media_loaded())

    def test_when_a_media_is_loaded_then_is_media_loaded_returns_true(self):
        self.media_player.load(A_MEDIA)
        self.assertTrue(self.media_player._is_media_loaded())

    def test_when_loading_a_media_then_unloading_then_is_media_loaded_returns_false(self):
        self.media_player.load(A_MEDIA)
        self.media_player.unload()

        self.assertFalse(self.media_player._is_media_loaded())

    def test_given_no_media_loaded_when_unloading_then_nomedialoadederror_is_raised(self):
        with self.assertRaises(NoMediaLoadedError):
            self.media_player.unload()

    def test_given_no_media_loaded_when_calling_play_then_nomedialoadederror_is_raised(self):
        with self.assertRaises(NoMediaLoadedError):
            self.media_player.play()

        self.assertFalse(self.media_driver.play.called)

    def test_given_no_media_loaded_when_calling_pause_then_nomedialoadederror_is_raised(self):
        with self.assertRaises(NoMediaLoadedError):
            self.media_player.pause()

        self.assertFalse(self.media_driver.pause.called)

    def test_given_no_media_loaded_when_calling_stop_then_nomedialoadederror_is_raised(self):
        with self.assertRaises(NoMediaLoadedError):
            self.media_player.stop()

        self.assertFalse(self.media_driver.stop.called)

    def test_given_a_media_loaded_when_calling_play_then_driver_play_is_called(self):
        self.media_player.load(A_MEDIA)
        self.media_player.play()

        self.assertTrue(self.media_driver.play.called)

    def test_given_a_media_playing_when_calling_pause_then_driver_pause_is_called(self):
        self.media_player.load(A_MEDIA)
        self.media_player.play()
        self.media_player.pause()

        self.assertTrue(self.media_driver.pause.called)

    def test_given_a_media_playing_when_calling_stop_then_driver_stop_is_called(self):
        self.media_player.load(A_MEDIA)
        self.media_player.play()
        self.media_player.stop()

        self.assertTrue(self.media_driver.stop.called)

    def test_given_no_media_loaded_when_calling_is_playing_then_returns_false(self):
        self.assertFalse(self.media_player.is_playing())

    def test_given_a_media_playing_when_calling_is_playing_after_play_then_returns_true(self):
        self.media_player.load(A_MEDIA)
        self.media_player.play()

        self.assertTrue(self.media_player.is_playing())

    def test_given_a_media_playing_when_pausing_then_is_playing_returns_false(self):
        self.media_player.load(A_MEDIA)
        self.media_player.play()
        self.media_player.pause()

        self.assertFalse(self.media_player.is_playing())

    def test_given_a_media_playing_when_stopping_then_is_playing_returns_false(self):
        self.media_player.load(A_MEDIA)
        self.media_player.play()
        self.media_player.stop()

        self.assertFalse(self.media_player.is_playing())

    def test_given_a_media_paused_when_stopping_then_is_playing_returns_false(self):
        self.media_player.load(A_MEDIA)
        self.media_player.play()
        self.media_player.pause()
        self.media_player.stop()

        self.assertFalse(self.media_player.is_playing())

    def test_given_a_media_playing_when_calling_play_then_mediaalreadyplayingerror_is_raised(self):
        self.media_player.load(A_MEDIA)
        self.media_player.play()

        with self.assertRaises(MediaAlreadyPlayingError):
            self.media_player.play()

    def test_given_no_media_playing_when_calling_pause_then_nomediaplayingerror_is_raised(self):
        self.media_player.load(A_MEDIA)

        with self.assertRaises(NoMediaPlayingError):
            self.media_player.pause()

    def test_given_no_media_loaded_when_calling_get_status_as_dict_then_media_is_none_and_is_not_playing(self):
        status = self.media_player.get_status_as_dict()

        self.assertTrue(status["loaded_media"] is None)
        self.assertFalse(status["is_playing"])

    def test_given_a_loaded_media_when_calling_get_status_as_dict_then_media_is_set_and_is_not_playing(self):
        self.media_player.load(A_MEDIA)
        status = self.media_player.get_status_as_dict()

        self.assertEqual(status["loaded_media"], A_MEDIA.to_dict())
        self.assertFalse(status["is_playing"])

    def test_given_a_loaded_media_playing_when_calling_get_status_as_dict_then_media_is_set_and_is_playing(self):
        self.media_player.load(A_MEDIA)
        self.media_player.play()
        status = self.media_player.get_status_as_dict()

        self.assertEqual(status["loaded_media"], A_MEDIA.to_dict())
        self.assertTrue(status["is_playing"])


if __name__ == "__main__":
    unittest.main()
