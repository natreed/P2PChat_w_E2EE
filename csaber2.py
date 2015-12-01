# Copyright (C) 2015 Nathan Reed, natreed@pdx.edu.  Created in collaboration
# with Rachael Johnson arenjae.com, email: rj@arenjae.com
# Also in close collaboration with the CS300 class and Bart Massey, Professor

from os import urandom

password = str.encode('password')
REPS = 20


def swap(l, a, b):
	"""Swap entries a and b in list l."""
	temp = l[a]
	l[a] = l[b]
	l[b] = temp


def rc4(message, password):
	i = 0
	state = list(range(256))
	key = list(range(256))
	cipher = b""
	for a in range(REPS):
		while i < 256:
			ctemp = password[i % len(password):(i % len(password)) + 1]
			key[i] = ord(ctemp)
			state[i] = i
			i += 1
	i = j = 0
	while i < 256:
		j = (j + state[i] + key[i]) % 256
		swap(state, i, j)
		i += 1
	a = 1
	while a <= len(message):
		i = (i + 1) % 256
		j = (j + state[i]) % 256
		swap(state, i, j)
		k = state[(state[i] + state[j]) % 256]
		ctemp = message[a - 1:a]
		itemp = ord(ctemp)
		cipherbyte = itemp ^ k
		cipherbyte = bytes([cipherbyte])  # change to byte
		cipher += cipherbyte
		a += 1
	return cipher


def encrypt(message, password):
	iv = urandom(10)
	password += iv
	encryptedMessage = rc4(message, password)
	return iv + encryptedMessage  # concatenate iv and encrypted message


def decrypt(message, password):
	iv = message[0:10]  # grab iv from first 10 characters of message
	password += iv  # add iv to password
	message = message[10:message.__len__()]  # real message to decrypt is without the IV
	return rc4(message, password)  # decrypt and return decrypted message