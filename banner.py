#!/usr/bin/python3

import socket
import re

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('www.skilledarmy.com', 80))
httpGet = b"Get / HTTP/1.1\nHost: www.skilledarmy.com\n\n"
data = ''
try:
    sock.sendall(httpGet)
    data = sock.recvfrom(1024)
    strdata=data[0]
    headers = strdata.splitlines()
    for header in headers:
        print(header.decode())
except socket.error:
    print("Socket error", socket.error)
finally:
    print('closing connection')
    sock.close()