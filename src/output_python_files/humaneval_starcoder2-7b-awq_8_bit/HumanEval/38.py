def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
#     split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def encode_vigenere(s: str, key: str):
    """
    returns encoded string by using vigenere cipher.
    """
    # create list of characters from key.
    key_list = list(key)
    # create list of characters from string.
    s_list = list(s)
    # create list of encoded characters.
    encoded_list = []
    # iterate over characters in string.
    for i in range(len(s_list)):
        # get index of character in key.
        key_index = ord(key_list[i % len(key)]) - ord('a')
        # get index of character in string.
        s_index = ord(s_list[i]) - ord('a')
        # get index of encoded character.
        encoded_index = (s_index + key_index) % 26
        # get character from index.
        encoded_list.append(chr(encoded_index + ord('a')))
    # return encoded string.
    return "".join(encoded_list)


def decode_vigenere(s: str, key: str):
    """
    takes as input string encoded with encode_vigenere function. Returns decoded string.
    """
    # create list of characters from key.
    key_list = list(key)
    # create list of characters from string.
    s_list = list(s)
    # create list of decoded characters.
    decoded_list = []
    # iterate over characters in string.
    for i in range(len(s_list)):
        # get index of character in key.
        key_index = ord(key_list[i % len(key)]) - ord('a')
        # get index of character in string.
        s_index = ord(s_list[i]) - ord('a')
        # get index of decoded character.
        decoded_index = (s_index - key_index) % 26
        # get character from index.
        decoded_list.append(chr(decoded_index + ord('a')))
    # return decoded string.
    return "".join(decoded_list)


def encode_affine(s: str, a: int, b: int):
    """
    returns encoded string by using affine cipher.
    """
    # create list of characters from string.
    s_list = list(s)
    # create list of encoded characters.
    encoded_list = []
    # iterate over characters in string.
    for i in range(len(s_list)):
        # get index of character in string.
        s_index = ord(s_list[i]) - ord('a')
        # get index of encoded character.
        encoded_index = (a * s_index + b) % 26
        # get character from index.
        encoded_list.append(chr(encoded_index + ord('a')))
    # return encoded string.
    return "".join(encoded_list)


def decode_affine(s: str, a: int, b: int):
    """
    takes as input string encoded with encode_affine function. Returns decoded string.
    """
    # create list of characters from string.
    s_list = list(s)
    # create list of decoded characters.
    decoded_list = []
    # iterate over characters in string.
    for i in range(len(s_list)):
        # get index of character in string.
        s_index = ord(s_list[i]) -