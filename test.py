import whodis
import pytest
import subprocess
from whodis import ui_utils

whodis_proc = subprocess.Popen(['python', 'whodis/whodis.py'], 
                                   stdout=subprocess.PIPE, stdin=subprocess.PIPE)

# whodis_output = whodis_proc.communicate()[0]
# print(whodis_output)
# whodis_output = whodis_proc.communicate(input='1'.encode())[0]
# print(whodis_output)
# print("--==--==--==--==--")
# expected_output = b"\r\n          _               _ _     \r\n__      _| |__   ___   __| (_)___ \r\n\\ \\ /\\ / / '_ \\ / _ \\ / _` | / __|\r\n \\ V  V /| | | | (_) | (_| | \\__ \\\r\n  \\_/\\_/ |_| |_|\\___/ \\__,_|_|___/\r\n-----------------------------------\r\n\r\n1) Fake login page 2) Some other option 3) Another feature\r\n\r\n> Please enter your choice: \x1b[1A\x1b[2K\x1b[1A\x1b[2K\x1b[1A\x1b[2KAvailable login pages:\r\n\r\n1) Test Example\r\n\r\n> Please choose a login page: "
# print(whodis_output.decode())

# print(whodis_output == expected_outpu