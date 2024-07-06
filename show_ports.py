#!/usr/bin/env python3
import socket

def find_serv_name():
    protocolName = 'tcp'
    for port in [80, 25]:
        print("Port: %s => service name: %s" %(port, socket.getservbyport(port, protocolName)))

    print("Port: %s => service name: %s" %(53, socket.getservbyport(53, 'udp')))

if __name__ =='__main__':
    find_serv_name()