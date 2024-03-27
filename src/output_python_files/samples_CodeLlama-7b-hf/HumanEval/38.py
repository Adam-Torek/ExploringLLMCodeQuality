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
    return "".join([chr((ord(c) + ord(key[i % len(key)])) % 256) for i, c in enumerate(s)])


def decode_vigenere(s: str, key: str):
    """
    takes as input string encoded with encode_vigenere function. Returns decoded string.
    """
    return "".join([chr((ord(c) - ord(key[i % len(key)])) % 256) for i, c in enumerate(s)])


def encode_affine(s: str, a: int, b: int):
    """
    returns encoded string by shifting each character by shift.
    """
    return "".join([chr((ord(c) * a + b) % 256) for c in s])


def decode_affine(s: str, a: int, b: int):
    """
    takes as input string encoded with encode_affine function. Returns decoded string.
    """
    return "".join([chr((ord(c) - b) % 256) for c in s])


def encode_rail_fence(s: str, n: int):
    """
    returns encoded string by shifting each character by shift.
    """
    # create matrix of size n x len(s)
    matrix = [[" " for _ in range(len(s))] for _ in range(n)]
    # fill matrix with characters
    for i, c in enumerate(s):
        matrix[i % n][i // n] = c
    # join matrix elements
    return "".join([row[i] for row in matrix for i in range(len(s))])


def decode_rail_fence(s: str, n: int):
    """
    takes as input string encoded with encode_rail_fence function. Returns decoded string.
    """
    # create matrix of size n x len(s)
    matrix = [[" " for _ in range(len(s))] for _ in range(n)]
    # fill matrix with characters
    for i, c in enumerate(s):
        matrix[i % n][i // n] = c
    # join matrix elements
    return "".join([row[i] for row in matrix for i in range(len(s))])


def encode_morse(