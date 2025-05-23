from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    if not numbers:
        return []
    return numbers[:1] + [delimeter] + numbers[1:] if len(numbers) > 1 else numbers


if __name__ == "__main__":
    import doctest

    doctest.testmod()