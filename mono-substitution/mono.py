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
		If the user did not specify a key to encrypt with, generate one
		randomly and return the key.
	'''
	pass

# Obviously other functions will have to be created

def encrypt(plaintext, key):
	'''
		Given the plaintext, return the ciphertext as encrypted
		with the key 'key'.
	'''
	pass

def decrypt(ciphertext):
	'''
		Given the ciphertext, return the plaintext.
	'''
	pass

def main()
	descript = ''
	encrypt_help = ''
	decrypt_help = ''
	file_help = ''
	string_help = ''
	key_help = ''
	rand_key = ''
	out_file = ''

	parser = argparse.ArgumentParser(description=descrip)
	parser.add_argument('-e', '--encrypt', help=encrypt_help)
	parser.add_argument('-d', '--decrypt', help=decrypt_help)
	parser.add_argument('-f', '--txt-file', help=file_help)
	parser.add_argument('-s', '--string', help=string_help)
	parser.add_arguemtn('-k', '--key', help=key_help)
	parser.add_argument('-r', '--random-key', help=rand_key)
	parser.add_argument('-o', '--out-file', help=out_file)

	args = parser.parse_args()

	'''
		Example inputs:

		   1. Passing in a file to decrypt with a specified key:

				$ python mono.py -e -f <ciphertext.txt> -k 'bcdefjhijklmnopqrstuvwxyza' -o <plaintext.txt>

		   2. Passing in a string to encrypt with a random key:

				$ python mono.py -d -s 'Encrypt me, please.' -r -o <ciphertext.txt>

		If no output file is specified with '-o', print the cipher/plaintext to STDOUT.
	'''

	file_name = ''
	out_file_name = ''
	plaintext = ''
	key = ''

	# Flags for whether we are encrypting or decrypting
	encrypt = False
	decrypt = False

	if args.txt_file is not None:
		# An input text file was passed in as the text to encrypt
		print('Got file:', args.txt_file)
		file_name = args.txt_file
	if args.out_file is not None:
		# An output file name was specified
		print('Got out file:', args.out_file)
		out_file_name = args.out_file
	elif args.string is not None:
		# A string was passed in as the text to encrypt
		print('Got string:', args.string)
		plaintext = args.string
	elif args.key is not None:
		# A key was specified by the user to encrypt with
		if validate_key(args.key) == True:
			key = args.key
		else:
			# An invalid key was passed in by the user, die gracefully w/ error message
	elif args.key is None:
		# Generate a random key
		key = generate_key




if __name__ == '__main__':
	main()