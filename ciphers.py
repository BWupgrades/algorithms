"""
Websites used:
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
	alphabet = "abcdefghijklmnopqrstuvwxyz"
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
	alphabet = "abcdefghijklmnopqrstuvwxyz"
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

#--- USED TO TEST ---	
test = "Hello, this is a test example!"
e = txt_to_morse(test, "idek")
print(e)
d = morse_to_txt(e, "idek")
print(d)
