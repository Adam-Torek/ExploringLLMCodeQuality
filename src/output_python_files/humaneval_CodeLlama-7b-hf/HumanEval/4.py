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
    return sum(abs(x - mean(numbers)) for x in numbers) / len(numbers)


def mean(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate the mean of this dataset.
    >>> mean([1.0, 2.0, 3.0, 4.0])
    2.5
    """
    return sum(numbers) / len(numbers)


def median(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate the median of this dataset.
    >>> median([1.0, 2.0, 3.0, 4.0])
    2.5
    """
    numbers = sorted(numbers)
    if len(numbers) % 2 == 0:
        return (numbers[len(numbers) // 2] + numbers[len(numbers) // 2 - 1]) / 2
    else:
        return numbers[len(numbers) // 2]


def mode(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate the mode of this dataset.
    >>> mode([1.0, 2.0, 3.0, 4.0])
    2.0
    """
    numbers = sorted(numbers)
    counts = {}
    for number in numbers:
        if number in counts:
            counts[number] += 1
        else:
            counts[number] = 1
    return max(counts, key=counts.get)


def variance(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate the variance of this dataset.
    >>> variance([1.0, 2.0, 3.0, 4.0])
    1.25
    """
    mean_value = mean(numbers)
    return sum((x - mean_value) ** 2 for x in numbers) / len(numbers)


def standard_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate the standard deviation of this dataset.
    >>> standard_deviation([1.0, 2.0, 3.0, 4.0])
    1.1180339887498949
    """
    return variance(numbers) ** 0.5


def coefficient_of_variation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate the coefficient of variation of this dataset.
    Coefficient of variation is the ratio of the standard deviation to the mean:
    CV = SD / mean
    >>> coefficient_of_variation([1.0, 2.0, 3.0, 4.0])
    0.5
    """
    return standard_deviation(numbers) / mean(numbers)


def skewness(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate the skewness of this dataset.
    Skewness is the third standardized moment about the mean:
    Skewness = (mean(abs(x - x_mean)))^3
    >>> skewness([1.0, 2.0, 3.0, 4.0])
    0.0
    """
    mean_value = mean(numbers)
    return sum(((x - mean_value) ** 3 for x in numbers)) / len(numbers)


def kurtosis(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate the kurtosis of this dataset.
    Kurtosis is the fourth standardized moment about the mean:
    Kurtosis = (mean(abs(x - x_mean)))^4
    >>> kurtosis