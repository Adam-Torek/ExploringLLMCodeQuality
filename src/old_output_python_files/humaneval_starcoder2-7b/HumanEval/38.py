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

def encode_vigenere(s: str, key: str):
    """
    takes as input string and key. Returns encoded string.
    """
    # create list of characters from key
    key_list = list(key)
    # create list of characters from string
    s_list = list(s)
    # create list of encoded characters
    encoded_list = []
    # iterate over characters in string
    for i in range(len(s_list)):
        # get index of character in key
        key_index = key_list.index(s_list[i])
        # get character from key
        key_char = key_list[key_index]
        # get index of character in alphabet
        alphabet_index = alphabet.index(key_char)
        # get character from alphabet
        alphabet_char = alphabet[alphabet_index]
        # get index of character in encoded alphabet
        encoded_index = encoded_alphabet.index(alphabet_char)
        # get character from encoded alphabet
        encoded_char = encoded_alphabet[encoded_index]
        # add character to encoded list
        encoded_list.append(encoded_char)
    # return encoded string
    return "".join(encoded_list)


def decode_vigenere(s: str, key: str):
    """
    takes as input string and key. Returns decoded string.
    """
    # create list of characters from key
    key_list = list(key)
    # create list of characters from string
    s_list = list(s)
    # create list of decoded characters
    decoded_list = []
    # iterate over characters in string
    for i in range(len(s_list)):
        # get index of character in key
        key_index = key_list.index(s_list[i])
        # get character from key
        key_char = key_list[key_index]
        # get index of character in alphabet
        alphabet_index = alphabet.index(key_char)
        # get character from alphabet
        alphabet_char = alphabet[alphabet_index]
        # get index of character in decoded alphabet
        decoded_index = decoded_alphabet.index(alphabet_char)
        # get character from decoded alphabet
        decoded_char = decoded_alphabet[decoded_index]
        # add character to decoded list
        decoded_list.append(decoded_char)
    # return decoded string
    return "".join(decoded_list)


def encode_affine(s: str, a: int, b: int):
    """
    takes as input string and two integers. Returns encoded string.
    """
    # create list of characters from string
    s_list = list(s)
    # create list of encoded characters
    encoded_list = []
    # iterate over characters in string
    for i in range(len(s_list)):
        # get character from string
        char = s_list[i]
        # get index of character in alphabet
        alphabet_index = alphabet.index(char)
        # get character from alphabet
        alphabet_char = alphabet[alphabet_index]
        # get index of character in encoded alphabet
        encoded_index = (a * alphabet_index + b) % 26
        # get character from encoded alphabet
        encoded_char = encoded_alphabet[encoded_index]
        # add character to encoded list
        encoded_list.append(encoded_char)
    # return encoded string
    return "".join(encoded_list)


def decode_affine(s: str, a: int, b: int):
    """
    takes as input string and two integers. Returns decoded string.
    """
    # create list of characters from string
    s_list = list(s)
    # create list of decoded characters
    decoded_list = []
    # iterate over characters in string
    for i in range(len(s_list)):
        # get character from string
        char = s_list[i]
        # get index of character in alphabet
        alphabet_index = encoded_alphabet.index(char)
        # get character from