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
    return ''.join([chr((ord(x) - 97 + 2 * 2) % 26 + 97) for x in s])


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
    return ''.join([chr((ord(x) - 97 - 2 * 2) % 26 + 97) for x in s])


def main():
    """Read in a string from the user and print out the encrypted and
    decrypted versions of the string.
    """
    s = input('Enter a string: ')
    print('Encrypted:', encrypt(s))
    print('Decrypted:', decrypt(encrypt(s)))


if __name__ == '__main__':
    main()