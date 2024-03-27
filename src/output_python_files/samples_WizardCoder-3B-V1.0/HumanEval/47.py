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
    [3]
    >>> mode([-10, 4, 6, 1000, 10, 20])
    [10, 20]
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
    >>> correlation([1, 2, 3], [4, 5, 6])
    0.8
    >>> correlation([1, 2, 3], [4, 5, 6, 7])
    0.9
    """

def pearson_correlation(x: list, y: list):
    """Return Pearson correlation coefficient between two lists x and y.
    >>> pearson_correlation([1, 2, 3], [4, 5, 6])
    0.8
    >>> pearson_correlation([1, 2, 3], [4, 5, 6, 7])
    0.9
    """

def spearman_correlation(x: list, y: list):
    """Return Spearman correlation coefficient between two lists x and y.
    >>> spearman_correlation([1, 2, 3], [4, 5, 6])
    0.8
    >>> spearman_correlation([1, 2, 3], [4, 5, 6, 7])
    0.9
    """

def z_score(x: float, mean: float, std_dev: float):
    """Return z-score of x with respect to mean and standard deviation.
    >>> z_score(3, 2, 1)
    1.6448536269515367
    """

def t_score(x: float, mean: float, std_dev: float):
    """Return t-score of x with respect to mean and standard deviation.
    >>> t_score(3, 2, 1)
    2.185039863261518
    """

def chi_square_test(x: list, y: list):
    """Return chi-square test of independence between two lists x and y.
    >>> chi_square_test([1, 2, 3], [4, 5, 6])
    0.0
    >>> chi_square_test([1, 2, 3], [4, 5, 6, 7])
    0.0
    """

def fisher_exact_test(x: list, y: list):
    """Return Fisher exact test of independence between two lists x and y.
    >>> fisher_exact_test([1, 2, 3], [4, 5, 6])
    0.0
    >>> fisher_exact_test([1, 2, 3], [4, 5, 6, 7])
    0.0
    """

def kruskal_wallis_test(x: list,