def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """
    if text == '':
        return None
    else:
        return hashlib.md5(text.encode()).hexdigest()


def string_to_sha1(text):
    """
    Given a string 'text', return its sha1 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_sha1('Hello world') == '2ef7bde608ce5404e97d5f042f95f897421e92e0'
    """
    if text == '':
        return None
    else:
        return hashlib.sha1(text.encode()).hexdigest()


def string_to_sha256(text):
    """
    Given a string 'text', return its sha256 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_sha256('Hello world') == 'b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9'
    """
    if text == '':
        return None
    else:
        return hashlib.sha256(text.encode()).hexdigest()


def string_to_sha512(text):
    """
    Given a string 'text', return its sha512 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_sha512('Hello world') == 'ddaf35a193617abacc417349ae20413112e6fa4e89a97ea20a9eeee64b55d39a2192992a274fc1a836ba3c23a3feebbd454d4423643ce80e2a9ac94fa54ca49f'
    """
    if text == '':
        return None
    else:
        return hashlib.sha512(text.encode()).hexdigest()


def string_to_sha3_256(text):
    """
    Given a string 'text', return its sha3_256 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_sha3_256('Hello world') == '4e1606d43e9758b2485881c978b2a5f539726241388996532507e1036139375e'
    """
    if text == '':
        return None
    else:
        return hashlib.sha3_256(text.encode()).hexdigest()


def string_to_sha3_512(text):
    """
    Given a string 'text', return its sha3_512 hash equivalent string.
    If 'text' is an empty string, return None.

    >>>