'''
This module determines how likely a decryption is to be the correct one by how many English words
it seems to have. It MUST have words, i.e., there must be whitespace separating words.

Just call the is_correct() function when using this module.
'''

wordlist = open("word_dictionary.txt", 'r').read().split('\n') # I'm an OED man myself

def english_score(text, wordlist):
    ''' Determine how likely a decryption is to be the correct one by how many English words
        it seems to have.

    :return: percentage of words considered english in the text
    '''

    text = text.lower()
    score = 0
    msg_len = 0

    for word in text.split():  # iterate by word, i.e. whitespace in the string
        msg_len += 1.0  # count the total number of words
        if word in wordlist:
            score += 1.0

    # For debugging:
    # print str(score) + " considered-English words out of " + str(msg_len) + " total words."
    # print str((score / msg_len) * 100) + "%"

    return (score / msg_len) * 100

def is_correct(text):
    ''' If the text has >= 30% English, return it because it's probably the correct
        decryption. Otherwise, return None.
    '''

    if english_score(text, wordlist) >= 30:
        return text
    else:
        return None


