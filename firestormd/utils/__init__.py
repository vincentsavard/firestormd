import os


class TemporarilyAddedFile:
    def __init__(self, filepath):
        self._filepath = filepath

    def __enter__(self):
        if os.path.exists(self._filepath):
            raise ValueError("'{0}' already exists.".format(self._filepath))

        open(self._filepath, "a").close()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        try:
            os.remove(self._filepath)
        except OSError:
            pass


class TemporarilyRemovedFile:
    def __init__(self, filepath):
        self._filepath = filepath
        self._content = ""

    def __enter__(self):
        if not os.path.exists(self._filepath):
            raise ValueError("'{0}' does not exist.".format(self._filepath))

        with open(self._filepath) as file_handle:
            self._content = file_handle.read()

        os.remove(self._filepath)

    def __exit__(self, exc_type, exc_value, traceback):
        with open(self._filepath, "a") as file_handle:
            file_handle.write(self._content)
