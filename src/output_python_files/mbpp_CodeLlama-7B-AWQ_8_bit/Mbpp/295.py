"""
Write a function to return the sum of all divisors of a number.
assert sum_div(8)==7
"""


def sum_div(n):
    """
    >>> sum_div(8)
    7
    >>> sum_div(12)
    12
    >>> sum_div(10)
    26
    >>> sum_div(1)
    1
    >>> sum_div(0)
    0
    >>> sum_div(-1)
    0
    """
    if n < 0:
        return 0
    if n == 0:
        return 0
    if n == 1:
        return 1
    sum = 1
    for i in range(2, n):
        if n % i == 0:
            sum += i
    return sum


if __name__ == "__main__":
    import doctest

    doctest.testmod()