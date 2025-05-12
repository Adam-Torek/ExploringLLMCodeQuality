"""
Write a python function to count the number of non-empty substrings of a given string.
assert number_of_substrings("abc") == 6
"""


def number_of_substrings(string):
    """
    >>> number_of_substrings("abc")
    6
    >>> number_of_substrings("")
    0
    >>> number_of_substrings("a")
    1
    >>> number_of_substrings("ab")
    3
    >>> number_of_substrings("abcde")
    10
    >>> number_of_substrings("abcdeabcde")
    20
    >>> number_of_substrings("abcdeabcdeabcde")
    30
    >>> number_of_substrings("abcdeabcdeabcdeabcde")
    40
    >>> number_of_substrings("abcdeabcdeabcdeabcdeabcde")
    50
    """
    if not string:
        return 0
    return sum(1 for i in range(len(string)) for j in range(i + 1, len(string) + 1))


if __name__ == "__main__":
    import doctest

    doctest.testmod()