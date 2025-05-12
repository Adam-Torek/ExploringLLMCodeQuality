"""
Write a python function to find the first repeated character in a given string.
assert first_repeated_char("abcabc") == "a"
"""


def first_repeated_char(string):
    """
    :param string: str
    :return: str
    """
    return min(set(string), key=string.count)


if __name__ == '__main__':
    print(first_repeated_char("abcabc"))
    print(first_repeated_char("abca"))
    print(first_repeated_char("abc"))
    print(first_repeated_char("abcaa"))
    print(first_repeated_char("abcabca"))
    print(first_repeated_char("abcabcaa"))
    print(first_repeated_char("abcabcaaa"))
    print(first_repeated_char("abcabcaaaa"))
    print(first_repeated_char("abcabcaaaaa"))
    print(first_repeated_char("abcabcaaaaaa"))
    print(first_repeated_char("abcabcaaaaaaa"))
    print(first_repeated_char("abcabcaaaaaaaa"))
    print(first_repeated_char("abcabcaaaaaaaaa"))
    print(first_repeated_char("abcabcaaaaaaaaaa"))
    print(first_repeated_char("abcabcaaaaaaaaaaa"))
    print(first_repeated_char("abcabcaaaaaaaaaaaa"))
    print(first_repeated_char("abcabcaaaaaaaaaaaaa"))
    print(first_repeated_char("abcabcaaaaaaaaaaaaaa"))
    print(first_repeated_char("abcabcaaaaaaaaaaaaaaa"))
    print(first_repeated_char("abcabcaaaaaaaaaaaaaaaa"))
    print(first_repeated_char("abcabcaaaaaaaaaaaaaaaaa"))
    print(first_repeated_char("abcabcaaaaaaaaaaaaaaaaaa"))
    print(first_repeated_char("abcabcaaaaaaaaaaaaaaaaaaa"))
    print(first_repeated_char("abcabcaaaaaaaaaaaaaaaaaaaa"))
    print(first_repeated_char("abcabcaaaaaaaaaaaaaaaaaaaaa"))
    print(first_repeated_char("abcabcaaaaaaaaaaaaaaaaaaaaaa"))
    print(first_repeated_char("abcabcaaaaaaaaaaaaaaaaaaaaaaa"))
    print(first_repeated_char("abcabcaaaaaaaaaaaaaaaaaaaaaaaa"))
    print(first_repeated_char("abcabcaaaaaaaaaaaaaaaaaaaaaaaaa"))
    print(first_repeated_char("abcabcaaaaaaaaaaaaaaaaaaaaaaaaaa"))
    print(first_repeated_char("abcabcaaaaaaaaaaaaaaaaaaaaaaaaaaa"))
    print(first_repeated_char("abcabcaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))
    print(first_repeated_char("abcabcaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))
    print(first_repeated_char("abcabcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))
    print(first_repeated_char("abcabcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))
    print(first_repeated_char("abcabcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))
    print(first_repeated_char("abcabcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))
    print(first_repeated_char("abcabcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))
    print(first_repeated_char("abcabcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))
    print(first_repeated_char("abcabcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))
    print(first_repeated_char("abcabcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))
    print(first_repeated_char("abcabcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))
    print(first_repeated_char("abcabcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))
    print(first_repeated_char("abcabcaaaaaaaaaaaaaaaaa