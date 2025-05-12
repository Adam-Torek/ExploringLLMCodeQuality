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


def encode_vigenere(s: str, k: str):
    """
    returns encoded string by using vigenere cipher.
    """
    return "".join([chr(((ord(ch) + ord(k[i % len(k)])) - ord("a")) % 26 + ord("a")) for i, ch in enumerate(s)])


def decode_vigenere(s: str, k: str):
    """
    takes as input string encoded with encode_vigenere function. Returns decoded string.
    """
    return "".join([chr(((ord(ch) - ord(k[i % len(k)])) + 26) % 26 + ord("a")) for i, ch in enumerate(s)])


def encode_affine(s: str, a: int, b: int):
    """
    returns encoded string by using affine cipher.
    """
    return "".join([chr(((ord(ch) * a + b) % 26) + ord("a")) for ch in s])


def decode_affine(s: str, a: int, b: int):
    """
    takes as input string encoded with encode_affine function. Returns decoded string.
    """
    return "".join([chr(((ord(ch) - b) * a % 26) + ord("a")) for ch in s])


def encode_rail_fence(s: str, n: int):
    """
    returns encoded string by using rail fence cipher.
    """
    if n < 1:
        raise ValueError("n must be greater than 0")
    if n == 1:
        return s
    res = ""
    for i in range(n):
        res += s[i::n]
    return res


def decode_rail_fence(s: str, n: int):
    """
    takes as input string encoded with encode_rail_fence function. Returns decoded string.
    """
    if n < 1:
        raise ValueError("n must be greater than 0")
    if n == 1:
        return s
    res = ""
    for i in range(n):
        res += s[i::n]
    return res


def encode_playfair(s: str, k: str):
    """
    returns encoded string by using playfair cipher.
    """
    if len(s) != len(k):
        raise ValueError("s and k must be of same length")
    res = ""
    for i in range(len(s)):
        if s[i] == k[i]:
            res += s[i]
        else:
            res += s[i] + k[i]
    return res


def decode_playfair(s: str, k: str):
    """
    takes as input string encoded with encode_playfair function. Returns decoded string.
    """
    if len(s) != len(k):
        raise ValueError("s and k must be