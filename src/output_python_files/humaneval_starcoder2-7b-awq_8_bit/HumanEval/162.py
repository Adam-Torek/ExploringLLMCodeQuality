def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """

def md5_to_string(md5):
    """
    Given an md5 hash equivalent string'md5', return its string equivalent.
    If'md5' is an empty string, return None.

    >>> md5_to_string('3e25960a79dbc69b674cd4ec67a72c62') == 'Hello world'
    """

def md5_to_hex(md5):
    """
    Given an md5 hash equivalent string'md5', return its hex equivalent string.
    If'md5' is an empty string, return None.

    >>> md5_to_hex('3e25960a79dbc69b674cd4ec67a72c62') == '3e25960a79dbc69b674cd4ec67a72c62'
    """

def hex_to_md5(hex):
    """
    Given an md5 hash equivalent hex string 'hex', return its string equivalent.
    If 'hex' is an empty string, return None.

    >>> hex_to_md5('3e25960a79dbc69b674cd4ec67a72c62') == '3e25960a79dbc69b674cd4ec67a72c62'
    """

def md5_to_base64(md5):
    """
    Given an md5 hash equivalent string'md5', return its base64 equivalent string.
    If'md5' is an empty string, return None.

    >>> md5_to_base64('3e25960a79dbc69b674cd4ec67a72c62') == 'SGVsbG8gV29ybGQ='
    """

def base64_to_md5(base64):
    """
    Given an md5 hash equivalent base64 string 'base64', return its string equivalent.
    If 'base64' is an empty string, return None.

    >>> base64_to_md5('SGVsbG8gV29ybGQ=') == '3e25960a79dbc69b674cd4ec67a72c62'
    """

def md5_to_base64_url(md5):
    """
    Given an md5 hash equivalent string'md5', return its base64 url equivalent string.
    If'md5' is an empty string, return None.

    >>> md5_to_base64_url('3e25960a79dbc69b674cd4ec67a72c62') == 'SGVsbG8gV29ybGQ'
    """

def base64_url_to_md5(base64_url):
    """
    Given an md5 hash equivalent base64 url string 'base64_url', return its string equivalent.
    If 'base64_url' is an empty string, return None.

    >>> base64_url_to_md5('SGVsbG8gV29ybGQ') == '3e25960a79dbc69b674cd4ec67a72c62'
    """

def md5_to_base64_url_safe(md5):
    """
    Given an md5 hash equivalent string'md5', return its base64 url safe equivalent string.
    If'md5' is an empty string, return None.

    >>> md5_to_base64_url_safe('3e25960a79dbc69b674cd4ec67a72c62') == 'SGVsbG8gV29ybGQ'
    """

def base64_url_safe_to_md5(base64_url_safe):
    """
    Given an md5 hash equivalent base64 url safe string 'base64_url_safe