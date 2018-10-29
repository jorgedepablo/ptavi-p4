#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Client UDP implement a socket to a server
"""

import socket
import sys

# Constants. IP adress of the serser and content to send
try:
    SERVER = sys.argv[1]
    PORT = int(sys.argv[2])
    LINE = sys.argv[3:]
except IndexError or ValueError:
    sys.exit('Usage: python3 client.py "server" "port" "line" ')

def register():
    USER = sys.argv[4]
    REGISTER = 'REGISTER sip:'+ USER + ' SIP/2.0'
    my_socket.send(bytes(REGISTER, 'utf-8') + b'\r\n\r\n')

# Create the socket, config it and connect it to a server/port
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as my_socket:
    my_socket.connect((SERVER, PORT))
    if sys.argv[3] == 'register':
        register()
    else:
        LINE = ' '.join(LINE)
        print('Sending:', LINE)
        my_socket.send(bytes(LINE, 'utf-8') + b'\r\n')

    data = my_socket.recv(1024)
    print('Received -- ', data.decode('utf-8'))

print("Socket done.")
