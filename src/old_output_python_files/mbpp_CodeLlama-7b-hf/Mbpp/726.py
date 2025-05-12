"""
Write a function that takes as input a tuple of numbers (t_1,...,t_{N+1}) and returns a tuple of length N where the i-th element of the tuple is equal to t_i * t_{i+1}.
assert multiply_elements((1, 5, 7, 8, 10)) == (5, 35, 56, 80)
"""


def multiply_elements(t):
    """
    >>> multiply_elements((1, 5, 7, 8, 10))
    (5, 35, 56, 80)
    >>> multiply_elements((1, 2, 3, 4, 5))
    (2, 6, 12, 20)
    >>> multiply_elements((1, 2, 3))
    (2, 6)
    >>> multiply_elements((1, 2))
    (2,)
    >>> multiply_elements((1))
    (1,)
    >>> multiply_elements(())
    ()
    """
    if len(t) == 0:
        return ()
    elif len(t) == 1:
        return (t[0],)
    else:
        return (t[0] * t[1],) + multiply_elements(t[1:])


if __name__ == "__main__":
    import doctest

    doctest.testmod()
