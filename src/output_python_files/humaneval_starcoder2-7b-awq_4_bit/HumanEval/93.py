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
    Write a function that takes a message, encodes it, and then 
    decodes it. 
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
    Write a function that takes a filename, encodes it, and then 
    decodes it. 
    Assume only letters. 
    
    Examples:
    >>> encode_decode_file('test.txt')
    'TGST'
    >>> encode_decode_file('test.txt')
    'This is a message'
    """

def encode_decode_file_with_key(filename, key):
    """
    Write a function that takes a filename, encodes it, and then 
    decodes it. 
    Assume only letters. 
    
    Examples:
    >>> encode_decode_file_with_key('test.txt', 1)
    'TGST'
    >>> encode_decode_file_with_key('test.txt', 1)
    'This is a message'
    """

def encode_decode_file_with_key_and_file(filename, key, output_filename):
    """
    Write a function that takes a filename, encodes it, and then 
    decodes it. 
    Assume only letters. 
    
    Examples:
    >>> encode_decode_file_with_key_and_file('test.txt', 1, 'output.txt')
    'TGST'
    >>> encode_decode_file_with_key_and_file('test.txt', 1, 'output.txt')
    'This is a message'
    """

def encode_decode_file_with_key_and_file_and_key(filename, key, output_filename):
    """
    Write a function that takes a filename, encodes it, and then 
    decodes it. 
    Assume only letters. 
    
    Examples:
    >>> encode_decode_file_with_key_and_file_and_key('test.txt', 1, 'output.txt', 2)
    'TGST'
    >>> encode_decode_file_with_key_and_file_and_key('test.txt', 1, 'output.txt', 2)
    'This is a message'
    """

def encode_decode_file_with_key_and_file_and_key_and_file(filename, key, output_filename):
    """
    Write a function that takes a filename, encodes it, and then