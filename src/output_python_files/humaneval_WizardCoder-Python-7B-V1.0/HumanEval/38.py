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
    # reverse elements in each group. Unless group has fewer elements than 3.
    groups = [(group[-1:] + group[:-1]) if len(group) == 3 else group for group in groups]
    return "".join(groups)

def encode_base64(s: str):
    """
    returns encoded string in base64 format.
    """
    return base64.b64encode(s.encode("utf-8")).decode("utf-8")

def decode_base64(s: str):
    """
    takes as input string encoded in base64 format. Returns decoded string.
    """
    return base64.b64decode(s.encode("utf-8")).decode("utf-8")

def encode_rot13(s: str):
    """
    returns encoded string using rot13 cipher.
    """
    return codecs.encode(s, "rot_13")

def decode_rot13(s: str):
    """
    takes as input string encoded with rot13 cipher. Returns decoded string.
    """
    return codecs.decode(s, "rot_13")

def encode_hex(s: str):
    """
    returns encoded string in hex format.
    """
    return s.encode("utf-8").hex()

def decode_hex(s: str):
    """
    takes as input string encoded in hex format. Returns decoded string.
    """
    return bytes.fromhex(s).decode("utf-8")

def encode_base32(s: str):
    """
    returns encoded string in base32 format.
    """
    return base64.b32encode(s.encode("utf-8")).decode("utf-8")

def decode_base32(s: str):
    """
    takes as input string encoded in base32 format. Returns decoded string.
    """
    return base64.b32decode(s.encode("utf-8")).decode("utf-8")

def encode_base85(s: str):
    """
    returns encoded string in base85 format.
    """
    return base64.b85encode(s.encode("utf-8")).decode("utf-8")

def decode_base85(s: str):
    """
    takes as input string encoded in base85 format. Returns decoded string.
    """
    return base64.b85decode(s.encode("utf-8")).decode("utf-8")

def encode_ascii85(s: str):
    """
    returns encoded string in ascii85 format.
    """
    return base64.a85encode(s.encode("utf-8")).decode("utf-8")

def decode_ascii85(s: str):
    """
    takes as input string encoded in ascii85 format. Returns decoded string.
    """
    return base64.a85decode(s.encode("utf-8")).decode("utf-8")

def encode_morse(s: str):
    """
    returns encoded string in morse code format.
    """
    morse_code = {
        'A': '.-', 'B': '-...', 'C