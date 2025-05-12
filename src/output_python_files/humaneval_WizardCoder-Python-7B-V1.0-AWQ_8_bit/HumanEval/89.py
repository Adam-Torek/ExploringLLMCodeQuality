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
    return ''.join([new_dict[char] if char in new_dict else char for char in s])


# Test cases
print(encrypt('hi')) # should print 'lm'
print(encrypt('asdfghjkl')) # should print 'ewhjklnop'
print(encrypt('gf')) # should print 'kj'
print(encrypt('et')) # should print 'ix'

# Additional test cases
print(encrypt('hello world')) # should print 'lo rwlqpnfjv'
print(encrypt('python')) # should print 'tynuhmps'
print(encrypt('programming')) # should print 'vqwgxrqzbzc'
print(encrypt('abcdefghijklmnopqrstuvwxyz')) # should print 'cdefghijklmnopqrstuvwxyza'
print(encrypt('zyxwvutsrqponmlkjihgfedcba')) # should print 'zyxwvutsrqponmlkjihgfedcba'
print(encrypt('1234567890')) # should print '1234567890'
print(encrypt('')) # should print ''
print(encrypt(' ')) # should print ' '
print(encrypt('Hello, World!')) # should print 'jgnnq, Tuhfn!'
print(encrypt('Hello, World! ')) # should print 'jgnnq, Tuhfn! '
print(encrypt('Hello, World! ')) # should print 'jgnnq, Tuhfn! '
print(encrypt('Hello, World! ')) # should print 'jgnnq, Tuhfn! '
print(encrypt('Hello, World! ')) # should print 'jgnnq, Tuhfn! '
print(encrypt('Hello, World! ')) # should print 'jgnnq, Tuhfn! '
print(encrypt('Hello, World! ')) # should print 'jgnnq, Tuhfn! '
print(encrypt('Hello, World! ')) # should print 'jgnnq, Tuhfn! '
print(encrypt('Hello, World! ')) # should print 'jgnnq, Tuhfn! '
print(encrypt('Hello, World! ')) # should print 'jgnnq, Tuhfn! '
print(encrypt('Hello, World! ')) # should print 'jgnnq, Tuhfn! '
print(encrypt('Hello, World! ')) # should print 'jgnnq, Tuhfn! '
print(encrypt('Hello, World! ')) # should print 'jgnnq, Tuhfn! '
print(encrypt('Hello, World! ')) # should print 'jgnnq, Tuhfn! '
print(encrypt('Hello, World! ')) # should print 'jgnnq, Tuhfn! '
print(encrypt('Hello, World! ')) # should print 'jgnnq, Tuhfn! '
print(encrypt('Hello, World! ')) # should print 'jgnnq, Tuhfn! '
print(encrypt('Hello, World! ')) # should print 'jgnnq, Tuhfn! '
print(encrypt('Hello, World! ')) # should print 'jgnnq, Tuhfn! '
print(encrypt('Hello, World! ')) # should print 'jgnnq, Tuhfn! '
print(encrypt