#!/usr/bin/env python
import subprocess

CURRENT_BRANCH_COMMAND = "git rev-parse --abbrev-ref HEAD"
CURRENT_REVISION_COMMAND = "git rev-parse --short HEAD"

VERSION_PY_CONTENT = """# auto-generated file
VERSION = "{0}"
"""

class CouldNotFindBranchNameError(Exception): pass

def get_current_branch():
    return execute_command(CURRENT_BRANCH_COMMAND.split())

def get_current_revision():
    return execute_command(CURRENT_REVISION_COMMAND.split())

def execute_command(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE)
    return process.stdout.read().decode("utf-8").strip()

def write_version_py_file():
    with open("./firestormd/version.py", "w") as file_handle:
        file_handle.write(VERSION_PY_CONTENT.format(get_current_revision()))

if __name__ == "__main__":
    write_version_py_file()
