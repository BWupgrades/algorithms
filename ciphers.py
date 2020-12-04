"""
Basic ciphers implemented with encrypt and decrypt functions.
Each function returns either the plain text or cipher text
Also has a basic functions to allow repeated call for user input.
"""

"""
Atbash Cipher
	The substitution cipher with a set key, which is the character set reversed
	Key type is a pre-set list
"""

def atbash_encrypt(txt, key=None):
	cipher_txt = ""
	for char in txt:
		ascii_val = (127 - ord(char))
		cipher_txt += chr(ascii_val)
	return cipher_txt

def atbash_decrypt(txt, key=None):
	plain_txt = ""
	for char in txt:
		ascii_val = (127 - ord(char))
		plain_txt += chr(ascii_val)
	return plain_txt

"""
Caesar Cipher
	Shifts each character over by the value of the key
	Key type is an integer
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

"""
Substitution Cipher
	Replaces each character with another set character
	Key type is a list
"""
#---------------------- NOT DONE YET ----------------------
def substitution_encrypt(txt, key):
	print(len(string.printable))


#--- USED TO TEST ---	
# test = "Hello, this is a test example! Don't forget to test :)"
# e = atbash_encrypt(test)
# d = atbash_decrypt(e)
# print(e, "\n", d)