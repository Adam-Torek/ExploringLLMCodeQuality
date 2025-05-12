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

    >>> string_to_sha256('Hello world') == 'a591a6d40bf4204c105ee06bb2e30a253f866f8fc917b9e439b25e014e75d6e8793e522d4622c6f66f738b80dbe6d2'
    """
    if not text:
        return None
    return hashlib.sha256(text.encode('utf-8')).hexdigest()



def string_to_sha512(text):
    """
    Given a string 'text', return its sha512 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_sha512('Hello world') == 'cf83e1357eefb8bdf15428505d1d831c51cfa4b26f0c7f78efc9b8d4d14d75b263f7c9a8f5549e27afbebaef1a07c7d'
    """
    if not text:
        return None
    return hashlib.sha512(text.encode('utf-8')).hexdigest()



def string_to_sha3_512(text):
    """
    Given a string 'text', return its sha3_512 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_sha3_512('Hello world') == '8d5a614c37c9642899486f4c8a545b38d05c0d9139f74d3717d3852298739f7c0d4c7d5d87876d8994872d088d16d8d1d510d41f475f9'
    """
    if not text:
        return None
    return hashlib.sha3_512(text.encode('utf-8')).hexdigest()



def string_to_sha3_384(text):
    """
    Given a string 'text', return its sha3_384 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_sha3_384('Hello world') == 'a1f6d8a292c7e4c4e8f4c3426d58e2b03e24e988731e5414f2c30d0e1