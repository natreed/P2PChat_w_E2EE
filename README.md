TauNet
=============
####Private and encrypted communication network of Raspberry Pi2's

Send and receive encrypted messages over a private network via the internet.

####Build and Execution Instructions

- This program is written in python 3. It will work when run with any version of python 3.3 to 3.5.
- To run the program all files will need to be in the same location. To execute on the command line enter $ python3 TauNet.py


####For The Encryption
- Cipher Saber 2
- RC4 <- algorithm to output a stream of random numbers (run key scheduler 20 times after each message received / and transmitted)
- RC4 key will be used by everyone in the network
- IV thing (10 randomly chosen bytes that are appended to the password)
- Address Book of names and corresponding IP Addresses



####Notes
- Socket python package used for sockets
    - search for python socket example

- Used threading for concurrent sending and receiving operations

#####Basic Code Outline:
- Need an encrypt / decrypt function.
    - Functions will decrypt a message or encrypt a message using protocol specified by Bart
    
- Listen() function for a specific port - any message sent to that port will be received, decrypted, and then displayed to the user
- Send function (EncryptedStringToSend, AddressToSendTo)
    - Function will send an inputted string to an address 
    - select statement a readable - to check for a closed port
        
- Address Book -should read in a text file and convert to two lists - one with user names, and the other with user addresses
    - Text file should have one line per user / address
    - username should come first, followed by a space, followed by a address


#####Advance Code Outline:
 - Csaber.py 
 - server.py
 - client.py
 - addressBook.py
 - TauNet.py
    - Main handler for everything. This has a while loop that will keep looping until user decides to quit program
	1. View messages
	2. Send messages
	3. quit
