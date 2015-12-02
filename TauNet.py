# Copyright (C) 2015 Nathan Reed, natreed@pdx.edu.  Created in collaboration
# with Rachael Johnson arenjae.com, email: rj@arenjae.com
# Also in close collaboration with the CS300 class and Bart Massey, Professor

import server
import client
import threading
import Csaber
import userList
from os import _exit


password = b'password'
PORT = 6283
senderHeader = "from: natreed\r\n"
versionHeader = "version: 0.2\r\n"

# Main Screen, user always returns to this screen
def userInterface():
	print("**********************************************")
	print("What would you like to do?")
	print("1. Send Message")
	print("2. View Messages")
	print("3. Quit")
	print("**********************************************")
	userChoice = input(":")

	if userChoice == "1":
		target = userList.addressBook()
		message = input("Enter your message:")
		while len(message.encode('utf-8')) > 934:
			message = input("Message is too long. \nEnter message:")
		encryptedMessage = Csaber.encrypt(versionHeader + senderHeader + userList.recieverHeader + message, password)
		clientThread = threading.Thread(target=client.clientFunc, args=(target, encryptedMessage))
		clientThread.start()
	elif userChoice == "2":
		if len(server.messages) == 0:
			print("No message for you ..")
		else:
			print("Here are your messages..")
			for x in server.messages:
				print((x))
	elif userChoice == "3":
		return False
	else:
		print("That is not a valid choice...")
	return True

if __name__ == "__main__":
	# This is where the program really starts
	serverThread = server.server()
	serverThread.start()
	userList.addressBookPopulate()
	while userInterface():
		pass
	_exit(0)
