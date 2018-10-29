#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Programa cliente UDP que abre un socket a un servidor
"""

import socket
import sys

# Constantes. Dirección IP del servidor y contenido a enviar
try:
    SERVER = sys.argv[1]
    PORT = int(sys.argv[2])
    LINE = sys.argv[3:]
except IndexError or ValueError:
    sys.exit('Usage: python3 client.py "server" "port" "line" ')

# Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as my_socket:
    my_socket.connect((SERVER, PORT))
    LINE = ' '.join(LINE)
    print('Sending:', LINE)
    my_socket.send(bytes(LINE, 'utf-8') + b'\r\n')
    data = my_socket.recv(1024)
    print('Received -- ', data.decode('utf-8'))

print("Socket done.")
