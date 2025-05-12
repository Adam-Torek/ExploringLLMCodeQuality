def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """
    import hashlib
    if not text:
        return None
    return hashlib.md5(text.encode()).hexdigest()

def test_string_to_md5():
    """
    Test the string_to_md5 function.
    """
    assert string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    assert string_to_md5('') is None
    assert string_to_md5('abc') == '906eb0d1f01c81189c172e17c2d79bbf'
    assert string_to_md5('12345') == '5eb6f7b15f960f6ec47e3d32p9ebeee5'
    assert string_to_md5('123456') == '87c36a5afb1c2d5bbf15d5616c8ca932'
    assert string_to_md5('admin') == 'b882d0e151715c51c72d76e917ebd09d'
    assert string_to_md5('password') == '5eb6f7b15f960f6ec47e3d32p9ebeee5'
    assert string_to_md5('12345678') == '94d48d5d6b3041eb0211bde522663e2e'
    assert string_to_md5('1234567890') == '4abd3b3a394b04dc4a261d3e6548b0bb'
    assert string_to_md5('123456789012345') == '6745230c4fe1b6483182efc42623b041'
    assert string_to_md5('123456789012345678901234') == '94d48d5d6b3041eb0211bde522663e2e'
    assert string_to_md5('12345678901234567890123456789012') == '6745230c4fe1b6483182efc42623b041'
    assert string_to_md5('1234567890123456789012345678901234567890') == '4abd3b3a394b04dc4a261d3e6548b0bb'
    assert string_to_md5('1234567890123456789012345678901234567890123456789012345678901234') == '94d48d5d6b3041eb0211bde522663e2e'
    assert string_to_md5('123456789012345678901234567890123456789012345678901234567890123456789012