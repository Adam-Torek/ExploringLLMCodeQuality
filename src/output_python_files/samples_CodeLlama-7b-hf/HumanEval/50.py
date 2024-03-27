def encode_shift(s: str):
    """
    returns encoded string by shifting every character by 5 in the alphabet.
    """
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])


def decode_shift(s: str):
    """
    takes as input string encoded with encode_shift function. Returns decoded string.
    """
    return "".join([chr(((ord(ch) - 5 + 26) % 26) + ord("a")) for ch in s])


def encode_rot(s: str):
    """
    returns encoded string by rotating every character by 5 in the alphabet.
    """
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])


def decode_rot(s: str):
    """
    takes as input string encoded with encode_rot function. Returns decoded string.
    """
    return "".join([chr(((ord(ch) - 5 + 26) % 26) + ord("a")) for ch in s])


def encode_vigenere(s: str, key: str):
    """
    returns encoded string by using vigenere cipher.
    """
    return "".join([chr(((ord(ch) + ord(key[i % len(key)])) % 26) + ord("a")) for i, ch in enumerate(s)])


def decode_vigenere(s: str, key: str):
    """
    takes as input string encoded with encode_vigenere function. Returns decoded string.
    """
    return "".join([chr(((ord(ch) - ord(key[i % len(key)])) % 26) + ord("a")) for i, ch in enumerate(s)])


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
    if n <= 0:
        raise ValueError("n must be greater than 0")
    if n == 1:
        return s
    res = ""
    for i in range(n):
        res += "".join([ch for ch in s if (i + (ord(ch) - ord("a")) % n) % n == i])
    return res


def decode_rail_fence(s: str, n: int):
    """
    takes as input string encoded with encode_rail_fence function. Returns decoded string.
    """
    if n <= 0:
        raise ValueError("n must be greater than 0")
    if n == 1:
        return s
    res = ""
    for i in range(n):
        res += "".join([ch for ch in s if (i + (ord(ch) - ord("a")) % n) % n == i])
    return res


def encode_atbash(s: str):
    """
    returns encoded string by using atbash cipher.
    """
    return "".join([chr((25 - ord(ch) + ord("a")) % 26) for ch in s])


def decode_atbash(s: str):
    """
    takes as input string encoded with encode_atbash function. Returns decoded string.
    """
    return "".join([chr((25 - ord(ch) + ord("a")) % 26) for ch in s])


def encode_morse(s: str):