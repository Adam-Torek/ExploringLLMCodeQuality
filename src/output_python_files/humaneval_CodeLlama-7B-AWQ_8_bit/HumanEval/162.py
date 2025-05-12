def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """
    if text == '':
        return None
    else:
        return hashlib.md5(text.encode('utf-8')).hexdigest()


def string_to_sha1(text):
    """
    Given a string 'text', return its sha1 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_sha1('Hello world') == '2ef7bde608ce5404e97d5f0385611a0b0f154e3b'
    """
    if text == '':
        return None
    else:
        return hashlib.sha1(text.encode('utf-8')).hexdigest()


def string_to_sha256(text):
    """
    Given a string 'text', return its sha256 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_sha256('Hello world') == 'b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9'
    """
    if text == '':
        return None
    else:
        return hashlib.sha256(text.encode('utf-8')).hexdigest()


def string_to_sha512(text):
    """
    Given a string 'text', return its sha512 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_sha512('Hello world') == '4e16b08f03926463e3197cd7e820e44f58f24dc4186711e4be3d822377eda89667c8f607bea4977306d27a1569b30a319'
    """
    if text == '':
        return None
    else:
        return hashlib.sha512(text.encode('utf-8')).hexdigest()


def string_to_sha3_256(text):
    """
    Given a string 'text', return its sha3_256 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_sha3_256('Hello world') == '7538f06e9784905db4c0815d57f6949c13f3f92d92258b2297946e6b79831e3c'
    """
    if text == '':
        return None
    else:
        return hashlib.sha3_256(text.encode('utf-8')).hexdigest()


def string_to_sha3_512(text):
    """
    Given a string 'text', return its sha3_512 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_sha3_512('Hello world') == '471732855447758076366585646123413677298688950853824659714916748438525863858362586583000924037804366567362695362326232695658617