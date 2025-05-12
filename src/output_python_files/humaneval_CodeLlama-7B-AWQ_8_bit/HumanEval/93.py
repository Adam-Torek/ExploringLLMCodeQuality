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
    # Your code here
    pass

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
    # Your code here
    pass

def main():
    """
    This is a main function that will test your encode and decode functions.
    """
    print('Running tests...')
    test_encode()
    test_decode()
    print('Passed!')

def test_encode():
    """
    This function tests your encode function.
    """
    print('Running test_encode...')
    assert encode('test') == 'TGST'
    assert encode('This is a message') == 'tHKS KS C MGSSCGG'
    print('Passed test_encode!')

def test_decode():
    """
    This function tests your decode function.
    """
    print('Running test_decode...')
    assert decode('TGST') == 'test'
    assert decode('tHKS KS C MGSSCGG') == 'This is a message'
    print('Passed test_decode!')

if __name__ == '__main__':
    main()