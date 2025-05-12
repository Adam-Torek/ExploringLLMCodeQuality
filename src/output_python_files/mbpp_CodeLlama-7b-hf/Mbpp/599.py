"""
Write a function to find sum and average of first n natural numbers.
assert sum_average(10)==(55, 5.5)
"""


def sum_average(n):
    """
    >>> sum_average(10)
    (55, 5.5)
    """
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum, sum / n


if __name__ == "__main__":
    import doctest

    doctest.testmod()