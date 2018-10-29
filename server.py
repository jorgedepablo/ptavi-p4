#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Class (and main program) for echo server in UDP simple
"""

import socketserver
import sys

class SIPRegisterHandler(socketserver.DatagramRequestHandler):
    """
    Echo server class
    """
    dicc_Data = {}
    def handle(self):
        """
        handle method of the server class
        (all requests will be handled by this method)
        """
        for line in self.rfile:
            DATA = line.decode('utf-8').split()
            if DATA:
                if DATA[0] == 'REGISTER':
                    self.dicc_Data[DATA[1]] = self.client_address[0]
                    self.wfile.write(b'SIP/2.0 200 OK\r\n\r\n')
                else:
                    self.wfile.write(b'Received request')
                    print('The client send us: ', line.decode('utf-8'))
        print('IP: ', self.client_address[0], 'Port: ', self.client_address[1])

if __name__ == "__main__":
    # Listens at localhost ('') and setting port
    # and calls the EchoHandler class to manage the request
    PORT = int(sys.argv[2])
    serv = socketserver.UDPServer(('', PORT), SIPRegisterHandler)

    print('Runnig echo server UDP...')
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        print('  Server interrupt')
