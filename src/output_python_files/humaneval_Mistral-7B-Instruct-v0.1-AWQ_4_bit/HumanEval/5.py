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
    if len(numbers) == 1:
        return [numbers[0]]
    return [numbers[i] for i in range(len(numbers) - 1)
             if i % 2 == 0 else numbers[i] + [delimeter] + numbers[i + 1]]