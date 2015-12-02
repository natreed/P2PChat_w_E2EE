# Copyright (C) 2015 Nathan Reed, natreed@pdx.edu.  Created in collaboration
# with Rachael Johnson arenjae.com, email: rj@arenjae.com
# Also in close collaboration with the CS300 class and Bart Massey, Professor

import server
import client
import threading
import Csaber
from os import _exit

password = str.encode('password')
PORT = 6283

addressNames = []
addressList = []
addressFile = 'addresses.txt'
senderHeader = "from: natreed\r\n"
versionHeader = "version: 0.2\r\n"


# address book
def addressBook():
	for i in range(len(addressList)):
		print(i + 1, ". ", addressNames[i])
	intTarget = int(input("Choose a person to send a message to: "))
	target = (addressList[intTarget - 1], PORT)

	global recieverHeader
	recieverHeader = "to: " + addressNames[intTarget - 1] + "\r\n\r\n"

	return target


# Adds addresses and usernames from addresses.txt to a dictionary
def addressBookPopulate():
	count = 0
	with open(addressFile, 'r') as f:
		addressBook = f.readlines()
	with open(addressFile, 'r') as f:
		for line in f:
			count += 1
	for i in range(count):
		b = addressBook[i].split()
		addressNames.append(b[0])
		addressList.append(b[1])
	addressNames.append('Test')
	addressList.append('localhost')


# Main Screen, user always returns to this screen
def MainScreen():
	print("**********************************************")
	print("What would you like to do?")
	print("1. Send Message")
	print("2. View Messages")
	print("3. Quit")
	print("**********************************************")
	userChoice = input(":")

	if userChoice == "1":
		target = addressBook()

		message = input("Enter your message:")
		while len(message.encode('utf-8')) > 94:  # restrict message to 94 bytes
			message = input("Message is too long. \nEnter message:")

		encryptedMessage = Csaber.encrypt(versionHeader + senderHeader + recieverHeader + message, password)
		clientThread = threading.Thread(target=client.clientFunc, args=(target, encryptedMessage))
		clientThread.start()

	elif userChoice == "2":
		print("Viewing messages..")
		for msg in server.messages:
			print((msg))

	elif userChoice == "3":
		return False

	else:
		print("That is not a valid choice...")

	return True


# This is where the program really starts
serverThread = server.server()
serverThread.start()
addressBookPopulate()
while MainScreen():
	pass

_exit(0)
