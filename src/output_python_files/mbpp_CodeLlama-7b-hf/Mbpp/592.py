"""
Write a python function to find the sum of the product of consecutive binomial co-efficients.
assert sum_Of_product(3) == 15
"""


def sum_Of_product(n):
    """
    >>> sum_Of_product(3)
    15
    """
    return sum(binomial_coefficient(n, i) * binomial_coefficient(n, i + 1) for i in range(n - 1))


def binomial_coefficient(n, k):
    """
    >>> binomial_coefficient(3, 2)
    3
    """
    return factorial(n) // (factorial(k) * factorial(n - k))


def factorial(n):
    """
    >>> factorial(3)
    6
    """
    if n == 0:
        return 1
    return n * factorial(n - 1)


if __name__ == "__main__":
    import doctest

    doctest.testmod()