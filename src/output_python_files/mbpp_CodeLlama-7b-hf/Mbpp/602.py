"""
Write a python function to find the first repeated character in a given string.
assert first_repeated_char("abcabc") == "a"
"""


def first_repeated_char(string):
    """
    >>> first_repeated_char("abcabc")
    'a'
    >>> first_repeated_char("abca")
    'a'
    >>> first_repeated_char("abc")
    'None'
    """
    for i in range(len(string)):
        if string.count(string[i]) > 1:
            return string[i]
    return "None"


if __name__ == "__main__":
    import doctest

    doctest.testmod()
