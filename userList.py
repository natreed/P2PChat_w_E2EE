# Copyright (C) 2015 Nathan Reed, natreed@pdx.edu.
# Collaborated with Rachael Johnson arenjae.com, email: rj@arenjae.com
# Also in close collaboration with the CS300 class and Bart Massey, Professor



#A list of names and a list of addresses
#the index of the name corresponds that users address in
#the address list.
addressNames = []
addressList = []
addressFile = 'addresses.txt'

# address book takes a port as an argument
# returns a target ip and port
def addressBook(port):
	#print a list of names and addresses to choose from
	for i in range(len(addressList)):
		print(i + 1, ". ", addressNames[i])
	#create a target tuple with ip address and port to connect to
	intTarget = int(input("Choose a person to send a message to: \n\n"))
	target = (addressList[intTarget - 1], port)
	#Get the name using the same index, from the names list and create the receiver
	#header variable
	global recieverHeader
	#two new lines as specified in requirements specification
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
	addressNames.append('Test\n')
	addressList.append('localhost')

