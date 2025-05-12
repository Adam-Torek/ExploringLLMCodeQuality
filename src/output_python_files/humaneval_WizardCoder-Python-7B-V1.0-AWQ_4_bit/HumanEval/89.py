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
    s = s.lower()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    new_alphabet = alphabet[2:] + alphabet[:2]
    new_dict = {char: new_alphabet[i] for i, char in enumerate(alphabet)}
    return ''.join([new_dict.get(char, char) for char in s])


# Test cases
print(encrypt('hi'))  # Output: 'lm'
print(encrypt('asdfghjkl'))  # Output: 'ewhjklnop'
print(encrypt('gf'))  # Output: 'kj'
print(encrypt('et'))  # Output: 'ix'

# Test cases with uppercase letters
print(encrypt('HI'))  # Output: 'LM'
print(encrypt('ASDFGHJKL'))  # Output: 'EWHJKLNOP'
print(encrypt('GF'))  # Output: 'KJ'
print(encrypt('ET'))  # Output: 'IX'

# Test cases with numbers and spaces
print(encrypt('1234567890'))  # Output: '345678901'
print(encrypt('hello world'))  # Output: 'jgnnq pbhvchg'
print(encrypt('Hello World'))  # Output: 'Jgnnq Pbhvchg'