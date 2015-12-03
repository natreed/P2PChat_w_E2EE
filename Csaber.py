# Copyright (C) 2015 Nathan Reed, natreed@pdx.edu.
# Collaborated with Rachael Johnson arenjae.com, email: rj@arenjae.com
# Also in close collaboration with the CS300 class and Bart Massey, Professor

from os import urandom

password = b'password'
REPS = 20

#rc4 encryption takes a stream of bytes and a key and returns an encrypted stream of
#bytes using the key for encryption
def rc4(input, key):
    cipher = bytearray(len(input))
    i, j, state, keystream = 0, 0, list(range(256)), bytearray(list(range(len(input))))

    #run key scheduling for designated number of rounds. randomize the state list using key
    for r in range(REPS):
        for i in range(256):
            j = (j + state[i] + key[i % len(key)]) % 256
            state[i], state[j] = state[j], state[i]
    j = 0
    for i in range(0, len(input)):
        x = (i + 1) % 256
        j = (j + state[x]) % 256
        state[x], state[j] = state[j], state[x]
        keystream[i] = state[(state[x] + state[j]) % 256]
        #create the cipher using xor
        cipher[i] = ((keystream[i]) ^ input[i])
    return cipher

#encrypt takes a string as a message and a password in bytes and returns and encrypted stream
#of bytes which is the message concatenated with the iv of 10 random bytes
def encrypt(message, password):
    message = str.encode(message) #convertmessage to bytes
    iv = urandom(10)
    password += iv
    encryptedMessage = rc4(message, password)
    return iv + encryptedMessage  # concatenate iv and encrypted message


def decrypt(message, password):
	iv = message[0:10]  # grab iv from first 10 characters of message
	password += iv  # add iv to password
	message = message[10:len(message)]  # real message to decrypt is without the IV
	return rc4(message, password)  # decrypt and return decrypted message

#main is used for testing.  I used used test files from Bart's CipherSaber2 repo
#this works byt the way
if __name__ == "__main__":
    password = b'asdfg'
    REPS = 10
    infile = open("testfile.txt", 'br')
    #outfile = open("outfile.txt", 'br')
    message = infile.read()
    #message = b'ksjhlkjhgsa'

    print(message)
    decryptedText = decrypt(message, password)
    print(decryptedText)
    encryptedText = encrypt(message, password)