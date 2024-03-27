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
    vowels = "aeiou"
    encoded_message = ""
    for char in message:
        if char.isalpha():
            if char.islower():
                encoded_message += char.upper()
            else:
                encoded_message += char.lower()
        elif char in vowels:
            index = vowels.index(char)
            encoded_message += chr(ord(char) + 3)
        else:
            encoded_message += char
    return encoded_message

def decode(encoded_message):
    """
    Write a function that takes an encoded message, and decodes it 
    by swapping case of all letters, and replacing all letters 
    that are 3 places ahead of them in the english alphabet with 
    the original vowels. 

    Examples:
    >>> decode('TGST')
    'test'
    >>> decode('tHKS KS C MGSSCGG')
    'This is a message'
    """
    vowels = "aeiou"
    decoded_message = ""
    for char in encoded_message:
        if char.isalpha():
            if char.islower():
                decoded_message += char.upper()
            else:
                decoded_message += char.lower()
        elif char in vowels:
            index = vowels.index(char)
            decoded_message += vowels[index]
        else:
            decoded_message += char
    return decoded_message

if __name__ == "__main__":
    message = "This is a message"
    encoded_message = encode(message)
    print(encoded_message)
    decoded_message = decode(encoded_message)
    print(decoded_message)</s>