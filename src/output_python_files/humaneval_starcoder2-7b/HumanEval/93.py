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

def decode(message):
    """
    Write a function that takes a message, and decodes it in such a 
    way that it swaps case of all letters, replaces all vowels in 
    the message with the letter that appears 2 places ahead of that 
    vowel in the english alphabet. 
    Assume only letters. 
    
    Examples:
    >>> decode('TGST')
    'test'
    >>> decode('tHKS KS C MGSSCGG')
    'This is a message'
    """

def encode_decode(message):
    """
    Write a function that takes a message, and encodes it in such a 
    way that it swaps case of all letters, replaces all vowels in 
    the message with the letter that appears 2 places ahead of that 
    vowel in the english alphabet. 
    Assume only letters. 
    
    Examples:
    >>> encode_decode('test')
    'TGST'
    >>> encode_decode('This is a message')
    'tHKS KS C MGSSCGG'
    >>> encode_decode('tHKS KS C MGSSCGG')
    'This is a message'
    """

def encode_decode_file(filename):
    """
    Write a function that takes a filename, and encodes it in such a 
    way that it swaps case of all letters, replaces all vowels in 
    the message with the letter that appears 2 places ahead of that 
    vowel in the english alphabet. 
    Assume only letters. 
    
    Examples:
    >>> encode_decode_file('test.txt')
    'TGST'
    >>> encode_decode_file('test2.txt')
    'tHKS KS C MGSSCGG'
    >>> encode_decode_file('test3.txt')
    'This is a message'
    """

def encode_decode_file_with_key(filename, key):
    """
    Write a function that takes a filename, and encodes it in such a 
    way that it swaps case of all letters, replaces all vowels in 
    the message with the letter that appears 2 places ahead of that 
    vowel in the english alphabet. 
    Assume only letters. 
    
    Examples:
    >>> encode_decode_file_with_key('test.txt', 1)
    'TGST'
    >>> encode_decode_file_with_key('test2.txt', 1)
    'tHKS KS C MGSSCGG'
    >>> encode_decode_file_with_key('test3.txt', 1)
    'This is a message'
    >>> encode_decode_file_with_key('test3.txt', 2)
    'tHKS KS C MGSSCGG'
    """

def encode_decode_file_with_key_and_file(filename, key, output_filename):
    """
    Write a function that takes a filename, and encodes it in such a 
    way that it swaps case of all letters, replaces all vowels in 
    the message with the letter that appears 2 places ahead of that 
    vowel in the english alphabet. 
    Assume only letters. 
    
    Examples:
    >>> encode_decode_file_with_key_and_file('test.txt', 1, 'test_output.txt')