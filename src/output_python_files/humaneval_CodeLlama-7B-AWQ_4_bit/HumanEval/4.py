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


def median_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Median Absolute Deviation
    around the median of this dataset.
    Median Absolute Deviation is the average absolute difference between each
    element and a centerpoint (median in this case):
    MAD = average | x - x_median |
    >>> median_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    1.0
    """
    median = median(numbers)
    return sum(abs(x - median) for x in numbers) / len(numbers)


def mean_absolute_percentage_error(y_true: List[float], y_pred: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Percentage
    Error around the mean of this dataset.
    Mean Absolute Percentage Error is the average absolute difference between
    each element and a centerpoint (mean in this case) divided by the centerpoint:
    MAPE = average | x - x_mean | / x_mean
    >>> mean_absolute_percentage_error([1.0, 2.0, 3.0, 4.0], [1.0, 2.0, 3.0, 4.0])
    0.0
    """
    return sum(abs(x - y) / y for x, y in zip(y_true, y_pred)) / len(y_true)


def median_absolute_percentage_error(y_true: List[float], y_pred: List[float]) -> float:
    """ For a given list of input numbers, calculate Median Absolute Percentage
    Error around the median of this dataset.
    Median Absolute Percentage Error is the average absolute difference between
    each element and a centerpoint (median in this case) divided by the centerpoint:
    MAPE = average | x - x_median | / x_median
    >>> median_absolute_percentage_error([1.0, 2.0, 3.0, 4.0], [1.0, 2.0, 3.0, 4.0])
    0.0
    """
    median = median(y_true)
    return sum(abs(x - y) / y for x, y in zip(y_true, y_pred)) / len(y_true)


def mean_squared_error(y_true: List[float], y_pred: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Squared Error around
    the mean of this dataset.
    Mean Squared Error is the average squared difference between each element
    and a centerpoint (mean in this case):
    MSE = average (x - x_mean)^2
    >>> mean_squared_error([1.0, 2.0, 3.0, 4.0], [1.0, 2.0, 3.0, 4.0])
    0.0
    """
    return sum((x - y) ** 2 for x, y in zip(y_true, y_pred)) / len(y_true)


def mean_squared_logarithmic_error(y_true: List[float], y_pred: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Squared Logarithmic
    Error around the mean of this dataset.
    Mean Squared Logarithmic Error is the average squared difference between
    each element and a centerpoint (mean in this case):
    MSE =