class MediaService:
    def __init__(self, media_repository, media_player):
        self._media_repository = media_repository
        self._media_player = media_player

    def update(self):
        self._media_repository.update()

    def get_all_medias(self):
        return self._media_repository.get_all_medias()

    def get_by_id(self, media_id):
        return self._media_repository.get_by_id(media_id)

    def load_media_by_id(self, media_id):
        media = self._media_repository.get_by_id(media_id)
        self._media_player.load(media)

    def play_loaded_media(self):
        self._media_player.play()

    def pause_loaded_media(self):
        self._media_player.pause()

    def stop_loaded_media(self):
        self._media_player.stop()

    def get_player_status(self):
        return self._media_player.get_status_as_dict()
