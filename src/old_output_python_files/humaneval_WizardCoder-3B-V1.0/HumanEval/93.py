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

#     # Create a dictionary to store the frequency of each letter
#     freq = {}
#     for letter in message:
#         if letter in freq:
#             freq[letter] += 1
#         else:
#             freq[letter] = 1

#     # Sort the dictionary by frequency in descending order
#     sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

#     # Create a list of tuples containing the letter and its frequency
#     sorted_freq_list = [(letter, freq[letter]) for letter, _ in sorted_freq]

#     # Create a list of tuples containing the letter and its frequency
#     encoded_message = []
#     for letter, freq in sorted_freq_list:
#         if letter.isupper():
#             encoded_message.append(letter.lower())
#         else:
#             encoded_message.append(letter.upper())

#     # Replace vowels with the letter that appears 2 places ahead of that vowel
#     vowels = ['a', 'e', 'i', 'o', 'u']
#     for i, letter in enumerate(encoded_message):
#         if letter in vowels:
#             if i + 2 < len(encoded_message) and encoded_message[i + 2] in vowels:
#                 encoded_message[i] = encoded_message[i + 2]

#     return ''.join(encoded_message)

    # Alternative solution using a single loop
    encoded_message = []
    for letter in message:
        if letter.isupper():
            encoded_message.append(letter.lower())
        else:
            encoded_message.append(letter.upper())

    for i, letter in enumerate(encoded_message):
        if letter in vowels:
            if i + 2 < len(encoded_message) and encoded_message[i + 2] in vowels:
                encoded_message[i] = encoded_message[i + 2]

    return ''.join(encoded_message)


# Test cases
print(encode('test'))  # Output: 'TGST'
print(encode('This is a message'))  # Output: 'tHKS KS C MGSSCGG'<|endoftext|>