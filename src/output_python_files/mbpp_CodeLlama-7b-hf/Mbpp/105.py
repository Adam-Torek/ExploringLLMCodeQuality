"""
Write a python function to count true booleans in the given list.
assert count([True,False,True]) == 2
"""


def count(lst):
    """
    >>> count([True,False,True])
    2
    >>> count([True,True,True])
    3
    >>> count([False,False,False])
    0
    """
    return sum(1 for x in lst if x)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
</s>