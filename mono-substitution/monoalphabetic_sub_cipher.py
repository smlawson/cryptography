import argparse


def main()
	descript = ''
	file_help = ''
	key_help = ''
	rand_key = ''
	out_file = ''

	parser = argparse.ArgumentParser(description=descrip)
	parser.add_argument('-f', '--txt-file', help=file_help)
	parser.add_arguemtn('-k', '--key', help=key_help)
	parser.add_argument('-r', '--random-key', help=rand_key)
	parser.add_argument('-o', '--out-file', help=out_file)


if __name__ == '__main__':
	main()