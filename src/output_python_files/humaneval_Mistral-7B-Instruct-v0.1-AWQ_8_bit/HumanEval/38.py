def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    # split string into groups of three.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def test_encode_cyclic():
    """
    tests encode_cyclic function.
    """
    assert encode_cyclic("") == ""
    assert encode_cyclic("a") == "a"
    assert encode_cyclic("ab") == "ab"
    assert encode_cyclic("abc") == "abc"
    assert encode_cyclic("abcd") == "abcd"
    assert encode_cyclic("abcd") == "abcd"
    assert encode_cyclic("abcd") == "abcd"
    assert encode_cyclic("abcd") == "abcd"
    assert encode_cyclic("abcd") == "abcd"
    assert encode_cyclic("abcd") == "abcd"
    assert encode_cyclic("abcd") == "abcd"
    assert encode_cyclic("abcd") == "abcd"
    assert encode_cyclic("abcd") == "abcd"
    assert encode_cyclic("abcd") == "abcd"
    assert encode_cyclic("abcd") == "abcd"
    assert encode_cyclic("abcd") == "abcd"
    assert encode_cyclic("abcd") == "abcd"
    assert encode_cyclic("abcd") == "abcd"
    assert encode_cyclic("abcd") == "abcd"
    assert encode_cyclic("abcd") == "abcd"
    assert encode_cyclic("abcd") == "abcd"
    assert encode_cyclic("abcd") == "abcd"
    assert encode_cyclic("abcd") == "abcd"
    assert encode_cyclic("abcd") == "abcd"
    assert encode_cyclic("abcd") == "abcd"
    assert encode_cyclic("abcd") == "abcd"
    assert encode_cyclic("abcd") == "abcd"
    assert encode_cyclic("abcd") == "abcd"
    assert encode_cyclic("abcd") == "abcd"
    assert encode_cyclic("abcd") == "abcd"
    assert encode_cyclic("abcd") == "abcd"
    assert encode_cyclic("abcd") == "abcd"
    assert encode_cyclic("abcd") == "abcd"
    assert encode_cyclic("abcd") == "abcd"
    assert encode_cyclic("abcd") == "abcd"
    assert encode_cyclic("abcd") == "abcd"
    assert encode_cyclic("abcd") == "abcd"
    assert encode_cyclic("abcd") == "abcd"
    assert encode_cyclic("abcd") == "abcd"
    assert encode_cyclic("abcd") == "abcd"
    assert encode_cyclic("abcd") == "abcd"
    assert encode_cyclic("abcd") == "abcd"
    assert encode_cyclic("abcd") == "abcd"
    assert encode_cyclic("abcd") == "abcd"
    assert encode_cyclic("abcd