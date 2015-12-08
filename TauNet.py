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


def userMenu():
    print("**********************************************")
    print("What would you like to do?")
    print("1. Send Message")
    print("2. View Messages")
    print("3. Quit")
    print("**********************************************\n")
    choice = input(":   ")
    return choice

def sendMsg(target):
	#l = len(server.messageList)
	message = input(": ")
	#Exit the function with a carriage return
	if message == "":
		return False
    #check message length to make sure it is in bounds
	while len(message.encode('utf-8')) > 934:
		message = input("Message is too long. \nEnter message:")
    #extract encrypted message using encrypt function
	encryptedMessage = Csaber.encrypt(versionHeader + senderHeader + userList.recieverHeader + message, password)
    #to send create separate thread for sending message and start it.
	clientThread = threading.Thread(target=client.clientFunc, args=(target, encryptedMessage))
	clientThread.start()
	return True

# Main Screen provides a simple user interface along with a response handlero
def userInterface():

	responseHandler = userMenu()

	#Handler for sending message.
	if responseHandler == "1":
        #addressbook allows user to choose ip address to send a message to
		target = userList.addressBook(PORT)

		print("Enter your message")
		#Start a Dialogue with someone bypassing the menu to exit just hit enter
		print("Hit enter AT ANY TIME to return to main menu.")

		while True:
			if sendMsg(target):
				continue
			else:
				break

    #Handler for checking messages. Check messages list.
	elif responseHandler == "2":
		if len(server.messageList) == 0:
			print("No messages .. ")
		else:
			print("\nHere are your messages..")
			for x in server.messageList:
				print((x))

    #If user wants to quit, stop looping.
	elif responseHandler == "3":
		return False
	else:
		print("That is not a valid choice...")
	return True


# Main Function starts server and loops on userInterface
if __name__ == "__main__":
	#Read in names and IP addresses from address list.
	userList.addressBookPopulate()
    #Start the server on it's own thread and get it listeninig.
	serverThread = server.server()
	serverThread.start()
    #loop on user interface.
	while userInterface():
		pass
	_exit(0)
