TauNet
=============
####Private and encrypted communication network of Raspberry Pi2's

Send and receive encrypted messages over a private network via the internet.

####Build and Execution Instructions

- This program is written in python 3. It will work when run with any version of python 3.3 to 3.5.
- To run the program all files will need to be in the same location. To execute on the command line enter $ python3 TauNet.py
- The main menu gives the options of either sending or recieving messages.  
- When sending a message you will remain connected on that socket until you hit the carriage return.  This will take you back to the main menu.
- Messages recieved will show up in real-time.  If you are talking to one person and you receive a message from someone else or want to leave the 
- conversation for any other reason.  Simply hit return.
- To switch conversations you must then choose the 'send message' option and send a message to the other person you would like to talk to. 
- To quit hit the carriage return to exit the conversation and select 'quit' (option 3).

####For The Encryption
- Cipher Saber 2
- RC4 <- algorithm to output a stream of random numbers (run key scheduler 20 times after each message received / and transmitted)
- RC4 key will be used by everyone in the network
- IV thing (10 randomly chosen bytes that are appended to the password)
- Address Book of names and corresponding IP Addresses


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

- Used threading for concurrent sending and receiving operations
- Used python threading for concurrent sending and receiving operation

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
