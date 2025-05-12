from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
    return any(abs(x - y) < threshold for x, y in pairs(numbers))


def pairs(iterable):
    """ Generate pairs of elements from given iterable.
    >>> list(pairs([1, 2, 3]))
    [(1, 2), (1, 3), (2, 3)]
    """
    return itertools.combinations(iterable, 2)


if __name__ == "__main__":
    import doctest
    doctest.testmod()