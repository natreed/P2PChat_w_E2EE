# Copyright (C) 2015 Nathan Reed, natreed@pdx.edu.
# collaborated with Rachael Johnson arenjae.com, email: rj@arenjae.com
# Also in close collaboration with the CS300 class and Bart Massey, Prof
# An invaluable resource for this was https://pymotw.com/2/select/, https://pymotw.com/2/threading/
# https://pymotw.com/2/socket/tcp.html#easy-client-connections
# https://pymotw.com/2/socket/index.html

import socket
import Csaber
import threading
import select
import sys

messageList = []
password = b'password'

PORT = 6283
host = '0.0.0.0'

#Get our server listening on it's own thread by using the threading class
class server(threading.Thread):
	def run(self):
		self.host_pair = (host, PORT)
		print("Listening on ", host, ":", PORT)
		#print("Listening on {}:{}.".format(*self.host_pair))
		listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		listener.bind(self.host_pair)
		#listens for up to 5 simultaneous connections
		listener.listen(5)
		#Start listening, go to getMessage function
		while True:
			connection, sender = listener.accept()
			threading.Thread(target=getMessage, args=(connection,)).start()

#takes socket connection as argument. adds new messages to list of streamed messages.
def getMessage(connection):
	#Wait for notification that an input channel is ready using select() function
	readable, writable, exceptional = select.select([connection], [], [])
	message = b""
	# A "readable" server socket is ready to accept a connection
	for s in readable:
		while True:  #read in 256 bytes at a time
			temp = s.recv(256)
			if temp:
				message += temp
			else: #stream has disconnected and client is ready to be closed
				s.close()
				break;
	#If the message is empty protocol says to discard
	if len(message) == 0:
		return
	decryptedMessage = Csaber.decrypt(message, password).decode('ascii')
	print(decryptedMessage + "\n")
	messageList.append(decryptedMessage + '\n')



