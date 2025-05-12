def encode_shift(s: str):
    """
    returns encoded string by shifting every character by 5 in the alphabet.
    """
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])


def decode_shift(s: str):
    """
    takes as input string encoded with encode_shift function. Returns decoded string.
    """
    return "".join([chr(((ord(ch) - 5 - ord("a")) % 26 + ord("a")) for ch in s) if ch.isalpha() else ch for ch in s]


def encode_rot13(s: str):
    """
    returns encoded string using rot13 cipher.
    """
    return s.encode("rot13")

def decode_rot13(s: str):
    """
    takes as input string encoded with encode_rot13 function. Returns decoded string.
    """
    return s.encode("rot13")

def encode_vigenere(s: str, key: str):
    """
    returns encoded string using vigenere cipher with key.
    """
    key = key.lower()
    key_len = len(key)
    return "".join([chr(((ord(ch) + ord(key[i % key_len]) - 2*ord("a")) % 26 + ord("a")) for i, ch in enumerate(s) if ch.isalpha())]

def decode_vigenere(s: str, key: str):
    """
    takes as input string encoded with encode_vigenere function. Returns decoded string.
    """
    key = key.lower()
    key_len = len(key)
    return "".join([chr(((ord(ch) - ord(key[i % key_len]) - 2*ord("a")) % 26 + ord("a")) for i, ch in enumerate(s) if ch.isalpha())]

def encode_xor(s: str, key: str):
    """
    returns encoded string using xor cipher with key.
    """
    key = key.lower()
    return "".join([chr(ord(ch) ^ ord(key[i % len(key)]) for i, ch in enumerate(s)])

def decode_xor(s: str, key: str):
    """
    takes as input string encoded with encode_xor function. Returns decoded string.
    """
    key = key.lower()
    return "".join([chr(ord(ch) ^ ord(key[i % len(key)]) for i, ch in enumerate(s)])

def encode_base64(s: str):
    """
    returns encoded string using base64 encoding.
    """
    return base64.b64encode(s.encode("utf-8")).decode("utf-8")

def decode_base64(s: str):
    """
    takes as input string encoded with encode_base64 function. Returns decoded string.
    """
    return base64.b64decode(s.encode("utf-8")).decode("utf-8")

def encode_hex(s: str):
    """
    returns encoded string using hex encoding.
    """
    return s.encode("utf-8").hex()

def decode_hex(s: str):
    """
    takes as input string encoded with encode_hex function. Returns decoded string.
    """
    return bytes.fromhex(s).decode("utf-8")

def encode_b64_to_hex(s: str):
    """
    returns encoded string using base64 encoding and then hex encoding.
    """
    return encode_hex(encode_base64(s))

def decode_hex_to_b64(s: str):
    """
    takes as input string encoded with encode_b64_to_hex function. Returns decoded string.
    """
    return decode_base64(decode_hex(s))

def encode_base