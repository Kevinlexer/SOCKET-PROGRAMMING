#!/usr/bin/env python3

import socket

host = '127.0.0.1'
port = 12345
BUFFER_SIZE = 1024

MESSAGE = 'Hello guys this is your first message'

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_tcp:
    socket_tcp.connect((host, port))
    socket_tcp.send(MESSAGE.encode('utf-8'))
    data = socket_tcp.recv(BUFFER_SIZE)