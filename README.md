# TauNet
=============
For detailed documentation look here:  https://github.com/natreed/P2PChat_w_E2EE/tree/master/documentation

Private and encrypted communication network of Raspberry Pi2's

Send and receive encrypted messages over a private network via the internet.

### Build and Execution Instructions

- This program is written in python 3. It will work when run with any version of python 3.3 to 3.7.
- Open Linux terminal and clone the repository: 'git clone https://github.com/natreed/P2PChat_w_E2EE'	
- To run:  '$ python3 TauNet.py'
- The main menu gives the options of either sending or recieving messages.  
- When sending a message you will remain connected on that socket until you hit the carriage return.  This will take you back to the main menu.
- Messages recieved will show up in real-time.  If you are talking to one person and you receive a message from someone else or want to leave the conversation for any other reason.  Simply hit return.
- To switch conversations, choose the 'send message' option and send a message to the other person you would like to talk to. 
- To quit hit the carriage return to exit the conversation and select 'quit' (option 3).

### Encryption
- Cipher Saber 2
- RC4 <- algorithm to output a stream of random numbers (run key scheduler 20 times after each message received / and transmitted)
- RC4 key will be used by everyone in the network
- IV thing (10 randomly chosen bytes that are appended to the password)
- Address Book of names and corresponding IP Addresses


### Basic Code Outline:
- Listen() function for a specific port - any message sent to that port will be received, decrypted, and then displayed to the user
- Send function (EncryptedStringToSend, AddressToSendTo)
    - Function will send an inputted string to an address 
    - select statement a readable - to check for a closed port
        
- ***Address Book*** - read in a text file and convert to two lists - one with user names, and the other with user addresses
    - Text file should have one line per user / address
    - Username should come first, followed by a space, followed by a address

- Used threading for concurrent sending and receiving operations.

### High Level Code Outline:
 - Csaber.py 
 - server.py
 - client.py
 - addressBook.py
 - TauNet.py
    - Main handler for everything. This has a while loop that will keep looping until user decides to quit program
	1. View messages
	2. Send messages
	3. quit
