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
    # split string to groups of three characters.
    groups = [s[i:i+3] for i in range(0, len(s), 3)]
    # reverse order of elements in each group.
    groups = [group[::-1] for group in groups]
    # concatenate groups.
    return "".join(groups)

def encode_base64(s: str):
    """
    returns base64 encoded string.
    """
    return base64.b64encode(s.encode("utf-8")).decode("utf-8")

def decode_base64(s: str):
    """
    takes as input base64 encoded string. Returns decoded string.
    """
    return base64.b64decode(s.encode("utf-8")).decode("utf-8")

def encode_base64_cyclic(s: str):
    """
    returns base64 encoded string with cyclic encoding.
    """
    return encode_base64(cyclic_encode(s))

def decode_base64_cyclic(s: str):
    """
    takes as input base64 encoded string with cyclic encoding. Returns decoded string.
    """
    return decode_cyclic(decode_base64(s))

def encode_base64_cyclic_urlsafe(s: str):
    """
    returns base64 urlsafe encoded string with cyclic encoding.
    """
    return base64.urlsafe_b64encode(s.encode("utf-8")).decode("utf-8")

def decode_base64_cyclic_urlsafe(s: str):
    """
    takes as input base64 urlsafe encoded string with cyclic encoding. Returns decoded string.
    """
    return decode_cyclic(base64.urlsafe_b64decode(s.encode("utf-8")).decode("utf-8"))

def encode_base64_urlsafe(s: str):
    """
    returns base64 urlsafe encoded string.
    """
    return base64.urlsafe_b64encode(s.encode("utf-8")).decode("utf-8")

def decode_base64_urlsafe(s: str):
    """
    takes as input base64 urlsafe encoded string. Returns decoded string.
    """
    return base64.urlsafe_b64decode(s.encode("utf-8")).decode("utf-8")

def encode_base64_urlsafe_cyclic(s: str):
    """
    returns base64 urlsafe encoded string with cyclic encoding.
    """
    return encode_base64_urlsafe(cyclic_encode(s))

def decode_base64_urlsafe_cyclic(s: str):
    """
    takes as input base64 urlsafe encoded string with cyclic encoding. Returns decoded string.
    """
    return decode_cyclic(decode_base64_urlsafe(s))

def encode_base64_urlsafe_cyclic_urlsafe(s: str):
    """
    returns base64 urlsafe encoded string with cyclic encoding.
    """
    return base64.urlsafe_b64encode(cyclic_encode(s).encode("utf-8")).decode("utf-8")

def decode_base64_urlsafe_cyclic_urlsafe(s: str):
    """
    takes as input base64 urlsafe encoded string with cyclic encoding. Returns decoded string.