def encode_shift(s: str):
    """
    returns encoded string by shifting every character by 5 in the alphabet.
    """
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])


def decode_shift(s: str):
    """
    takes as input string encoded with encode_shift function. Returns decoded string.
    """
#    return "".join([chr(((ord(ch) - 5 - ord("a")) % 26) + ord("a")) for ch in s])
    return "".join([chr(((ord(ch) - 5 - ord("a")) % 26) + ord("a")) for ch in s])


def encode_vigenere(s: str, key: str):
    """
    returns encoded string by shifting every character by the value of the key.
    """
    return "".join([chr(((ord(ch) + ord(key[i % len(key)]) - ord("a")) % 26) + ord("a")) for i, ch in enumerate(s)])


def decode_vigenere(s: str, key: str):
    """
    takes as input string encoded with encode_vigenere function. Returns decoded string.
    """
    return "".join([chr(((ord(ch) - ord(key[i % len(key)]) - ord("a")) % 26) + ord("a")) for i, ch in enumerate(s)])


def encode_caesar(s: str, key: int):
    """
    returns encoded string by shifting every character by the value of the key.
    """
    return "".join([chr(((ord(ch) + key - ord("a")) % 26) + ord("a")) for ch in s])


def decode_caesar(s: str, key: int):
    """
    takes as input string encoded with encode_caesar function. Returns decoded string.
    """
    return "".join([chr(((ord(ch) - key - ord("a")) % 26) + ord("a")) for ch in s])


def encode_affine(s: str, key: int):
    """
    returns encoded string by shifting every character by the value of the key.
    """
    return "".join([chr(((ord(ch) * key + ord("a")) % 26) + ord("a")) for ch in s])


def decode_affine(s: str, key: int):
    """
    takes as input string encoded with encode_affine function. Returns decoded string.
    """
    return "".join([chr(((ord(ch) - ord("a")) * key - ord("a")) % 26) + ord("a")) for ch in s])


def encode_substitution(s: str, key: str):
    """
    returns encoded string by shifting every character by the value of the key.
    """
    return "".join([key[ord(ch) - ord("a")] for ch in s])


def decode_substitution(s: str, key: str):
    """
    takes as input string encoded with encode_substitution function. Returns decoded string.
    """
    return "".join([key[ord(ch) - ord("a")] for ch in s])


def encode_rail_fence(s: str, key: int):
    """
    returns encoded string by shifting every character by the value of the key.
    """
    return "".join([s[i] for i in range(len(s)) if i % (key - 1) == 0])


def decode_rail_fence(s: str, key: int):
    """
    takes as input string encoded with encode_rail_fence function. Returns decoded string.
    """
    return "".join([s[i] for i in range(len(s)) if i % (key - 1) == 0])


def encode_morse(s: str):
    """
    returns encoded string by shifting every character by the value of the key.
    """
    return "".join([MORSE_CODE[ch] for ch in s])


def decode_morse(s: str):
    """
    takes as input string encoded with encode_morse function. Returns decoded string.
    """
    return "".join([MORSE_CODE_REVERSE[ch] for ch in s])


def encode_atbash(s: str):
    """
    returns encoded string by shifting every character by the value of the key.
    """
    return "".join([chr(25 - ord(ch) + ord("