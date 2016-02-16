import os
import subprocess

COMMAND = "mplayer"
PLAY_COMMAND = b" "
PAUSE_COMMAND = b" "
STOP_COMMAND = b"q"

class MPlayerDriver:
    def __init__(self):
        self._process = None

    def play(self, filepath):
        if not self._is_process_started():
            self._process = subprocess.Popen([COMMAND, filepath],
                                             stdout=open(os.devnull, "w"),
                                             stderr=subprocess.STDOUT, stdin=subprocess.PIPE)
        else:
            self._send_command(PLAY_COMMAND)

    def pause(self):
        self._send_command(PAUSE_COMMAND)

    def stop(self):
        self._send_command(STOP_COMMAND)
            
    def _is_process_started(self):
        return self._process is not None and self._process.poll() is None

    def _send_command(self, input_bytestring):
        if self._is_process_started():
            self._process.stdin.write(input_bytestring)
            self._process.stdin.flush()
