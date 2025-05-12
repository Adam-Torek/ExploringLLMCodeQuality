def encode_shift(s: str):
    """
    returns encoded string by shifting every character by 5 in the alphabet.
    """
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])


def decode_shift(s: str):
    """
    takes as input string encoded with encode_shift function. Returns decoded string.
    """
    return "".join([chr(((ord(ch) - 5 - ord("a")) % 26) + ord("a")) for ch in s])


def encode_rot(s: str):
    """
    returns encoded string by rotating every character by 5 in the alphabet.
    """
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])


def decode_rot(s: str):
    """
    takes as input string encoded with encode_rot function. Returns decoded string.
    """
    return "".join([chr(((ord(ch) - 5 - ord("a")) % 26) + ord("a")) for ch in s])


def encode_vigenere(s: str, key: str):
    """
    returns encoded string by using vigenere cipher.
    """
    return "".join([chr(((ord(ch) + ord(key[i % len(key)])) - ord("a")) % 26 + ord("a")) for i, ch in enumerate(s)])


def decode_vigenere(s: str, key: str):
    """
    takes as input string encoded with encode_vigenere function. Returns decoded string.
    """
    return "".join([chr(((ord(ch) - ord(key[i % len(key)])) - ord("a")) % 26 + ord("a")) for i, ch in enumerate(s)])


def encode_affine(s: str, a: int, b: int):
    """
    returns encoded string by using affine cipher.
    """
    return "".join([chr(((ord(ch) * a + b) - ord("a")) % 26 + ord("a")) for ch in s])


def decode_affine(s: str, a: int, b: int):
    """
    takes as input string encoded with encode_affine function. Returns decoded string.
    """
    return "".join([chr(((ord(ch) - b) * a - ord("a")) % 26 + ord("a")) for ch in s])


def encode_rail_fence(s: str, key: int):
    """
    returns encoded string by using rail fence cipher.
    """
    if key < 1:
        raise ValueError("key must be greater than 0")
    if key == 1:
        return s
    result = ""
    for i in range(key):
        result += s[i::key]
    for i in range(key):
        result += s[i + key::key]
    return result


def decode_rail_fence(s: str, key: int):
    """
    takes as input string encoded with encode_rail_fence function. Returns decoded string.
    """
    if key < 1:
        raise ValueError("key must be greater than 0")
    if key == 1:
        return s
    result = ""
    for i in range(key):
        result += s[i::key]
    for i in range(key):
        result += s[i + key::key]
    return result


def encode_playfair(s: str, key: str):
    """
    returns encoded string by using playfair cipher.
    """
    if len(key) < 2:
        raise ValueError("key must be at least 2 characters long")
    key = key.upper()
    key_dict = {}
    for i, ch in enumerate(key):
        if