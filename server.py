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
    def add_users(self, sip_address, expires_time):
        self.dicc_Users[sip_address] = self.client_address[0] + ' Expires: ' + expires_time
        self.wfile.write(b'SIP/2.0 200 OK\r\n\r\n')
        print(self.dicc_Users)

    def del_user(self, sip_address):
        try:
            del self.dicc_Users[sip_address]
            self.wfile.write(b'SIP/2.0 200 OK\r\n\r\n')
            print(self.dicc_Users)
        except KeyError:
            self.wfile.write(b"SIP/2.0 404 User Not Found\r\n\r\n")

    def handle(self):
        """
        handle method of the server class
        (all requests will be handled by this method)
        """
        received_mess = []
        for line in self.rfile:
            received_mess = line.decode('utf-8')
            received_mess = ''.join(received_mess).split()
            if received_mess:
                if received_mess[0] == 'REGISTER':
                    sip_address = received_mess[1].split(':')[1]
                elif received_mess[0] == 'Expires:':
                    expires_time = float(received_mess[1])
                    if expires_time > 0:
                        expires_time = expires_time + time.time()
                        expires_time = time.strftime('%Y-%m-%d %H:%M:%S',
                                        time.gmtime(expires_time))
                        self.add_users(sip_address, expires_time)
                    elif expires_time == 0:
                        self.del_user(sip_address)



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
