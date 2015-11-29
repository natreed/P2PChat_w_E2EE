
# Copyright (C) 2015 Nathan Reed, natreed@pdx.edu.  Created in collaboration
# with Rachael Johnson arenjae.com, email: rj@arenjae.com
# Also in close collaboration with the CS300 class and Bart Massey, Professor


import socket
import Csaber
import threading
import select

messages = []
password = str.encode('password')

PORT = 6283
host = '0.0.0.0'

class server(threading.Thread):
	def run(self):

		print("Server Started...")
		self.host_pair = (host, PORT)

		print("Listening on {}:{}.".format(*self.host_pair))
		conn = None
		listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		listener.bind(self.host_pair)
		listener.listen(10)

		while True:
			conn, sender = listener.accept()
			threading.Thread(target=getMessage, args=(conn,)).start()


def getMessage(conn):
	readable, writable, exceptional = select.select([conn], [], [])
	buffer = b""
	for s in readable:
		while True:
			temp = s.recv(256)
			if temp:
				buffer += temp
			else:
				s.close()
				break;
	messages.append(Csaber.decrypt(buffer, password).decode('ascii') + '\n')
