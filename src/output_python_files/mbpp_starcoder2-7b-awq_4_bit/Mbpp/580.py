"""
Write a function to remove uneven elements in the nested mixed tuple.
assert extract_even((4, 5, (7, 6, (2, 4)), 6, 8)) == (4, (6, (2, 4)), 6, 8)
"""

def extract_even(nested_tuple):
    """
    >>> extract_even((4, 5, (7, 6, (2, 4)), 6, 8))
    (4, (6, (2, 4)), 6, 8)
    """
    return tuple(extract_even(item) if isinstance(item, tuple) else item for item in nested_tuple if item % 2 == 0)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
/python/python_fundamentals/python_fundamentals_pt1/python_fundamentals_pt1.py
"""
Python Fundamentals

Python Fundamentals I

"""

# 1.
def print_list(list):
    """
    >>> print_list([1, 2, 3, 4, 5])
    1 2 3 4 5
    """
    print(' '.join(map(str, list)))

# 2.
def print_list_reverse(list):
    """
    >>> print_list_reverse([1, 2, 3, 4, 5])
    5 4 3 2 1
    """
    print(' '.join(map(str, reversed(list))))

# 3.
def print_list_length(list):
    """
    >>> print_list_length([1, 2, 3, 4, 5])
    5
    """
    print(len(list))

# 4.
def print_list_min(list):
    """
    >>> print_list_min([1, 2, 3, 4, 5])
    1
    """
    print(min(list))

# 5.
def print_list_max(list):
    """
    >>> print_list_max([1, 2, 3, 4, 5])
    5
    """
    print(max(list))

# 6.
def print_list_sum(list):
    """
    >>> print_list_sum([1, 2, 3, 4, 5])
    15
    """
    print(sum(list))

# 7.
def print_list_avg(list):
    """
    >>> print_list_avg([1, 2, 3, 4, 5])
    3.0
    """
    print(sum(list) / len(list))

# 8.
def print_list_median(list):
    """
    >>> print_list_median([1, 2, 3, 4, 5])
    3.0
    """
    list.sort()
    if len(list) % 2 == 0:
        print((list[len(list) // 2] + list[len(list) // 2 - 1]) / 2)
    else:
        print(list[len(list) // 2])

# 9.
def print_list_mode(list):
    """
    >>> print_list_mode([1, 2, 3, 4, 5])
    1
    """
    from collections import Counter
    c = Counter(list)
    print(c.most_common(1)[0][0])

# 10.
def print_list_range(list):
    """
    >>> print_list_range([1, 2, 3, 4, 5])
    4
    """
    print(max(list) - min(list))

# 11.
def print_list_variance(list):
    """
    >>> print_list_variance([1, 2, 3, 4, 5])
    2.0
    """
    from statistics import variance
    print(variance(list))

# 12.
def print_list_std_dev(list):
    """
    >>> print_list_std_dev([1, 2, 3, 4, 5])
    1.4142135623730951
    """
    from statistics import stdev
    print(stdev(list))

# 13.
def print_list_sum_of_squares(list):
    """
    >>> print_list_sum_