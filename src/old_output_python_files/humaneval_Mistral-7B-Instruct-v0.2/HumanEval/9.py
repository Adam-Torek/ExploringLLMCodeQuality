from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    if not numbers:
        return []

    max_num = numbers[0]
    result = [max_num]

    for num in numbers[1:]:
        max_num = max(num, max_num)
        result.append(max_num)

    return result


def rolling_min(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling minimum element found until given moment
    in the sequence.
    >>> rolling_min([1, 2, 3, 2, 3, 4, 2])
    [1, 1, 1, 1, 1, 2, 2]
    """
    if not numbers:
        return []

    min_num = numbers[0]
    result = [min_num]

    for num in numbers[1:]:
        min_num = min(num, min_num)
        result.append(min_num)

    return result


def rolling_sum(numbers: List[int], window_size: int) -> List[int]:
    """ From a given list of integers, generate a list of rolling sums of given window size.
    >>> rolling_sum([1, 2, 3, 4, 5], 2)
    [3, 6, 10]
    """
    if not numbers:
        return []

    window = [0] * window_size
    result = []

    for num in numbers:
        window.pop(0)
        window.append(num)
        result.append(sum(window))

    return result


def rolling_difference(numbers: List[int], window_size: int) -> List[int]:
    """ From a given list of integers, generate a list of rolling differences of given window size.
    >>> rolling_difference([1, 2, 3, 4, 5], 2)
    [1, 1, 2]
    """
    if not numbers:
        return []

    window = [0] * window_size
    result = []

    for num in numbers:
        window.pop(0)
        window.append(num)
        result.append(window[-1] - window[-window_size])

    return result


def rolling_product(numbers: List[int], window_size: int) -> List[int]:
    """ From a given list of integers, generate a list of rolling products of given window size.
    >>> rolling_product([1, 2, 3, 4, 5], 2)
    [2, 6, 12]
    """
    if not numbers:
        return []

    window = [1] * window_size
    result = []

    for num in numbers:
        window.pop(0)
        window.append(num)
        result.append(product(window))

    return result


def product(numbers: List[int]) -> int:
    """ Multiply all given numbers.
    >>> product([1, 2, 3])
    6
    """
    if not numbers:
        return 0

    result = 1
    for num in numbers:
        result *= num

    return result


def rolling_mean(numbers: List[int], window_size: int) -> List[float]:
    """ From a given list of integers, generate a list of rolling means of given window size.
    >>> rolling_mean([1, 2, 3, 4, 5], 2)
    [2.5, 3.5]
    """
    if not numbers:
        return []

    window = [0] * window_size
    result = []

    for num in numbers:
        window.