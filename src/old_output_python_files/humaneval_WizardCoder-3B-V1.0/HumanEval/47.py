def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """

def mode(l: list):
    """Return mode of elements in the list l.
    >>> mode([3, 1, 2, 4, 5])
    [1]
    >>> mode([-10, 4, 6, 1000, 10, 20])
    [10]
    """

def mean(l: list):
    """Return mean of elements in the list l.
    >>> mean([3, 1, 2, 4, 5])
    3.0
    >>> mean([-10, 4, 6, 1000, 10, 20])
    10.0
    """

def variance(l: list):
    """Return variance of elements in the list l.
    >>> variance([3, 1, 2, 4, 5])
    2.0
    >>> variance([-10, 4, 6, 1000, 10, 20])
    10000.0
    """

def standard_deviation(l: list):
    """Return standard deviation of elements in the list l.
    >>> standard_deviation([3, 1, 2, 4, 5])
    1.0
    >>> standard_deviation([-10, 4, 6, 1000, 10, 20])
    100.0
    """

def correlation(x: list, y: list):
    """Return correlation coefficient between two lists x and y.
    >>> correlation([3, 1, 2, 4, 5], [1, 2, 3, 4, 5])
    1.0
    >>> correlation([1, 2, 3, 4, 5], [10, 20, 30, 40, 50])
    -0.5
    """

def pearson_correlation(x: list, y: list):
    """Return Pearson correlation coefficient between two lists x and y.
    >>> pearson_correlation([3, 1, 2, 4, 5], [1, 2, 3, 4, 5])
    1.0
    >>> pearson_correlation([1, 2, 3, 4, 5], [10, 20, 30, 40, 50])
    -0.5
    """

def spearman_correlation(x: list, y: list):
    """Return Spearman correlation coefficient between two lists x and y.
    >>> spearman_correlation([3, 1, 2, 4, 5], [1, 2, 3, 4, 5])
    1.0
    >>> spearman_correlation([1, 2, 3, 4, 5], [10, 20, 30, 40, 50])
    -0.5
    """

def covariance(x: list, y: list):
    """Return covariance between two lists x and y.
    >>> covariance([3, 1, 2, 4, 5], [1, 2, 3, 4, 5])
    0.0
    >>> covariance([1, 2, 3, 4, 5], [10, 20, 30, 40, 50])
    0.0
    """

def pearson_covariance(x: list, y: list):
    """Return Pearson covariance between two lists x and y.
    >>> pearson_covariance([3, 1, 2, 4, 5], [1, 2, 3, 4, 5])
    0.0
    >>> pearson_covariance([1, 2, 3, 4, 5], [10, 20, 30, 40, 50])
    0.0
    """

def spearman_covariance(x: list, y: list):
    """Return Spearman covariance between two lists x and y.
    >>> spearman_covariance([3, 1, 2, 4,