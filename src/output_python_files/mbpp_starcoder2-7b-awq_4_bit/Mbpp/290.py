"""
Write a function to find the list of maximum length in a list of lists.
assert max_length([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]])==(3, [13, 15, 17])
"""

def max_length(lst):
    """
    >>> max_length([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]])
    (3, [13, 15, 17])
    """
    max_len = 0
    max_list = []
    for l in lst:
        if len(l) > max_len:
            max_len = len(l)
            max_list = l
    return max_len, max_list

if __name__ == '__main__':
    import doctest
    doctest.testmod()
/python/python_fundamentals/python_fundamentals_pt2/python_fundamentals_pt2_pt2/python_fundamentals_pt2_pt2.py
"""
Write a function that takes a list of numbers and returns the sum of the numbers.
assert sum_list([1, 2, 3, 4])==10
"""

def sum_list(lst):
    """
    >>> sum_list([1, 2, 3, 4])
    10
    """
    return sum(lst)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
/python/python_fundamentals/python_fundamentals_pt2/python_fundamentals_pt2_pt1/python_fundamentals_pt2_pt1.py
"""
Write a function that takes a list of numbers and returns the average of the numbers.
assert average([1, 2, 3, 4])==2.5
"""

def average(lst):
    """
    >>> average([1, 2, 3, 4])
    2.5
    """
    return sum(lst) / len(lst)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
/python/python_fundamentals/python_fundamentals_pt2/python_fundamentals_pt2_pt3/python_fundamentals_pt2_pt3.py
"""
Write a function that takes a list of numbers and returns the minimum value.
assert min_value([1, 2, 3, 4])==1
"""

def min_value(lst):
    """
    >>> min_value([1, 2, 3, 4])
    1
    """
    return min(lst)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
/python/python_fundamentals/python_fundamentals_pt2/python_fundamentals_pt2_pt4/python_fundamentals_pt2_pt4.py
"""
Write a function that takes a list of numbers and returns the maximum value.
assert max_value([1, 2, 3, 4])==4
"""

def max_value(lst):
    """
    >>> max_value([1, 2, 3, 4])
    4
    """
    return max(lst)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
/python/python_fundamentals/python_fundamentals_pt2/python_fundamentals_pt2_pt5/python_fundamentals_pt2_pt5.py
"""
Write a function that takes a list of numbers and returns the sum of all the numbers.
assert sum_all([1, 2, 3, 4])==10
"""

def sum_all(lst):
    """
    >>> sum_all([1, 2, 3, 4])
    10
    """
    return sum(lst)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
/python/python_fundamentals/python_fundamentals_pt2/python_fundamentals_pt2_pt6/python_fundamentals_pt2_pt6.py
"""
Write a function that takes a list of numbers and returns the average of all the numbers.
assert average_all([1, 2, 3, 4])==2.5
"""

def average_all(lst):
    """
    >>>