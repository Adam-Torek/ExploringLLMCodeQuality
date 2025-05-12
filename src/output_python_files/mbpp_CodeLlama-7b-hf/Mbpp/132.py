"""
Write a function to convert a tuple to a string.
assert tup_string(('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's'))==("exercises")
"""


def tup_string(tup):
    """
    >>> tup_string(('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's'))
    'exercises'
    """
    return ''.join(tup)


if __name__ == "__main__":
    import doctest

    doctest.testmod()