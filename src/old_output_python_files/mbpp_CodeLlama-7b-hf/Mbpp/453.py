"""
Write a python function to find the sum of even factors of a number.
assert sumofFactors(18) == 26
"""


def sumofFactors(n):
    """
    >>> sumofFactors(18)
    26
    """
    sum = 0
    for i in range(1, n + 1):
        if n % i == 0:
            if i % 2 == 0:
                sum += i
    return sum


if __name__ == "__main__":
    import doctest

    doctest.testmod()
