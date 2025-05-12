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
    vowels = 'aeiou'
    result = ''
    for char in message:
        if char.isalpha():
            if char.islower():
                result += chr(ord(char) + 2)
            else:
                result += chr(ord(char) - 2)
        else:
            result += char
    return result

def decode(message):
    """
    Write a function that takes a message, and decodes it in such a 
    way that it swaps case of all letters, replaces all vowels in 
    the message with the letter that appears 2 places before that 
    vowel in the english alphabet. 
    Assume only letters. 
    
    Examples:
    >>> decode('TGST')
    'test'
    >>> decode('tHKS KS C MGSSCGG')
    'This is a message'
    """
    vowels = 'aeiou'
    result = ''
    for char in message:
        if char.isalpha():
            if char.islower():
                result += chr(ord(char) - 2)
            else:
                result += chr(ord(char) + 2)
        else:
            result += char
    return result