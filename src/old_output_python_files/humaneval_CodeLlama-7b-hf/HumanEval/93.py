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
    encoded_message = ''
    for i in range(len(message)):
        if message[i] in 'aeiou':
            encoded_message += message[i+2]
        else:
            encoded_message += message[i]
    return encoded_message

def decode(message):
    """
    Write a function that takes a message, and decodes in such a 
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
    message = message.lower()
    decoded_message = ''
    for i in range(len(message)):
        if message[i] in 'aeiou':
            decoded_message += message[i-2]
        else:
            decoded_message += message[i]
    return decoded_message

def main():
    message = input('Enter a message: ')
    encoded_message = encode(message)
    print('Encoded message:', encoded_message)
    decoded_message = decode(encoded_message)
    print('Decoded message:', decoded_message)

if __name__ == '__main__':
    main()
