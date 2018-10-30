#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Class (and main program) for echo server in UDP simple
"""

import socketserver
import sys
import time
import json

class SIPRegisterHandler(socketserver.DatagramRequestHandler):
    """
    Echo server class
    """
    dicc_Users = {}
    def add_users(self, sip_address, expires_time):
        """
        rescribir esto
        """
        self.dicc_Users[sip_address] = self.client_address[0] + ' Expires: ' + expires_time
        self.wfile.write(b'SIP/2.0 200 OK\r\n\r\n')
        print(self.dicc_Users)

    def del_user(self, sip_address):
        """
        rescribir esto
        """
        try:
            del self.dicc_Users[sip_address]
            self.wfile.write(b'SIP/2.0 200 OK\r\n\r\n')
            print(self.dicc_Users)
        except KeyError:
            self.wfile.write(b"SIP/2.0 404 User Not Found\r\n\r\n")

    def expires(self):
        """
        rescribir esto
        """
        users_list = list(self.dicc_Users)
        for users in users_list:
            expires_time = self.dicc_Users[1]
            current_time = time.strftime('%Y-%m-%d %H:%M:%S',
            time.gmtime(time.time()))
            if expires_time < current_time:
                self.del_user(self.dicc_Users[0])
                self.register2json()

    def handle(self):
        """
        rescribir esto
        """
        received_mess = []
        for index, line in enumerate(self.rfile):
            received_mess = line.decode('utf-8')
            received_mess = ''.join(received_mess).split()
            if index == 0:
                if received_mess[0] == 'REGISTER':
                    sip_address = received_mess[1].split(':')[1]
                else:
                    self.wfile.write(b"SIP/2.0 400 Bad Request\r\n\r\n")
            elif index == 1:
                if received_mess[0] == 'Expires:':
                    expires_time = float(received_mess[1])
                    if expires_time > 0:
                        expires_time = expires_time + time.time()
                        expires_time = time.strftime('%Y-%m-%d %H:%M:%S',
                                        time.gmtime(expires_time))
                        self.add_users(sip_address, expires_time)
                        self.register2json()
                    elif expires_time == 0:
                        self.del_user(sip_address)
                        self.register2json()
                else:
                    self.wfile.write(b"SIP/2.0 400 Bad Request\r\n\r\n")

    def register2json(self):
        """
        rescribir esto
        """
        with open('registered.json', 'w') as json_file:
            json.dump(self.dicc_Users, json_file, indent=4)


if __name__ == "__main__":
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
