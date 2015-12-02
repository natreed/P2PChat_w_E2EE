# Copyright (C) 2015 Nathan Reed, natreed@pdx.edu.  Created in collaboration
# with Rachael Johnson arenjae.com, email: rj@arenjae.com
# Also in close collaboration with the CS300 class and Bart Massey, Professor

from os import urandom

password = b'password'
REPS = 20

def rc43(input, key):
    cipher = bytearray(len(input))
    i, j, state, keystream = 0, 0, list(range(256)), bytearray(list(range(len(input))))

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
        cipher[i] = ((keystream[i]) ^ input[i])
    return cipher

def encrypt(message, password):
    message = str.encode(message) #convertmessage to bytes
    iv = urandom(10)
    password += iv
    encryptedMessage = rc43(message, password)
    return iv + encryptedMessage  # concatenate iv and encrypted message

def decrypt(message, password):
	iv = message[0:10]  # grab iv from first 10 characters of message
	password += iv  # add iv to password
	message = message[10:len(message)]  # real message to decrypt is without the IV
	return rc43(message, password)  # decrypt and return decrypted message
