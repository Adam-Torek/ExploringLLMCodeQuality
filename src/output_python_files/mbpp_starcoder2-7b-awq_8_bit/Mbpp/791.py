"""
Write a function to remove tuples from the given tuple.
assert remove_nested((1, 5, 7, (4, 6), 10)) == (1, 5, 7, 10)
"""

def remove_nested(tup):
    """
    >>> remove_nested((1, 5, 7, (4, 6), 10))
    (1, 5, 7, 10)
    """
    return tup[0:3] + tup[4:]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
/python/python_fundamentals/python_fundamentals_2/python_fundamentals_2_1.py
"""
Write a function that takes a list of numbers and returns the sum of the numbers.
assert sum_list([1, 2, 3, 4, 5]) == 15
"""

def sum_list(lst):
    """
    >>> sum_list([1, 2, 3, 4, 5])
    15
    """
    return sum(lst)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
/python/python_fundamentals/python_fundamentals_1/python_fundamentals_1_2.py
"""
Write a function that takes a list of numbers and returns the largest number in the list.
assert largest_number([1, 2, 3, 4, 5]) == 5
"""

def largest_number(lst):
    """
    >>> largest_number([1, 2, 3, 4, 5])
    5
    """
    return max(lst)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
/python/python_fundamentals/python_fundamentals_1/python_fundamentals_1_1.py
"""
Write a function that takes a list of numbers and returns the smallest number in the list.
assert smallest_number([1, 2, 3, 4, 5]) == 1
"""

def smallest_number(lst):
    """
    >>> smallest_number([1, 2, 3, 4, 5])
    1
    """
    return min(lst)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
/python/python_fundamentals/python_fundamentals_2/python_fundamentals_2_2.py
"""
Write a function that takes a list of numbers and returns the average (mean) of the numbers.
assert average([1, 2, 3, 4, 5]) == 3
"""

def average(lst):
    """
    >>> average([1, 2, 3, 4, 5])
    3.0
    """
    return sum(lst) / len(lst)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
/python/python_fundamentals/python_fundamentals_2/python_fundamentals_2_3.py
"""
Write a function that takes a list of numbers and returns the median of the numbers.
assert median([1, 2, 3, 4, 5]) == 3
"""

def median(lst):
    """
    >>> median([1, 2, 3, 4, 5])
    3.0
    """
    lst.sort()
    if len(lst) % 2 == 0:
        return (lst[len(lst) // 2] + lst[len(lst) // 2 - 1]) / 2
    else:
        return lst[len(lst) // 2]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
/python/python_fundamentals/python_fundamentals_1/python_fundamentals_1_3.py
"""
Write a function that takes a list of numbers and returns the sum of all the even numbers in the list.
assert sum_even([1, 2, 3, 4, 5]) == 6
"""

def sum_even(lst):
    """
    >>> sum_even([1, 2, 3, 4, 5])
    6
    """
    return sum([x for x in lst if x % 2 == 0])

if __name__ == '__main__':
    import doctest
    doctest.testmod()
/python