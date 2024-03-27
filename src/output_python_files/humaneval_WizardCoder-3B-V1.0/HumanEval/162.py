def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """

#     if not text:
#         return None

    import hashlib
    md5 = hashlib.md5()
    md5.update(text.encode('utf-8'))
    return md5.hexdigest()

# Test cases
print(string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62')
print(string_to_md5('') is None)<|endoftext|>