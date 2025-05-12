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
    # Your code here
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    rotated_alphabet = alphabet[2:] + alphabet[:2]
    encrypted = ''
    for letter in s:
        if letter in alphabet:
            encrypted += rotated_alphabet[alphabet.index(letter)]
        else:
            encrypted += letter
    return encrypted


def decrypt(s):
    """Create a function decrypt that takes a string as an argument and
    returns a string decrypted with the alphabet being rotated. 
    The alphabet should be rotated in a manner such that the letters 
    shift down by two multiplied to two places.
    For example:
    decrypt('lm') returns 'hi'
    decrypt('ewhjklnop') returns 'asdfghjkl'
    decrypt('kj') returns 'gf'
    decrypt('ix') returns 'et'
    """
    # Your code here
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    rotated_alphabet = alphabet[2:] + alphabet[:2]
    decrypted = ''
    for letter in s:
        if letter in alphabet:
            decrypted += alphabet[rotated_alphabet.index(letter)]
        else:
            decrypted += letter
    return decrypted


def main():
    """
    This function tests the functions in this module.
    """
    # Test encrypt
    assert encrypt('hi') == 'lm'
    assert encrypt('asdfghjkl') == 'ewhjklnop'
    assert encrypt('gf') == 'kj'
    assert encrypt('et') == 'ix'

    # Test decrypt
    assert decrypt('lm') == 'hi'
    assert decrypt('ewhjklnop') == 'asdfghjkl'
    assert decrypt('kj') == 'gf'
    assert decrypt('ix') == 'et'

    # Do not modify the code below this line.
    print('Success!')


if __name__ == '__main__':
    main()
