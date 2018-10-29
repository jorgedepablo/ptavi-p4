#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import socketserver
import sys

class EchoHandler(socketserver.DatagramRequestHandler):
    """
    Echo server class
    """

    def handle(self):
        """
        handle method of the server class
        (all requests will be handled by this method)
        """
        self.wfile.write(b'Received request')
        for line in self.rfile:
            print('The client send us ', line.decode('utf-8'))
        print('IP: ', self.client_address[0], 'Port: ', self.client_address[1])

if __name__ == "__main__":
    # Listens at localhost ('')
    # and calls the EchoHandler class to manage the request
    PORT = int(sys.argv[2])
    serv = socketserver.UDPServer(('', PORT), EchoHandler)

    print('Runnig echo server UDP...')
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        print('Server interrupt')
