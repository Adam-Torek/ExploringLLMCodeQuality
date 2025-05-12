def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """
    import hashlib
    return hashlib.md5(text.encode('utf-8')).hexdigest()

def md5_to_string(md5):
    """
    Given an md5 hash string, return its string equivalent.
    If 'md5' is None, return None.

    >>> md5_to_string('3e25960a79dbc69b674cd4ec67a72c62') == 'Hello world'
    """
    import hashlib
    return hashlib.md5(md5.encode('utf-8')).hexdigest()

def string_to_sha256(text):
    """
    Given a string 'text', return its sha256 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_sha256('Hello world') == 'a94a8fe5ccb19ba61c4c0873d391e987982fbbd3'
    """
    import hashlib
    return hashlib.sha256(text.encode('utf-8')).hexdigest()

def sha256_to_string(sha256):
    """
    Given a sha256 hash string, return its string equivalent.
    If 'sha256' is None, return None.

    >>> sha256_to_string('a94a8fe5ccb19ba61c4c0873d391e987982fbbd3') == 'Hello world'
    """
    import hashlib
    return hashlib.sha256(sha256.encode('utf-8')).hexdigest()

def string_to_sha1(text):
    """
    Given a string 'text', return its sha1 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_sha1('Hello world') == 'a94a8fe5ccb19ba61c4c0873d391e987982fbbd3'
    """
    import hashlib
    return hashlib.sha1(text.encode('utf-8')).hexdigest()

def sha1_to_string(sha1):
    """
    Given a sha1 hash string, return its string equivalent.
    If 'sha1' is None, return None.

    >>> sha1_to_string('a94a8fe5ccb19ba61c4c0873d391e987982fbbd3') == 'Hello world'
    """
    import hashlib
    return hashlib.sha1(sha1.encode('utf-8')).hexdigest()

def string_to_sha2(text):
    """
    Given a string 'text', return its sha2 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_sha2('Hello world') == 'a94a8fe5ccb19ba61c4c0873d391e987982fbbd3'
    """
    import hashlib
    return hashlib.sha2(text.encode('utf-8')).hexdigest()

def sha2_to_string(sha2):
    """
    Given a sha2 hash string, return its string equivalent.
    If 'sha2' is None, return None.

    >>> sha2_to_string('a94a8fe5ccb19ba61c4c0873d391e987982fbbd3') == 'Hello world'
    """
    import hashlib
    return hashlib.sha2(sha2.encode('utf-8')).hexdigest()

def string_