import argparse


def validate_key(key):
	'''
		In the case that a key was specified by the user (i.e., not a randomly
		generated one by this program), check to see if the key is a valid key
		for a monoalphabetic substitution cipher.
	'''
	return True

def generate_key():
	'''
		If the user did not specify a key to encrypt with, generate one
		randomly and return the key.
	'''
	pass

# Draw the rest of the fucking owl

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

def main():
	'''
		Main program execution, including the command-line interface and parsing
		of the command-line arguments so program flow can be determined.
	'''

	descrip = 'A monoalphabetic substitution encrypter/decrypter. It is capable ' \
			  'of encrypting with your key of choice or a with a key generated ' \
			  'randomly by this program. It can read in a file or a string passed ' \
			  'into the command line. If no output file is specified, the decryption' \
			  'will be printed to STDOUT.'
	encrypt_help = 'This flag specifies that the input will be encrypted.'
	decrypt_help = 'This flag specifies that the output will be decrypted.'
	file_help = 'The .txt file to be used as input.'
	string_help = 'The string to be used as input.'
	key_help = 'The key (as a string).'
	rand_key = 'This flag specifies that the program must generate a random key.'
	out_file = 'The output decryption file.'

	parser = argparse.ArgumentParser(description=descrip)

	group_action = parser.add_mutually_exclusive_group(required=True)
	group_action.add_argument('-e', '--encrypt', action='store_true', help=encrypt_help)
	group_action.add_argument('-d', '--decrypt', action='store_true', help=decrypt_help)

	group_input = parser.add_mutually_exclusive_group(required=True)
	group_input.add_argument('-f', '--txt-file', help=file_help)
	group_input.add_argument('-s', '--string', help=string_help)

	group_key = parser.add_mutually_exclusive_group(required=True)
	group_key.add_argument('-k', '--key', help=key_help)
	group_key.add_argument('-r', '--random-key', action='store_true', help=rand_key)

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

	# Flag for whether an output file was specified or not
	output_specified = False

	# Figure out whether we are encryption or decrypting
	if args.encrypt == True:
		encrypt = True
		print('Encryption mode.')
	else:
		decrypt = True
		print('Decryption mode.')

	if args.txt_file is not None:
		# An input text file was passed in as the text to encrypt
		file_name = args.txt_file
		print('Input file:', file_name)

	if args.string is not None:
		# A string was passed in as the text to encrypt
		plaintext = args.string
		print('Input string:', plaintext)

	if args.out_file is not None:
		# An output file name was specified
		out_file_name = args.out_file
		output_specified = True
		print('Output file:', out_file_name)

	# Figure out if a key is specified or if a random key will have to be generated
	if args.key is not None:
		# A key was specified by the user to encrypt with
		if validate_key(args.key) == True:
			key = args.key
			print("Key:", key)
		else:
			# An invalid key was passed in by the user, die gracefully w/ error message
			# Implement this -- figure out how to stop execution
			pass

	if args.key is None:
		# Generate a random key
		print("Generating a random key...")
		key = generate_key


if __name__ == '__main__':
	main()