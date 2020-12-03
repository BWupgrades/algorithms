"""
Basic ciphers implemented with encrypt and decrypt functions.
Each function returns either the plain text or cipher text
Also has a basic functions to allow repeated call for user input.
"""

import string

#Allows the user to input a string and a key
def user_input():
	txt, key, cipher_type = "", "", ""
	while txt == "":
		txt = input("Please enter text for the cipher: ")
	while key == "": 
		key = input("Please enter a key for the chipher: ")
	while cipher_type not in ["e", "d"]:
		cipher_type = input("Would you like to encrypt or decrypt? [e/d]").lower()
	return txt, key, cipher_type
"""
Caesar Cipher
	Shifts each character over by the value of the key
"""

def caesar_encrypt(txt, key):
	cipher_txt = ""
	for char in txt:
		ascii_val = (ord(char) - 32 + key) % 94 + 32
		cipher_txt += chr(ascii_val)
	return cipher_txt

def caesar_decrypt(txt, key):
	plain_txt = ""
	for char in txt:
		ascii_val = (ord(char) - 32 - key) % 94 + 32
		plain_txt += chr(ascii_val)
	return plain_txt

#Main program

txt, key, cipher_type = user_input()

try:
	key = int(key)
	if cipher_type == "e":
		print("\n--------------------------------------------------------")
		print("Caesar encrypt:", caesar_encrypt(txt, key))

	else:
		print("\n--------------------------------------------------------")
		print("Caesar decrypt:", caesar_decrypt(txt, key))

except:
	if cipher_type == "e":
		print("\n--------------------------------------------------------")
		
	else:
		print("\n--------------------------------------------------------")
		