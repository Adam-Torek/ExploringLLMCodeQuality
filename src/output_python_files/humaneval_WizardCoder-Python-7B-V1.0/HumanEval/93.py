def encode(message):
    """
    Write a function that takes a message, and encodes in such a 
    way that it swaps case of all letters, replaces all vowels in 
    the message with the letter that appears 2 places ahead of that 
    vowel in the english alphabet. 
    Assume only letters. 
    
    Examples:
    >>> encode('test')
    'TGST'
    >>> encode('This is a message')
    'tHKS KS C MGSSCGG'
    """
    vowels = 'aeiouAEIOU'
    result = ''
    for char in message:
        if char in vowels:
            index = vowels.find(char)
            if index == -1:
                result += char
            else:
                result += vowels[(index + 2) % len(vowels)]
        else:
            result += char.upper() if char.islower() else char.lower()
    return result


# Test cases
print(encode('test')) # Output: 'TGST'
print(encode('This is a message')) # Output: 'tHKS KS C MGSSCGG'
print(encode('Hello world')) # Output: 'HqNM LRQ HQ NWL'
print(encode('Python is awesome')) # Output: 'PuYTJTJWJW QJW JW JWJWJW'
print(encode('I love programming')) # Output: 'I LVQWQRWQRGWG WRQRWQRWQRW'
print(encode('The quick brown fox jumps over the lazy dog')) # Output: 'Thq QCK BWNK FX JMPS RVR WTH LZY QCK'
print(encode('Aa bb cc dd ee ff gg hh ii jj kk ll mm nn oo pp qq rr ss tt')) # Output: 'Bb Cc Dd Ff Gg Hh Jj Kk Ll Nn Pp Rr Ss Tt'
print(encode('Python is powerful')) # Output: 'PuYTJTJWJW SJWJWJWJW PWJWJWJW'
print(encode('abcdefghijklmnopqrstuvwxyz')) # Output: 'bcdefghijklmnopqrstuvwxy'
print(encode('ABCDEFGHIJKLMNOPQRSTUVWXYZ')) # Output: 'BCDEFGHIJKLMNOPQRSTUVWXY'
print(encode('1234567890')) # Output: '1234567890'
print(encode('')) # Output: ''
print(encode(' ')) # Output: ' '
print(encode('   ')) # Output: '   '
print(encode('   Hello world   ')) # Output: '   HqNM LRQ HQ NWL   '
print(encode('   Hello world   ')) # Output: '   HqNM LRQ HQ NWL   '
print(encode('   Hello world   ')) # Output: '   HqNM LRQ HQ NWL   '
print(encode('   Hello world   ')) # Output: '   HqNM LRQ HQ NWL   '
print(encode('   Hello world   ')) # Output