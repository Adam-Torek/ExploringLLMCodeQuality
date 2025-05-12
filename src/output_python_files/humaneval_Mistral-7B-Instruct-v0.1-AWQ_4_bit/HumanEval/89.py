def encrypt(s):
    """Create a function encrypt that takes a string as an argument and
    returns a string encrypted with the alphabet being rotated. 
    The alphabet should be rotated in a manner such that the letters 
    shift down by two multiplied to two places.
    For example:
    encrypt('hi') returns 'lm'
    encrypt('asdfghjkl') returns 'ewhjklnop'
    encrypt('gf') returns 'kj'
    encrypt('et') returns 'ix'
    """
    # create a list of the alphabet
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    # create a list of the encrypted alphabet
    encrypted_alphabet = alphabet[2:] + alphabet[:2]
    # create a list of the original string
    original_string = s.lower()
    # create a list of the encrypted string
    encrypted_string = ''
    # iterate through each letter in the original string
    for letter in original_string:
        # check if the letter is in the alphabet
        if letter in alphabet:
            # find the index of the letter in the alphabet
            index = alphabet.index(letter)
            # find the index of the encrypted letter in the encrypted alphabet
            encrypted_index = encrypted_alphabet.index(alphabet[index % len(alphabet)])
            # add the encrypted letter to the encrypted string
            encrypted_string += encrypted_alphabet[encrypted_index]
        else:
            # if the letter is not in the alphabet, add it to the encrypted string without encryption
            encrypted_string += letter
    # return the encrypted string
    return encrypted_string

# test the encrypt function
print(encrypt('hi'))
print(encrypt('asdfghjkl'))
print(encrypt('gf'))
print(encrypt('et'))