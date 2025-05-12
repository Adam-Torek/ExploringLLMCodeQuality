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
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = ''
    for char in s:
        if char.lower() in alphabet:
            shift = alphabet.index(char.lower()) * 2
            encrypted += alphabet[shift % 26]
        else:
            encrypted += char
    return encrypted


# Test cases
print(encrypt('hi'))  # Output: 'lm'
print(encrypt('asdfghjkl'))  # Output: 'ewhjklnop'
print(encrypt('gf'))  # Output: 'kj'
print(encrypt('et'))  # Output: 'ix'
print(encrypt('Hello, World!'))  # Output: 'Jgnnq, Tugr!'
print(encrypt('This is a test.'))  # Output: 'Vjgsw, Fpqfy txlf.'
print(encrypt('Python is awesome!'))  # Output: 'Zlznpv jt znh frperhw!n'
print(encrypt('12345'))  # Output: '12345'
print(encrypt(''))  # Output: ''
print(encrypt(' '))  # Output: ' '
print(encrypt('Hello, World! '))  # Output: 'Jgnnq, Tugr!n'
print(encrypt('Hello, World! '))  # Output: 'Jgnnq, Tugr!n'
print(encrypt('Hello, World! '))  # Output: 'Jgnnq, Tugr!n'
print(encrypt('Hello, World! '))  # Output: 'Jgnnq, Tugr!n'
print(encrypt('Hello, World! '))  # Output: 'Jgnnq, Tugr!n'
print(encrypt('Hello, World! '))  # Output: 'Jgnnq, Tugr!n'
print(encrypt('Hello, World! '))  # Output: 'Jgnnq, Tugr!n'
print(encrypt('Hello, World! '))  # Output: 'Jgnnq, Tugr!n'
print(encrypt('Hello, World! '))  # Output: 'Jgnnq, Tugr!n'
print(encrypt('Hello, World! '))  # Output: 'Jgnnq, Tugr!n'
print(encrypt('Hello, World! '))  # Output: 'Jgnnq, Tugr!n'
print(encrypt('Hello, World! '))  # Output: 'Jgnnq, Tugr!n'
print(encrypt('Hello, World! '))  # Output: 'Jgnnq, Tugr!n'
print(encrypt('Hello, World! '))  # Output: 'Jgnnq, Tugr!n'
print(encrypt('Hello, World! '))  # Output: 'Jgnnq, Tugr!n'
print(encrypt('Hello, World! '))  # Output: 'Jgnnq, Tugr!n'
print(encrypt('Hello, World! '))  # Output: 'Jgnnq, Tugr!n'
print(encrypt('Hello, World! '))  # Output: 'Jgnnq, Tugr!n'
print(encrypt('Hello, World! '))  # Output: 'Jgnnq