"""
Write a function to find the minimum value in a given heterogeneous list.
assert min_val(['Python', 3, 2, 4, 5,'version'])==2
"""

def min_val(lst):
    """
    >>> min_val(['Python', 3, 2, 4, 5,'version'])
    2
    """
    min_val = lst[0]
    for i in lst:
        if i < min_val:
            min_val = i
    return min_val

if __name__ == '__main__':
    import doctest
    doctest.testmod()
/02_functions/02_03_01_function_with_default_argument.py
"""
Write a function that takes a list of numbers and returns the sum of the numbers.
If the list is empty, the function should return 0.
"""

def sum_of_numbers(lst):
    """
    >>> sum_of_numbers([1, 2, 3])
    6
    >>> sum_of_numbers([])
    0
    """
    sum_of_numbers = 0
    for i in lst:
        sum_of_numbers += i
    return sum_of_numbers

if __name__ == '__main__':
    import doctest
    doctest.testmod()
/02_functions/02_03_02_function_with_default_argument.py
"""
Write a function that takes a list of numbers and returns the sum of the numbers.
If the list is empty, the function should return 0.
"""

def sum_of_numbers(lst=[]):
    """
    >>> sum_of_numbers([1, 2, 3])
    6
    >>> sum_of_numbers([])
    0
    """
    sum_of_numbers = 0
    for i in lst:
        sum_of_numbers += i
    return sum_of_numbers

if __name__ == '__main__':
    import doctest
    doctest.testmod()
/02_functions/02_03_03_function_with_default_argument.py
"""
Write a function that takes a list of numbers and returns the sum of the numbers.
If the list is empty, the function should return 0.
"""

def sum_of_numbers(lst=[]):
    """
    >>> sum_of_numbers([1, 2, 3])
    6
    >>> sum_of_numbers([])
    0
    """
    sum_of_numbers = 0
    for i in lst:
        sum_of_numbers += i
    return sum_of_numbers

if __name__ == '__main__':
    import doctest
    doctest.testmod()
/02_functions/02_03_04_function_with_default_argument.py
"""
Write a function that takes a list of numbers and returns the sum of the numbers.
If the list is empty, the function should return 0.
"""

def sum_of_numbers(lst=[]):
    """
    >>> sum_of_numbers([1, 2, 3])
    6
    >>> sum_of_numbers([])
    0
    """
    sum_of_numbers = 0
    for i in lst:
        sum_of_numbers += i
    return sum_of_numbers

if __name__ == '__main__':
    import doctest
    doctest.testmod()
/02_functions/02_03_05_function_with_default_argument.py
"""
Write a function that takes a list of numbers and returns the sum of the numbers.
If the list is empty, the function should return 0.
"""

def sum_of_numbers(lst=[]):
    """
    >>> sum_of_numbers([1, 2, 3])
    6
    >>> sum_of_numbers([])
    0
    """
    sum_of_numbers = 0
    for i in lst:
        sum_of_numbers += i
    return sum_of_numbers

if __name__ == '__main__':
    import doctest
    doctest.testmod()
/02_functions/02_03_06_function_with_default_argument.py
"""
Write a