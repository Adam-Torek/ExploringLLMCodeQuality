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


def mean_absolute_percentage_error(y_true: List[float], y_pred: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Percentage
    Error around the mean of this dataset.
    Mean Absolute Percentage Error is the average absolute difference between
    each element and a centerpoint (mean in this case) expressed as a percentage
    of the centerpoint:
    MAPE = average | x - x_mean | / x_mean
    >>> mean_absolute_percentage_error([1.0, 2.0, 3.0, 4.0], [1.0, 2.0, 3.0, 4.0])
    0.0
    >>> mean_absolute_percentage_error([1.0, 2.0, 3.0, 4.0], [1.0, 2.0, 3.0, 4.1])
    0.1
    """
    return sum(abs(x - y) / y for x, y in zip(y_true, y_pred)) / len(y_true)


def mean_squared_error(y_true: List[float], y_pred: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Squared Error around
    the mean of this dataset.
    Mean Squared Error is the average squared difference between each element
    and a centerpoint (mean in this case):
    MSE = average (x - x_mean)^2
    >>> mean_squared_error([1.0, 2.0, 3.0, 4.0], [1.0, 2.0, 3.0, 4.0])
    0.0
    >>> mean_squared_error([1.0, 2.0, 3.0, 4.0], [1.0, 2.0, 3.0, 4.1])
    0.01
    """
    return sum((x - y) ** 2 for x, y in zip(y_true, y_pred)) / len(y_true)


def mean_squared_logarithmic_error(y_true: List[float], y_pred: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Squared Logarithmic
    Error around the mean of this dataset.
    Mean Squared Logarithmic Error is the average squared difference between
    each element and a centerpoint (mean in this case) expressed as a logarithm:
    MSLE = average (log(x) - log(x_mean))^2
    >>> mean_squared_logarithmic_error([1.0, 2.0, 3.0, 4.0], [1.0, 2.0, 3.0, 4.0])
    0.0
    >>> mean_squared_logarithmic_error([1.0, 2.0, 3.0, 4.0], [1.0, 2.0, 3.0, 4.1])
    0.0001
    """
    return sum((log(x) - log(y)) ** 2 for x, y in zip(y_true, y_pred)) / len(y_true)


def median_absolute_error(y_true: List[float], y_pred: List[float]) -> float:
    """ For a given list of input numbers, calculate Median Absolute Error
    around the median of this dataset.
    Median Absolute Error is the median of the absolute difference between each
    element and a centerpoint (