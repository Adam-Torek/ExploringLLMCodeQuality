"""
Write a function to flatten the list of lists into a single set of numbers.
assert set(extract_singly([(3, 4, 5), (4, 5, 7), (1, 4)])) == set([3, 4, 5, 7, 1])
"""

def extract_singly(list_of_lists):
    """
    >>> extract_singly([(3, 4, 5), (4, 5, 7), (1, 4)])
    [3, 4, 5, 7, 1]
    """
    return [item for sublist in list_of_lists for item in sublist]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
/python/python_fundamentals/python_fundamentals_2/python_fundamentals_2_1.py
"""
Write a function that takes a list of numbers and returns the sum of the numbers.
assert sum_list([1, 2, 3, 4, 5]) == 15
"""

def sum_list(list_of_numbers):
    """
    >>> sum_list([1, 2, 3, 4, 5])
    15
    """
    return sum(list_of_numbers)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
/python/python_fundamentals/python_fundamentals_1/python_fundamentals_1_2.py
"""
Write a function that takes a list of numbers and returns the largest number.
assert largest_number([1, 2, 3, 4, 5]) == 5
"""

def largest_number(list_of_numbers):
    """
    >>> largest_number([1, 2, 3, 4, 5])
    5
    """
    return max(list_of_numbers)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
/python/python_fundamentals/python_fundamentals_2/python_fundamentals_2_2.py
"""
Write a function that takes a list of numbers and returns the smallest number.
assert smallest_number([1, 2, 3, 4, 5]) == 1
"""

def smallest_number(list_of_numbers):
    """
    >>> smallest_number([1, 2, 3, 4, 5])
    1
    """
    return min(list_of_numbers)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
/python/python_fundamentals/python_fundamentals_1/python_fundamentals_1_1.py
"""
Write a function that takes a list of numbers and returns the average of the numbers.
assert average([1, 2, 3, 4, 5]) == 3
"""

def average(list_of_numbers):
    """
    >>> average([1, 2, 3, 4, 5])
    3.0
    """
    return sum(list_of_numbers) / len(list_of_numbers)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
/python/python_fundamentals/python_fundamentals_3/python_fundamentals_3_1.py
"""
Write a function that takes a list of numbers and returns the sum of the even numbers.
assert sum_even([1, 2, 3, 4, 5]) == 6
"""

def sum_even(list_of_numbers):
    """
    >>> sum_even([1, 2, 3, 4, 5])
    6
    """
    return sum([num for num in list_of_numbers if num % 2 == 0])

if __name__ == '__main__':
    import doctest
    doctest.testmod()
/python/python_fundamentals/python_fundamentals_3/python_fundamentals_3_2.py
"""
Write a function that takes a list of numbers and returns the sum of the odd numbers.
assert sum_odd([1, 2, 3, 4, 5]) == 9
"""

def sum_odd(list_of_numbers):
    """
    >>> sum_odd([1, 2, 3, 4, 5])
    9
    """
    return sum([num for num in list_of_numbers