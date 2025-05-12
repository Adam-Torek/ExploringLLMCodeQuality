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

    >>> string_to_sha256('Hello world') == 'a591a6d40bf4204c105ee06bb2e2de0a738f4b3620475e80370e7445f5a89bc1d4a'
    """
    if not text:
        return None
    return hashlib.sha256(text.encode('utf-8')).hexdigest()



def string_to_sha512(text):
    """
    Given a string 'text', return its sha512 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_sha512('Hello world') == '8cc16f7f37a23f0f233a2e643b6d615b26575a6d4b3f7f1f0a6e2b8490699a0109c71f7d1d1dad0e94'
    """
    if not text:
        return None
    return hashlib.sha512(text.encode('utf-8')).hexdigest()



def string_to_sha3_512(text):
    """
    Given a string 'text', return its sha3_512 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_sha3_512('Hello world') == '94a6883461048766f75f2c8e7b1d26d7d9d0677b50a91e7f9b003279f1c1045d8d8c8d10703c3c9d03f0d7'
    """
    if not text:
        return None
    return hashlib.sha3_512(text.encode('utf-8')).hexdigest()



def string_to_sha3_384(text):
    """
    Given a string 'text', return its sha3_384 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_sha3_384('Hello world') == '94a6883461048766f75f2c8e7b1d26d7d9d0677b50a91e7f9b003279f1c1045d8d8c8d10703c3c9d03f0d7'
    """
    if not text:
        return None
    return hashlib.sha3_384(text.encode('utf-8')).hexdigest()



def string_to_sha3_256(text):
    """
    Given a string 'text', return its sha3_256 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_sha3_256('Hello world') == '94a6883461048766f75f2c8e7b1d26d7d9d0677b50a91e7f9b003279f1c1