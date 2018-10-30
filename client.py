#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Client UDP implement a socket to a server
"""

import socket
import sys

try:
    SERVER = sys.argv[1]
    PORT = int(sys.argv[2])
    USER = sys.argv[4]
    EXPIRES = int(sys.argv[5])
except IndexError or ValueError:
   sys.exit('Usage: python3 client.py "server" "port" register "user-name" "expires time"')

def register():
    """
    rescribir esto
    """
    REGISTER = 'REGISTER sip:'+ USER + ' SIP/2.0\r\n' + 'Expires: ' + str(EXPIRES)
    my_socket.send(bytes(REGISTER, 'utf-8') + b'\r\n\r\n')


with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as my_socket:
    my_socket.connect((SERVER, PORT))
    if sys.argv[3] == 'register':
        register()
    data = my_socket.recv(1024)
    print('Received -- ', data.decode('utf-8'))

print("Socket done.")
