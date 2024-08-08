"""
Day 10 - Networking
"""

import socket
import re
MY_SOCKET = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
MY_SOCKET.connect(('data.pr4e.org',80))

CMD = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
MY_SOCKET.send(CMD)
TEXT = ''
while True:
    data = MY_SOCKET.recv(512)
    if len(data) < 1:
        break
    TEXT = TEXT + data.decode()
MY_SOCKET.close()
PARSED_TEXT = ''
UNPARSED_TEXT = re.findall(r'.+',TEXT)
for line in UNPARSED_TEXT:
    PARSED_TEXT = PARSED_TEXT + line + ' '
print(PARSED_TEXT)


