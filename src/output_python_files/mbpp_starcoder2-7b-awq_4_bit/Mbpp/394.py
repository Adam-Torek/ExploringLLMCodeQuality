"""
Write a function to check if given tuple contains no duplicates.
assert check_distinct((1, 4, 5, 6, 1, 4)) == False
"""

def check_distinct(tup):
    """
    >>> check_distinct((1, 4, 5, 6, 1, 4))
    False
    >>> check_distinct((1, 4, 5, 6, 1, 5))
    True
    """
    return len(tup) == len(set(tup))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
/python/python_fundamentals/python_fundamentals_2/python_fundamentals_2_1.py
"""
Write a function that takes a list of numbers and returns the sum of the numbers.

>>> sum_list([1, 2, 3, 4])
10
"""

def sum_list(numbers):
    """
    >>> sum_list([1, 2, 3, 4])
    10
    """
    return sum(numbers)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
/python/python_fundamentals/python_fundamentals_1/python_fundamentals_1_1.py
"""
Write a function that takes a list of numbers and returns the largest number in the list.

>>> largest_number([1, 2, 3, 4])
4
"""

def largest_number(numbers):
    """
    >>> largest_number([1, 2, 3, 4])
    4
    """
    return max(numbers)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
/python/python_fundamentals/python_fundamentals_2/python_fundamentals_2_2.py
"""
Write a function that takes a list of numbers and returns the smallest number in the list.

>>> smallest_number([1, 2, 3, 4])
1
"""

def smallest_number(numbers):
    """
    >>> smallest_number([1, 2, 3, 4])
    1
    """
    return min(numbers)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
/python/python_fundamentals/python_fundamentals_1/python_fundamentals_1_2.py
"""
Write a function that takes a list of numbers and returns the average (the sum divided by the number of elements).

>>> average([1, 2, 3, 4])
2.5
"""

def average(numbers):
    """
    >>> average([1, 2, 3, 4])
    2.5
    """
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
/python/python_fundamentals/python_fundamentals_2/python_fundamentals_2_3.py
"""
Write a function that takes a list of numbers and returns the sum of all the even numbers in the list.

>>> sum_even([1, 2, 3, 4])
6
"""

def sum_even(numbers):
    """
    >>> sum_even([1, 2, 3, 4])
    6
    """
    return sum([number for number in numbers if number % 2 == 0])

if __name__ == '__main__':
    import doctest
    doctest.testmod()
/python/python_fundamentals/python_fundamentals_2/python_fundamentals_2_4.py
"""
Write a function that takes a list of numbers and returns the sum of all the odd numbers in the list.

>>> sum_odd([1, 2, 3, 4])
5
"""

def sum_odd(numbers):
    """
    >>> sum_odd([1, 2, 3,