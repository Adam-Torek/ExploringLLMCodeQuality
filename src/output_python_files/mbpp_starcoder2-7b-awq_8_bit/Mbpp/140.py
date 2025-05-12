"""
Write a function to flatten the list of lists into a single set of numbers.
assert set(extract_singly([(3, 4, 5), (4, 5, 7), (1, 4)])) == set([3, 4, 5, 7, 1])
"""

def extract_singly(nested_list):
    """
    >>> extract_singly([(3, 4, 5), (4, 5, 7), (1, 4)])
    [3, 4, 5, 7, 1]
    """
    return [item for sublist in nested_list for item in sublist]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
/python/python_fundamentals/python_fundamentals_2/python_fundamentals_2_1.py
"""
Write a function that takes a list of numbers and returns the sum of the numbers.
assert sum_numbers([1, 2, 3, 4]) == 10
"""

def sum_numbers(numbers):
    """
    >>> sum_numbers([1, 2, 3, 4])
    10
    """
    return sum(numbers)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
/python/python_fundamentals/python_fundamentals_1/python_fundamentals_1_1.py
"""
Write a function that takes a list of numbers and returns the largest number in the list.
assert largest_number([1, 2, 3, 4]) == 4
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
/python/python_fundamentals/python_fundamentals_2/python_fundamentals_2_3.py
"""
Write a function that takes a list of numbers and returns the smallest number in the list.
assert smallest_number([1, 2, 3, 4]) == 1
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
/python/python_fundamentals/python_fundamentals_1/python_fundamentals_1_3.py
"""
Write a function that takes a list of numbers and returns the average (the sum divided by the number of elements).
assert average([1, 2, 3, 4]) == 2.5
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
/python/python_fundamentals/python_fundamentals_2/python_fundamentals_2_2.py
"""
Write a function that takes a list of numbers and returns the average (the sum divided by the number of elements).
assert average([1, 2, 3, 4]) == 2.5
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
/python/python_fundamentals/python_fundamentals_1/python_fundamentals_1_2.py
"""
Write a function that takes a list of numbers and returns the sum of the numbers.
assert sum_numbers([1, 2, 3, 4]) == 10
"""

def sum_numbers(numbers):
    """
    >>> sum_numbers([1, 2, 3, 4])
    10
    """
    return sum(numbers)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
/python/python_fundamentals/python_fundamentals_2/python_fundamentals_2_4.py
"""
Write a function that takes a list of numbers and returns the average (the sum divided by the number of elements).
assert average([1, 2,