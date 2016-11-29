import timeit
import verifyer
import string


alphabet = string.printable

def encrypt(x):
    i = 0
    while i < len(x):
        if x[i] != ' ' and x[i] not in string.punctuation:
            a = 0
            while ord(alphabet[a]) != ord(x[i]):
                a += 1
            x[i] = chr(((ord(alphabet[a]) - 65 + s) % 26) + 65)
        i += 1
    return x

def decrypt(x):
    i = 0
    while i < len(x):
        if x[i] != ' ' and x[i] not in string.punctuation:
            a = 0
            while ord(alphabet[a]) != ord(x[i]):
                a += 1
            x[i] = chr(((ord(alphabet[a]) - 65 - s) % 26) + 65)
        i += 1
    return x

choice = input("Enter (1) to encrypt a message or (2) to decrypt a message: ")

while choice != 1 and choice != 2:
    choice = input("Enter (1) to encrypt a message or (2) to decrypt a message: ")

if choice == 1:
    plaintext = raw_input("Enter plaintext message (letters and spaces only): ")
    plaintext = plaintext.upper()
    p = list(plaintext)

    s = input("Enter shift parameter: ")

    start_time = timeit.default_timer()
    encrypt(p)
    ciphertext = ''.join(p)
    elapsed = timeit.default_timer() - start_time
    print ciphertext
    print("Encrypted message in %.10f seconds." % elapsed)

if choice == 2:
    ciphertext = raw_input("Enter ciphertext message: ")
    ciphertext = ciphertext.upper()
    c = list(ciphertext)

    known_key = raw_input("Do you know the shift parameter? Enter (Y)es or (N)o: ")

    while (known_key != "Yes"
        and known_key != "yes"
        and known_key != "Y"
        and known_key != "y"
        and known_key != "No"
        and known_key != "no"
        and known_key != "N"
        and known_key != "n"):
        known_key = raw_input("Do you know the shift parameter? Enter Yes or No: ")

    if (known_key == "Yes" or known_key == "yes" or known_key == "Y" or known_key == "y"):

        s = input("Enter shift parameter: ")

        start_time = timeit.default_timer()
        decrypt(c)
        plaintext = ''.join(c)
        print plaintext

        elapsed = timeit.default_timer() - start_time
        print("Decrypted with known key in %.10f seconds." % elapsed)

    else:
        s = 1
        print ""

        start_time = timeit.default_timer()
        while s < 26:
            decrypt(c)
            plaintext = ''.join(c)
            if verifyer.is_correct(plaintext) is not None:
                print plaintext
            encrypt(c)
            s += 1

        elapsed = timeit.default_timer() - start_time
        print("\nDecrypted by brute force method in %.10f seconds." % elapsed)