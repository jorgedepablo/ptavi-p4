#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Class (and main program) for echo server in UDP simple
"""

import socketserver
import sys
import time

class SIPRegisterHandler(socketserver.DatagramRequestHandler):
    """
    Echo server class
    """
    dicc_Users = {}
    def handle(self):
        """
        handle method of the server class
        (all requests will be handled by this method)
        """
        received_mess = []
        for line in self.rfile:
            received_mess = line.decode('utf-8')
            #received_mess.append(line.decode('utf-8'))
            received_mess = ''.join(received_mess).split()

            if received_mess:
                #print(received_mess)
                if received_mess[0] == 'REGISTER':
                    print(received_mess)
                    sip_address = received_mess[1].split(':')[1]
                    expires_time = received_mess
                    self.dicc_Users[sip_address] = self.client_address[0]
                    self.wfile.write(b'SIP/2.0 200 OK\r\n\r\n')


if __name__ == "__main__":
    # Listens at localhost ('') and setting port
    # and calls the EchoHandler class to manage the request
    try:
        PORT = int(sys.argv[2])
        serv = socketserver.UDPServer(('', PORT), SIPRegisterHandler)
    except IndexError or ValueError:
        sys.exit('Usage: python3 server.py "port"')

    print('Runnig echo server UDP...')
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        print('  Server interrupt')
