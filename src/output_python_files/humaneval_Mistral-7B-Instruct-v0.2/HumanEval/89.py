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
    #Your code here
    result = ""
    for char in s:
        if char.isalpha():
            ascii_num = ord(char)
            if char.islower():
                result += chr((ord(char) - 97 + 26) % 26 + 97)
            else:
                result += chr((ord(char) - 65 + 26) % 26 + 65)
        else:
            result += char
    return result

#Test cases
print(encrypt('hi'))
print(encrypt('asdfghjkl'))
print(encrypt('gf'))
print(encrypt('et'))</s>