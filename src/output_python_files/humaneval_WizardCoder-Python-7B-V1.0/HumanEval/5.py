from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    result = []
    for i in range(len(numbers)):
        if i % 2 == 0:
            result.append(numbers[i])
        else:
            result.append(numbers[i])
            result.append(delimeter)
    return result[:-1]

if __name__ == "__main__":
    import doctest
    doctest.testmod()