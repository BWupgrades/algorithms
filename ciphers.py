"""
Websites used for research:
	- http://practicalcryptography.com/ciphers/
	- https://www.cryptogram.org/resource-area/cipher-types/
"""

"""
Basic ciphers implemented with encrypt and decrypt functions.
Each function returns either the plain text or cipher text
Also has a basic functions to allow repeated call for user input.

key = None implies cipher doen NOT require a key or the key is pre set
"""

"""
IDEAS:
	- Have V1 to only change alpha characters and V2 to change all characters
	- Create GUI to display all functions, website?
"""

#Functions and Variables used across the ciphers
alphabet = "abcdefghijklmnopqrstuvwxyz"

#Required for Hill Cipher
def matrix_multiply(a, b):
	temp_val, c = 0, []
	for x in range(3):
		for y in range(3):
			temp_val += (a[y][x] * b[y])
		c.append(temp_val)
		temp_val = 0
	return c

"""
Affine Cipher
	Uses a mathmatical calculation to create the new char value for the cipher text
	Key type is 2x +ve integers
"""
def affine_encryption(txt, key_a, key_b):
	cipher_txt = ""
	for char in txt:
		if char.isalpha():
			p = alphabet.find(char.lower())
			c = ((key_a * p) + key_b) % 26
			if char.isupper():
				cipher_txt += alphabet[c].upper()
			else:
				cipher_txt += alphabet[c].lower()
		else:
			cipher_txt += char
	return cipher_txt

def affine_decryption(txt, key_a, key_b):
	plain_txt = ""
	#Gets the inverse of key_a
	for x in range (1, 25):
		check = (key_a * x) % 26
		if check == 1:
			inv_a = x
			break
	for char in txt:
		if char.isalpha():
			c = alphabet.find(char.lower())
			p = inv_a * (c - key_b) % 26
			if char.isupper():
				plain_txt += alphabet[p].upper()
			else:
				plain_txt += alphabet[p].lower()
		else:
			plain_txt += char
	return plain_txt

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
Baconian Cipher
	The substitution cipher with a specific key, each character bounded to multple letters
	Key type is a pre set list
"""
def baconian_encrypt(txt, key=None):
	cipher_txt = ""
	baconian_key = ["aaaaa", "aaaab", "aaaba", "aaabb", "aabaa", "aabab", "aabba", "aabbb", "abaaa", "abaaa", "abaab", "ababa", "ababb", "abbaa", "abbab", "abbba", "abbbb", "baaaa", "baaab", "baaba", "baabb", "baabb", "babaa", "babab", "babba", "babbb"] #Note I/J = abaaa and U/V = baabb
	for char in txt:
		if char.isalpha():
			val = alphabet.find(char.lower())
			if char.isupper():
				cipher_txt += baconian_key[val].upper()
			else:
				cipher_txt += baconian_key[val].lower()
		else:
			cipher_txt += char
	return cipher_txt

def baconian_decrypt(txt, key=None):
	cipher_txt = ""
	baconian_key = ["aaaaa", "aaaab", "aaaba", "aaabb", "aabaa", "aabab", "aabba", "aabbb", "abaaa", "abaaa", "abaab", "ababa", "ababb", "abbaa", "abbab", "abbba", "abbbb", "baaaa", "baaab", "baaba", "baabb", "baabb", "babaa", "babab", "babba", "babbb"] #Note I/J = abaaa and U/V = baabb
	count, temp_word = 0, ""
	for char in txt:
		if char.isalpha():
			count += 1
			temp_word += char
			if count == 5:
				val = baconian_key.index(temp_word.lower())
				if temp_word[0].isupper():
					cipher_txt += alphabet[val].upper()
				else:
					cipher_txt += alphabet[val].lower()
				count, temp_word = 0, ""
		else:
			cipher_txt += char
	return cipher_txt

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
Hill Cipher
	Breaks letters into blocks of 3 and uses matrix multiplication mod 26 to get new letters
	Key type is a 3x3 matrix, 2d array of 3 lists containing 3 integers
"""

def hill_encrypt(txt, key):
	cipher_txt = ""
	char_count, temp_lst, none_alpha_dict = 0, [], {}
	while char_count < len(txt):
		char = txt[char_count]
		if char.isalpha():
			if len(temp_lst) < 3:
				val = alphabet.find(char.lower())
				temp_lst.append(val)
			else:
				c = matrix_multiply(key, temp_lst)
				for i in c:
					pos = i % 26
					cipher_txt += alphabet[pos]
				if none_alpha_dict:
					for dict_key in none_alpha_dict:
						temp_char = none_alpha_dict[dict_key]
						position, char_value = temp_char[0], temp_char[1]
						cipher_txt = cipher_txt[:position] + char_value + cipher_txt[position:]
				temp_lst, none_alpha_dict = [], {}
				char_count -= 1 #To stop it skiping the 4th char
		else:
			if none_alpha_dict:
				temp_key = sorted(none_alpha_dict.keys())[-1]
				none_alpha_dict[temp_key+1] = [char_count, char]
			else:
				none_alpha_dict[0] = [char_count, char]
		char_count += 1
	#Ensures any vals left in temp_lst are added	
	if temp_lst != []:
		items_left = len(temp_lst)
		while len(temp_lst) < 3:
			temp_lst.append(0)
		c = matrix_multiply(key, temp_lst)
		for i in range(3-items_left):
			del c[-1]
		for i in c:
			pos = i % 26
			cipher_txt += alphabet[pos]
	#Ensures any vals left in none_alpha_dict are inserted
	if none_alpha_dict:
		for dict_key in none_alpha_dict:
			temp_char = none_alpha_dict[dict_key]
			position, char_value = temp_char[0], temp_char[1]
			cipher_txt = cipher_txt[:position] + char_value + cipher_txt[position:]
	return cipher_txt

#---------------------- NOT DONE YET ----------------------
def hill_decrypt(txt, key):
	pass

"""
Key Phrase Cipher
	A 26 letter key is used to replace plain text with the key letter assigned to the alphabet
	Key type is a 26 character string
"""
def key_phrase_encrypt(txt, key):
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
Morse Code
	Uses dots and dashes to determine each letter
	The key is a pre defined dict of morse code values
	Note: / is used to seperate the words for the user
"""
def txt_to_morse(txt, key=None):
	morse_txt = ""
	key = {
		"a": ".-", "b": "-...", "c": "-.-.",
		"d": "-..", "e": ".", "f": "..-.",
		"g": "--.", "h": "....", "i": "..",
		"j": ".---", "k": "-.-", "l": ".-..",
		"m": "--", "n": "-.", "o": "---",
		"p": ".--.", "q": "--.-", "r": ".-.",
		"s": "...", "t": "-", "u": "..-",
		"v": "...-", "w": ".--", "x": "-..-",
		"y": "-.-", "z": "--.."
	}
	for char in txt:
		if char.isalpha():
			morse_txt += (key[char.lower()] + " ")
		else:
			if char == " ":
				char = "  /  "
			morse_txt += char
	return morse_txt

def morse_to_txt(txt, key=None):
	plain_txt = ""
	key = {
		".-": "a", "-...": "b", "-.-.": "c",
		"-..": "d", ".": "e", "..-.": "f",
		"--.": "g", "....": "h", "..": "i",
		".---": "j", "-.-": "k", ".-..": "l",
		"--": "m", "-.": "n", "---": "o",
		".--.": "p", "--.-": "q", ".-.": "r",
		"...": "s", "-": "t", "..-": "u",
		"...-": "v", ".--": "w", "-..-": "x",
		"-.-": "y", "--..": "z"
	}
	temp_code = ""
	for char in txt:
		if (char == "." or char == "-") and len(temp_code) < 4:
			temp_code += char
		elif char == " " and temp_code != "":
			plain_txt += key[temp_code]
			temp_code = ""
		elif char == "/":
			plain_txt += " "
		else:
			plain_txt += char
	#Just to remove extra large spaces and make it look better
	nice_text, first_space = "", True
	for char in plain_txt:
		if char != " ":
			first_space = True
			nice_text += char
		elif first_space:
			nice_text += " "
			first_space = False
	return nice_text

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

def substitution_decrypt(txt, key):
	pass

#--- USED TO TEST ---	
test = "Hello, this is a test example!"
e = affine_encryption(test, 15, 11)
print(e)
d = affine_decryption(e, 15, 11)
print(d)
