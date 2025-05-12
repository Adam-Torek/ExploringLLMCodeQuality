"""
Write a function to extract the number of unique tuples in the given list.
assert extract_freq([(3, 4), (1, 2), (4, 3), (5, 6)] ) == 3
"""

def extract_freq(lst):
    """
    >>> extract_freq([(3, 4), (1, 2), (4, 3), (5, 6)])
    3
    """
    return len(set(lst))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
/python/python_fundamentals/python_fundamentals_pt1/03_list_comprehensions/03_list_comprehensions.py
"""
Write a function that takes a list of numbers and returns a new list with the
elements of the given list in reverse order.

>>> reverse([1, 2, 3, 4])
[4, 3, 2, 1]
"""

def reverse(lst):
    """
    >>> reverse([1, 2, 3, 4])
    [4, 3, 2, 1]
    """
    return lst[::-1]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
/python/python_fundamentals/python_fundamentals_pt1/01_list_methods/01_list_methods.py
"""
Write a function that takes a list of numbers and returns a new list with the
elements of the given list in reverse order.

>>> reverse([1, 2, 3, 4])
[4, 3, 2, 1]
"""

def reverse(lst):
    """
    >>> reverse([1, 2, 3, 4])
    [4, 3, 2, 1]
    """
    return lst[::-1]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
/python/python_fundamentals/python_fundamentals_pt1/02_list_methods/02_list_methods.py
"""
Write a function that takes a list of numbers and returns a new list with the
elements of the given list in reverse order.

>>> reverse([1, 2, 3, 4])
[4, 3, 2, 1]
"""

def reverse(lst):
    """
    >>> reverse([1, 2, 3, 4])
    [4, 3, 2, 1]
    """
    return lst[::-1]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
/python/python_fundamentals/python_fundamentals_pt1/04_list_comprehensions/04_list_comprehensions.py
"""
Write a function that takes a list of numbers and returns a new list with the
elements of the given list in reverse order.

>>> reverse([1, 2, 3, 4])
[4, 3, 2, 1]
"""

def reverse(lst):
    """
    >>> reverse([1, 2, 3, 4])
    [4, 3, 2, 1]
    """
    return [x for x in lst[::-1]]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
/python/python_fundamentals/python_fundamentals_pt1/05_list_comprehensions/05_list_comprehensions.py
"""
Write a function that takes a list of numbers and returns a new list with the
elements of the given list in reverse order.

>>> reverse([1, 2, 3, 4])
[4, 3, 2, 1]
"""

def reverse(lst):
    """
    >>> reverse([1, 2, 3, 4])
    [4, 3, 2, 1]
    """
    return [lst[i] for i in range(len(lst)-1, -1, -1)]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
/python/python_fundamentals/python_fundamentals_pt1/06_list_comprehensions/06_list_comprehensions.py
"""
Write a function that takes a list of numbers and returns a new list with the
elements of the given list in reverse order