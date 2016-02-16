import os

class MediaFinder:
    def __init__(self, path, valid_extensions):
        self.__path = path
        self.__valid_extensions = valid_extensions
        
    def find_medias(self):
        media_filepaths = set()
    
        for directory_path, _, filenames in os.walk(self.__path):
            for filename in filenames:
                for extension in self.__valid_extensions:
                    if filename.lower().endswith(extension):
                        media_filepaths.add(os.path.join(directory_path, filename))
                        break

        return media_filepaths
