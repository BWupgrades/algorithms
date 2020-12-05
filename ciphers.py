"""
Websites used:
	- 
"""


"""
Basic ciphers implemented with encrypt and decrypt functions.
Each function returns either the plain text or cipher text
Also has a basic functions to allow repeated call for user input.

key = None implies cipher doen NOT require a key or the key is pre set
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
Key Phrase Cipher
	A 26 letter key is used to replace plain text with the key letter assigned to the alphabet
	Key type is a 26 character string
"""
def key_phrase_encrypt(txt, key):
	alphabet = "abcdefghijklmnopqrstuvwxyz"
	cipher_txt = ""
	for char in txt:
		if char.isalpha():
			val = alphabet.find(char.lower())
			if char.isupper():
				cipher_txt += key[val].upper()
			else:
				cipher_txt += key[val].lower()
		else:
			cipher_txt += char
	return cipher_txt 

#---------------------- NOT DONE YET ----------------------
def key_phrase_decrypt(txt, key):
	pass
	#going to have to use stats to decrypt since not one-one
"""
Rail-Fence Cipher
	Writes each letter in a zig-zag (based on key val) then merges lines top to bottom
	Key type is an integer
"""
def rail_fence_encrypt(txt, key):
	pass_val = 0
	temp_dict = {}
	cipher_txt = ""
	#Creates a dictonary with number of lines started from they key
	for i in range(key):
		temp_dict[i] = ""
	i, diag_down = 0, True
	#Updates the value of each line with a char on that line
	for char in txt:
		temp_dict[i] += char
		if diag_down:
			i += 1
		else:
			i -= 1
		if i == 0 or i == (key - 1):
			diag_down = not diag_down
	#Puts all char's together to create the cipher text
	for dict_key in temp_dict:
		cipher_txt += temp_dict[dict_key]
	return cipher_txt

#---------------------- NOT DONE YET ----------------------
def rail_fence_decrypt(txt, key):
	pass

"""
ROT13 Cipher
	The ceaser cipher with a key set to 13
	Key type is an pre-set integer
"""
def rot13_encrypt(txt, key=None):
	cipher_txt = ""
	for char in txt:
		ascii_val = (ord(char) - 32 + 13) % 94 + 32
		cipher_txt += chr(ascii_val)
	return cipher_txt

def rot13_decrypt(txt, key=None):
	plain_txt = ""
	for char in txt:
		ascii_val = (ord(char) - 32 - 13) % 94 + 32
		plain_txt += chr(ascii_val)
	return plain_txt
	

"""
Substitution Cipher
	Replaces each character with another set character
	Key type is a list
"""
#---------------------- NOT DONE YET ----------------------
def substitution_encrypt(txt, key):
	pass


#--- USED TO TEST ---	
test = "Hello, this is a test example!"
e = key_phrase_encrypt(test, "onetwothreefourfivesixseve")
d = key_phrase_decrypt(e, "onetwothreefourfivesixseve")
print(e, "\n", d)