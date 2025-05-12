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


def encode_caesar(s: str, shift: int):
    """
    returns encoded string by shifting every character by shift in the alphabet.
    """
    return "".join([chr(((ord(ch) + shift - ord("a")) % 26) + ord("a")) for ch in s])


def decode_caesar(s: str, shift: int):
    """
    takes as input string encoded with encode_caesar function. Returns decoded string.
    """
    return "".join([chr(((ord(ch) - shift + 26) % 26) + ord("a")) for ch in s])


def encode_vigenere(s: str, key: str):
    """
    returns encoded string by shifting every character by shift in the alphabet.
    """
    return "".join([chr(((ord(ch) + ord(key[i % len(key)]) - ord("a")) % 26) + ord("a")) for i, ch in enumerate(s)])


def decode_vigenere(s: str, key: str):
    """
    takes as input string encoded with encode_vigenere function. Returns decoded string.
    """
    return "".join([chr(((ord(ch) - ord(key[i % len(key)]) + 26) % 26) + ord("a")) for i, ch in enumerate(s)])


def encode_affine(s: str, a: int, b: int):
    """
    returns encoded string by shifting every character by shift in the alphabet.
    """
    return "".join([chr(((ord(ch) * a + b - ord("a")) % 26) + ord("a")) for ch in s])


def decode_affine(s: str, a: int, b: int):
    """
    takes as input string encoded with encode_affine function. Returns decoded string.
    """
    return "".join([chr(((ord(ch) * a - b + 26) % 26) + ord("a")) for ch in s])


def encode_rail_fence(s: str, n: int):
    """
    returns encoded string by shifting every character by shift in the alphabet.
    """
    if n == 0:
        return s
    if n < 0:
        raise ValueError("n must be positive")
    encoded = ""
    for i in range(n):
        encoded += "".join([ch for ch in s if (i + 1) % (n + 1) == ord(ch) - ord("a") + 1])
    return encoded


def decode_rail_fence(s: str, n: int):
    """
    takes as input string encoded with encode_rail_fence function. Returns decoded string.
    """
    if n == 0:
        return s
    if n < 0:
        raise ValueError("n must be positive")
    decoded = ""
    for i in range(n):
        decoded += "".join([ch for ch in s if (i + 1) % (n + 1) == ord(ch) - ord("a") + 1])
    return decoded


def encode_morse(s: str):
    """
    returns encoded string by shifting every character by shift in the alphabet.
    """
    morse_code = {
        "a": ".-",
        "b":