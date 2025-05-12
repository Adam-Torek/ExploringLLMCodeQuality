from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    1.0
    """
    from functools import reduce
    from operator import abs
    return reduce(lambda a, x: a + abs(x - mean(numbers)), numbers) / len(numbers)


def mean(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate the mean of this dataset.
    >>> mean([1.0, 2.0, 3.0, 4.0])
    2.5
    """
    return reduce(lambda a, x: a + x, numbers) / len(numbers)


def median(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate the median of this dataset.
    >>> median([1.0, 2.0, 3.0, 4.0])
    2.5
    """
    numbers.sort()
    n = len(numbers)
    if n % 2 == 0:
        return (numbers[n//2 - 1] + numbers[n//2]) / 2
    else:
        return numbers[n//2]


def mode(numbers: List[float]) -> List[float]:
    """ For a given list of input numbers, calculate the mode of this dataset.
    >>> mode([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0])
    [10.0, 9.0, 8.0, 7.0, 6.0, 5.0, 4.0, 3.0, 2.0, 1.0]
    """
    from collections import Counter
    return list(Counter(numbers).most_common(1)[0][0])


def standard_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate the standard deviation of this dataset.
    >>> standard_deviation([1.0, 2.0, 3.0, 4.0])
    1.4142135623730951
    """
    mean = mean(numbers)
    variance = reduce(lambda a, x: a + pow(x - mean, 2), numbers) / len(numbers)
    return variance ** 0.5


def variance(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate the variance of this dataset.
    >>> variance([1.0, 2.0, 3.0, 4.0])
    3.0
    """
    mean = mean(numbers)
    variance = reduce(lambda a, x: a + pow(x - mean, 2), numbers) / len(numbers)
    return variance


def range_of_numbers(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate the range of this dataset.
    >>> range_of_numbers([1.0, 2.0, 3.0, 4.0])
    3.0
    """
    return max(numbers) - min(numbers)


def skewness(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate the skewness of this dataset.
    >>> skewness([1.0, 2.0, 3.0, 4.0])
    0.0
    """
    from functools import reduce
    from operator import sub
    from math import pow
    n = len(numbers)
    m = mean(numbers)
    variance = reduce(lambda a, x: a + pow(