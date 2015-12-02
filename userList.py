# Copyright (C) 2015 Nathan Reed, natreed@pdx.edu.  Created in collaboration
# with Rachael Johnson arenjae.com, email: rj@arenjae.com
# Also in close collaboration with the CS300 class and Bart Massey, Professor

#PORT = 6283
addressNames = []
addressList = []
addressFile = 'addresses.txt'

# address book
def addressBook(port):
	for i in range(len(addressList)):
		print(i + 1, ". ", addressNames[i])
	intTarget = int(input("Choose a person to send a message to: "))
	target = (addressList[intTarget - 1], port)
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

