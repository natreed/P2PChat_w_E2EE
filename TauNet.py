# Copyright (C) 2015 Nathan Reed, natreed@pdx.edu.
# Collaborated with Rachael Johnson arenjae.com, email: rj@arenjae.com
# Also in close collaboration with the CS300 class and Bart Massey, Professor



#TauNet is the File that is actually Run at the command line.
#It contains the primary user interface as well as main which runs the program.
#It also contains links to all other program segments. Also manages the program
#with user control from the command line.
import server
import client
import threading
import Csaber
import userList
from os import _exit

#These are the variables.  For simplicity they are declared globally.
password = b'password'  #the key for the ciphersaber 2 encryption
PORT = 6283 #agreed upon port to listen on
#header is in format specified in protocol.  recieverHeader is specified in the
#userList file in the addressBook function
senderHeader = "from: natreed\r\n"
versionHeader = "version: 0.2\r\n"

# Main Screen provides a simple user interface along with a response handler
def userInterface():
	print("**********************************************")
	print("What would you like to do?")
	print("1. Send Message")
	print("2. View Messages")
	print("3. Quit")
	print("**********************************************")
	print()

	responseHandler = input(":   ")

	#Handler for sending message.
	if responseHandler == "1":
        #addressbook allows user to choose ip address to send a message to
		target = userList.addressBook(PORT)
		message = input("Enter your message:")
        #check message length to make sure it is in bounds
		while len(message.encode('utf-8')) > 934:
			message = input("Message is too long. \nEnter message:")
        #extract encrypted message using encrypt function
		encryptedMessage = Csaber.encrypt(versionHeader + senderHeader + userList.recieverHeader + message, password)
        #to send create separate thread for sending message and start it.
		clientThread = threading.Thread(target=client.clientFunc, args=(target, encryptedMessage))
		clientThread.start()
    #Handler for checking messages. Check messages list.
	elif responseHandler == "2":
		if len(server.messageList) == 0:
			print("No message for you ..")
		else:
			print("Here are your messages..")
			for x in server.messageList:
				print((x))
    #If user wants to quit, stop looping.
	elif responseHandler == "3":
		return False
	else:
		print("That is not a valid choice...")
	return True

# This is where the program really starts
if __name__ == "__main__":
    #Start the server on it's own thread and get it listeninig.
	serverThread = server.server()
	serverThread.start()
    #Read in names and IP addresses from address list.
	userList.addressBookPopulate()
    #loop on user interface.
	while userInterface():
		pass
	_exit(0)
