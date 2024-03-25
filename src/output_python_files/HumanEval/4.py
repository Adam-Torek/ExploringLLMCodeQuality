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
    if not numbers:
        return 0.0
    mean = sum(numbers) / len(numbers)
    return sum(abs(x - mean) for x in numbers) / len(numbers)


def median_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Median Absolute Deviation
    around the median of this dataset.
    Median Absolute Deviation is the average absolute difference between each
    element and a centerpoint (median in this case):
    MAD = average | x - x_median |
    >>> median_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    1.0
    """
    if not numbers:
        return 0.0
    median = median_of_numbers(numbers)
    return sum(abs(x - median) for x in numbers) / len(numbers)


def median_of_numbers(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate the median of this dataset.
    >>> median_of_numbers([1.0, 2.0, 3.0, 4.0])
    2.5
    """
    if not numbers:
        return 0.0
    numbers = sorted(numbers)
    if len(numbers) % 2 == 0:
        return (numbers[len(numbers) // 2] + numbers[len(numbers) // 2 - 1]) / 2
    else:
        return numbers[len(numbers) // 2]


def standard_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate the standard deviation of
    this dataset.
    >>> standard_deviation([1.0, 2.0, 3.0, 4.0])
    1.2909944487358056
    """
    if not numbers:
        return 0.0
    mean = sum(numbers) / len(numbers)
    return sum((x - mean) ** 2 for x in numbers) / len(numbers)


def variance(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate the variance of this
    dataset.
    >>> variance([1.0, 2.0, 3.0, 4.0])
    1.25
    """
    if not numbers:
        return 0.0
    mean = sum(numbers) / len(numbers)
    return sum((x - mean) ** 2 for x in numbers) / len(numbers)


def z_score(number: float, mean: float, standard_deviation: float) -> float:
    """ For a given number, calculate the z-score of this number.
    >>> z_score(1.0, 2.0, 1.0)
    -1.0
    """
    return (number - mean) / standard_deviation


def z_score_from_numbers(number: float, numbers: List[float]) -> float:
    """ For a given number, calculate the z-score of this number.
    >>> z_score_from_numbers(1.0, [1.0, 2.0, 3.0, 4.0])
    -1.0
    """
    mean = sum(numbers) / len(numbers)
    standard_deviation = standard_deviation(numbers)
    return z_score(number, mean, standard_deviation)


def z_score_from_dataset(number: float, dataset: str) -> float:
    """ For a given number, calculate the z-score of this number.
    >>> z_score_from_dataset(1