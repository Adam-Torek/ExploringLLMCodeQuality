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


def mean_absolute_percentage_error(actual: List[float], predicted: List[float]) -> float:
    """ For a given list of actual and predicted values, calculate Mean Absolute
    Percentage Error (MAPE).
    MAPE = average | (actual - predicted) / actual |
    >>> mean_absolute_percentage_error([1.0, 2.0, 3.0, 4.0], [1.0, 2.0, 3.0, 4.0])
    0.0
    """
    return sum(abs((x - y) / x) for x, y in zip(actual, predicted)) / len(actual)


def mean_squared_error(actual: List[float], predicted: List[float]) -> float:
    """ For a given list of actual and predicted values, calculate Mean Squared
    Error (MSE).
    MSE = average (actual - predicted)^2
    >>> mean_squared_error([1.0, 2.0, 3.0, 4.0], [1.0, 2.0, 3.0, 4.0])
    0.0
    """
    return sum((x - y) ** 2 for x, y in zip(actual, predicted)) / len(actual)


def mean_squared_logarithmic_error(actual: List[float], predicted: List[float]) -> float:
    """ For a given list of actual and predicted values, calculate Mean Squared
    Logarithmic Error (MSLE).
    MSLE = average | log(actual) - log(predicted) |
    >>> mean_squared_logarithmic_error([1.0, 2.0, 3.0, 4.0], [1.0, 2.0, 3.0, 4.0])
    0.0
    """
    return sum(abs(math.log(x) - math.log(y)) for x, y in zip(actual, predicted)) / len(actual)


def median_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Median Absolute Deviation
    around the median of this dataset.
    Median Absolute Deviation is the median of the absolute differences between
    each element and a centerpoint (median in this case):
    MAD = median | x - x_median |
    >>> median_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    1.0
    """
    median = median(numbers)
    return median(abs(x - median) for x in numbers)


def median_absolute_percentage_error(actual: List[float], predicted: List[float]) -> float:
    """ For a given list of actual and predicted values, calculate Median Absolute
    Percentage Error (MAPE).
    MAPE = median | (actual - predicted) / actual |
    >>> median_absolute_percentage_error([1.0, 2.0, 3.0, 4.0], [1.0, 2.0, 3.0, 4.0])
    0.0
    """
    return median(abs((x - y) / x) for x, y in zip(actual, predicted))


def median_squared_error(actual: List[float], predicted: List[float]) -> float:
    """ For a given list of actual and predicted values, calculate Median Squared
    Error (MSE).
    MSE = median (actual - predicted)^2
    >>> median_squared_error([1.0, 2.0,