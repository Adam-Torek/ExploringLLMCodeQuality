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
    from math import mean
    return reduce(lambda a, x: a + abs(x - mean(numbers)), numbers, 0) / len(numbers)


def mean_absolute_percentage_deviation(numbers: List[float]) -> List[float]:
    """ For a given list of input numbers, calculate Mean Absolute Percentage
    Deviation around the mean of this dataset.
    Mean Absolute Percentage Deviation is the average absolute difference
    between each element and a centerpoint (mean in this case) expressed as a
    percentage:
    MAD = average | x - x_mean | / x_mean * 100
    >>> mean_absolute_percentage_deviation([1.0, 2.0, 3.0, 4.0])
    [33.33333333333333, 33.33333333333333, 33.33333333333333, 33.33333333333333]
    """
    from functools import reduce
    from math import mean
    return reduce(lambda a, x: a + abs(x - mean(numbers)) / mean(numbers) * 100, numbers, 0) / len(numbers)