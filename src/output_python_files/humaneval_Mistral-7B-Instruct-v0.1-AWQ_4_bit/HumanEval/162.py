def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """
    import hashlib
    return hashlib.md5(text.encode()).hexdigest()

def md5_to_string(md5):
    """
    Given an md5 hash string, return its string equivalent.
    If 'md5' is None, return None.

    >>> md5_to_string('3e25960a79dbc69b674cd4ec67a72c62') == 'Hello world'
    """
    import hashlib
    return hashlib.md5(md5.encode()).hexdigest()

def string_to_sha256(text):
    """
    Given a string 'text', return its sha256 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_sha256('Hello world') == 'a94a8fe5ccb19ba61c4c0873d391e987982fbbd3'
    """
    import hashlib
    return hashlib.sha256(text.encode()).hexdigest()

def sha256_to_string(sha256):
    """
    Given a sha256 hash string, return its string equivalent.
    If 'sha256' is None, return None.

    >>> sha256_to_string('a94a8fe5ccb19ba61c4c0873d391e987982fbbd3') == 'Hello world'
    """
    import hashlib
    return hashlib.sha256(sha256.encode()).hexdigest()

def string_to_sha512(text):
    """
    Given a string 'text', return its sha512 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_sha512('Hello world') == '6e94a8fe5ccb19ba61c4c0873d391e987982fbbd3'
    """
    import hashlib
    return hashlib.sha512(text.encode()).hexdigest()

def sha512_to_string(sha512):
    """
    Given a sha512 hash string, return its string equivalent.
    If 'sha512' is None, return None.

    >>> sha512_to_string('6e94a8fe5ccb19ba61c4c0873d391e987982fbbd3') == 'Hello world'
    """
    import hashlib
    return hashlib.sha512(sha512.encode()).hexdigest()

def string_to_sha1(text):
    """
    Given a string 'text', return its sha1 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_sha1('Hello world') == 'a94a8fe5ccb19ba61c4c0873d391e987982fbbd3'
    """
    import hashlib
    return hashlib.