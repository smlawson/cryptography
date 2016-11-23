alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def encrypt(x):
    i = 0
    while i < len(x):
        if x[i] != ' ':
            a = 0
            while ord(alphabet[a]) != ord(x[i]):
                a += 1
            x[i] = chr(((ord(alphabet[a]) - 65 + s) % 26) + 65)
        i += 1
    return x

def decrypt(x):
    i = 0
    while i < len(x):
        if x[i] != ' ':
            a = 0
            while ord(alphabet[a]) != ord(x[i]):
                a += 1
            x[i] = chr(((ord(alphabet[a]) - 65 - s) % 26) + 65)
        i += 1
    return x

#User begins by choosing encrytion or decrytion
choice = input("Enter (1) to encrypt a message or (2) to decrypt a message: ")

while choice != 1 and choice != 2:
    choice = input("Enter (1) to encrypt a message or (2) to decrypt a message: ")

if choice == 1:
    
    #plaintext encryption
    plaintext = raw_input("Enter plaintext message (letters and spaces only): ")
    plaintext = plaintext.upper()
    p = list(plaintext)

    s = input("Enter shift parameter: ")

    encrypt(p)
    ciphertext = ''.join(p)
    print ciphertext

if choice == 2:

    #ciphertext decryption
    
    ciphertext = raw_input("Enter ciphertext message: ")
    ciphertext = ciphertext.upper()
    c = list(ciphertext)

    #is the key known?
    known_key = raw_input("Do you know the shift parameter? Enter Yes or No: ")

    while known_key != "Yes" and known_key != "yes" and known_key != "Y" and known_key != "y" and known_key != "No" and known_key != "no" and known_key != "N" and known_key != "n":
        known_key = raw_input("Do you know the shift parameter? Enter Yes or No: ")
        
    #if the key is already known
    if known_key == "Yes" or known_key == "yes" or known_key == "Y" or known_key == "y":
        
        s = input("Enter shift parameter: ")

        decrypt(c)
        plaintext = ''.join(c)
        print plaintext

    #if the key is not known, we can try brute force
    else:
        
        s = 0
        while s < 26:
            decrypt(c)
            plaintext = ''.join(c)
            print plaintext
            encrypt(c)
            s += 1
