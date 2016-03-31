import os
import shutil


class MediaFixture:
    def build_media_directory(self, directory_path, subdirectories, media_paths):
        self.delete_media_directory(directory_path)
        self._create_medias_directory(directory_path, subdirectories)
        self._populate_media_directory(media_paths)

    def delete_media_directory(self, directory_path):
        if os.path.exists(directory_path):
            if os.path.isdir(directory_path):
                shutil.rmtree(directory_path)
            else:
                os.remove(directory_path)

    def _create_medias_directory(self, directory_path, subdirectories):
        os.mkdir(directory_path)

        for subdirectory in subdirectories:
            os.mkdir(os.path.join(directory_path, subdirectory))

    def _populate_media_directory(self, media_paths):
        for path in media_paths:
            open(path, "a").close()
