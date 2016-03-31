import subprocess

from firestormd.media.exceptions import UnsupportedCLIDriver


class CLICommands:
    def __init__(self, command, play_command, pause_command, stop_command):
        self._command = command
        self._play_command = play_command
        self._pause_command = pause_command
        self._stop_command = stop_command

    @property
    def command(self):
        return self._command

    @property
    def play_command(self):
        return self._play_command

    @property
    def pause_command(self):
        return self._pause_command

    @property
    def stop_command(self):
        return self._stop_command

SUPPORTED_DRIVERS = {
    "mplayer": CLICommands(["mplayer"], b" ", b" ", b"q"),
    "omxplayer": CLICommands(["omxplayer", "-o", "hdmi"], b" ", b" ", b"q"),
}


class CLIDriver:
    def __init__(self, driver):
        self._process = None

        try:
            self._commands = SUPPORTED_DRIVERS[driver]
        except KeyError:
            raise UnsupportedCLIDriver("'{0}' is not supported.")

    def play(self, filepath):
        if not self._is_process_started():
            self._process = subprocess.Popen(self._commands.command + [filepath],
                                             bufsize=0,
                                             stdout=subprocess.PIPE,
                                             stderr=subprocess.PIPE,
                                             stdin=subprocess.PIPE)
        else:
            self._send_command(self._commands.play_command)

    def pause(self):
        self._send_command(self._commands.pause_command)

    def stop(self):
        self._send_command(self._commands.stop_command)

    def _is_process_started(self):
        return self._process is not None and self._process.poll() is None

    def _send_command(self, input_bytestring):
        if self._is_process_started():
            self._process.stdin.write(input_bytestring)
            self._process.stdin.flush()
