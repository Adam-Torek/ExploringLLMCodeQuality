def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """
    import hashlib
    if not text:
        return None
    m = hashlib.md5()
    m.update(text.encode())
    return m.hexdigest()

def main():
    """
    Test the string_to_md5 function.
    """
    print(string_to_md5('Hello world'))
    print(string_to_md5(''))
    print(string_to_md5('The quick brown fox jumps over the lazy dog'))

if __name__ == '__main__':
    main()