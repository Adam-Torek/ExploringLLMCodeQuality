def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """
    if not text:
        return None
    return hashlib.md5(text.encode('utf-8')).hexdigest()


def string_to_sha256(text):
    """
    Given a string 'text', return its sha256 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_sha256('Hello world') == 'a591a6d40bf420404ec991c6bc642313e9072c32528c0b078e9071e3e4a7b7ac7c'
    """
    if not text:
        return None
    return hashlib.sha256(text.encode('utf-8')).hexdigest()

def string_to_sha512(text):
    """
    Given a string 'text', return its sha512 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_sha512('Hello world') == '8dd9d25e4b975d6d021f819266113f7c43d5415040a3a77b26e8d903176c42a5e61ad27d5d182100b056c06c799f7e7e7e7e0e03f7e'
    """
    if not text:
        return None
    return hashlib.sha512(text.encode('utf-8')).hexdigest()

def string_to_sha3_256(text):
    """
    Given a string 'text', return its sha3_256 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_sha3_256('Hello world') == 'a591a6dc0608652715871a84a07c72a2a27258b12a437c536f158e4e05'
    """
    if not text:
        return None
    return hashlib.sha3_256(text.encode('utf-8')).hexdigest()

def string_to_sha3_512(text):
    """
    Given a string 'text', return its sha3_512 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_sha3_512('Hello world') == '8dd9d25e4b975d6d021f819266113f7c43d5415040a3a77b26e8d903176c42a5e61ad27d5d182100b056c06c799f7e7e7e0e03f7e'
    """
    if not text:
        return None
    return hashlib.sha3