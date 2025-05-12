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
    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def encode_caesar(s: str, shift: int):
    """
    returns encoded string by shifting each character by shift.
    """
    return "".join([chr((ord(c) + shift) % 256) for c in s])


def decode_caesar(s: str, shift: int):
    """
    takes as input string encoded with encode_caesar function. Returns decoded string.
    """
    return "".join([chr((ord(c) - shift) % 256) for c in s])


def encode_vigenere(s: str, key: str):
    """
    returns encoded string by shifting each character by shift.
    """
    # get shift for each character in key.
    shifts = [ord(c) % 256 for c in key]
    # get shift for each character in s.
    shifts += [0] * (len(s) - len(key))
    # encode each character in s.
    return "".join([chr((ord(c) + shifts[i]) % 256) for i, c in enumerate(s)])


def decode_vigenere(s: str, key: str):
    """
    takes as input string encoded with encode_vigenere function. Returns decoded string.
    """
    # get shift for each character in key.
    shifts = [ord(c) % 256 for c in key]
    # get shift for each character in s.
    shifts += [0] * (len(s) - len(key))
    # decode each character in s.
    return "".join([chr((ord(c) - shifts[i]) % 256) for i, c in enumerate(s)])


def encode_substitution(s: str, key: str):
    """
    returns encoded string by substituting each character with corresponding character in key.
    """
    # get substitution for each character in s.
    substitutions = [key[ord(c) % len(key)] for c in s]
    # encode each character in s.
    return "".join(substitutions)


def decode_substitution(s: str, key: str):
    """
    takes as input string encoded with encode_substitution function. Returns decoded string.
    """
    # get substitution for each character in s.
    substitutions = [key[ord(c) % len(key)] for c in s]
    # decode each character in s.
    return "".join(substitutions)


def encode_transposition(s: str, key: str):
    """
    returns encoded string by transposing each character with corresponding character in key.
    """
    # get transposition for each character in s.
    transpositions = [key[ord(c) % len(key)] for c in s]
    # encode each character in s.
    return "".join(transpositions)


def decode_transposition(s: str, key: str):
    """
    takes as input