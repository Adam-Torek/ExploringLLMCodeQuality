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
    message = message.lower()
    message = message.replace('a', 'z')
    message = message.replace('e', 'y')
    message = message.replace('i', 'x')
    message = message.replace('o', 'w')
    message = message.replace('u', 'v')
    message = message.replace('y', 'e')
    message = message.replace('z', 'a')
    message = message.replace('x', 'i')
    message = message.replace('w', 'o')
    message = message.replace('v', 'u')
    return message


def decode(message):
    """
    Write a function that takes a message, and decodes in such a 
    way that it swaps case of all letters, replaces all vowels in 
    the message with the letter that appears 2 places behind that 
    vowel in the english alphabet. 
    Assume only letters. 
    
    Examples:
    >>> decode('TGST')
    'test'
    >>> decode('tHKS KS C MGSSCGG')
    'This is a message'
    """
    message = message.lower()
    message = message.replace('a', 'z')
    message = message.replace('e', 'y')
    message = message.replace('i', 'x')
    message = message.replace('o', 'w')
    message = message.replace('u', 'v')
    message = message.replace('y', 'e')
    message = message.replace('z', 'a')
    message = message.replace('x', 'i')
    message = message.replace('w', 'o')
    message = message.replace('v', 'u')
    return message


def main():
    """
    This is a test function to check your work.
    """
    print(encode('test'))
    print(encode('This is a message'))
    print(decode('TGST'))
    print(decode('tHKS KS C MGSSCGG'))


if __name__ == '__main__':
    main()