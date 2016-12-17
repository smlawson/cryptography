import argparse

def validate_key(key):
	'''
		In the case that a key was specified by the user (i.e., not a randomly
		generated one by this program), check to see if the key is a valid key
		for a monoalphabetic substitution cipher.
	'''
	pass

def generate_key():
	'''
		Return a key to encrypt with, generated (psuedo)randomly.
	'''
	pass

# Obviously other functions will have to be created


def encrypt(plaintext, key):
	pass

def decrypt(ciphertext):

def main()
	descript = ''
	file_help = ''
	string_help = ''
	key_help = ''
	rand_key = ''
	out_file = ''

	parser = argparse.ArgumentParser(description=descrip)
	parser
	parser.add_argument('-f', '--txt-file', help=file_help)
	parser.add_argument('-s', '--string', help=string_help)
	parser.add_arguemtn('-k', '--key', help=key_help)
	parser.add_argument('-r', '--random-key', help=rand_key)
	parser.add_argument('-o', '--out-file', help=out_file)

	args = parser.parse_args()

	'''
		Example inputs:

		Passing in a file to decrypt with a specified key:
			python mono.py -e -f <ciphertext.txt> -k 'bcdefjhijklmnopqrstuvwxyza' -o <plaintext.txt>

		Passing in a string to encrypt with a random key:
			python mono.py -d -s 'Encrypt me, please.' -r -o <ciphertext.txt>

		If no output file is specified with '-o', print the ciphertext to STDOUT.
	'''

	file_name = ''
	plaintext = ''
	key = ''

	# Flags for whether we are encrypting or decrypting
	encrypt = False
	decrypt = False

	if args.txt_file is not None:
		# An input text file was passed in as the text to encrypt
		print('Got file:', args.txt_file)
		file_name = args.txt_file
	elif args.string is not None:
		# A string was passed in as the text to encrypt
		print('Got string:', args.string)
		plaintext = args.string
	elif args.key is not None:
		# A key was specified by the user to encrypt with



if __name__ == '__main__':
	main()