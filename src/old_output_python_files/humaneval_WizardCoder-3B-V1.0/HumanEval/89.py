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

def rotate_alphabet(s):
    """Create a function rotate_alphabet that takes a string as an argument and
    returns a string rotated by the given amount.
    For example:
    rotate_alphabet('hi', 2) returns 'lm'
    rotate_alphabet('asdfghjkl', 3) returns 'ewhjklnop'
    rotate_alphabet('gf', 1) returns 'kj'
    rotate_alphabet('et', 0) returns 'ix'
    """

# Test cases
print(encrypt('hi')) # Output: 'lm'
print(encrypt('asdfghjkl')) # Output: 'ewhjklnop'
print(encrypt('gf')) # Output: 'kj'
print(encrypt('et')) # Output: 'ix'

print(rotate_alphabet('hi', 2)) # Output: 'lm'
print(rotate_alphabet('asdfghjkl', 3)) # Output: 'ewhjklnop'
print(rotate_alphabet('gf', 1)) # Output: 'kj'
print(rotate_alphabet('et', 0)) # Output: 'ix'<|endoftext|>