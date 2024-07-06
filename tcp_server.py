#!/usr/bin/env python3

import socket

host = '127.0.0.1'
port = 12345
BUFFER_SIZE = 1024


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_tcp:
    socket_tcp.bind((host, port))

    socket_tcp.listen(5)

    connection, addr = socket_tcp.accept()
    with connection:
        print('[*] Established connection')
        while True:
            data = connection.recv(BUFFER_SIZE)
            if not data:
                break
            else:
                print('[*] Data received: {}'.format(data.decode('utf-8')))
            connection.send(data)
