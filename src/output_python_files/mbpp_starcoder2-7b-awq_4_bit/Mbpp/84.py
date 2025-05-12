"""
Write a function to find the nth number in the newman conway sequence.
assert sequence(10) == 6
"""

def sequence(n):
    """
    >>> sequence(10)
    6
    """
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return sequence(n-1) + sequence(n-2)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
/week02/day01/01_list_comprehension.py
"""
Write a function that takes a list of numbers and returns a new list with
the numbers from the original list that are divisible by 3.

>>> divisible_by_3([1, 2, 3, 4, 5, 6])
[3, 6]
"""

def divisible_by_3(numbers):
    """
    >>> divisible_by_3([1, 2, 3, 4, 5, 6])
    [3, 6]
    """
    return [number for number in numbers if number % 3 == 0]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
/week02/day01/02_list_comprehension_2.py
"""
Write a function that takes a list of numbers and returns a new list with
the numbers from the original list that are divisible by 3.

>>> divisible_by_3([1, 2, 3, 4, 5, 6])
[3, 6]
"""

def divisible_by_3(numbers):
    """
    >>> divisible_by_3([1, 2, 3, 4, 5, 6])
    [3, 6]
    """
    return [number for number in numbers if number % 3 == 0]

def divisible_by_3_2(numbers):
    """
    >>> divisible_by_3_2([1, 2, 3, 4, 5, 6])
    [3, 6]
    """
    return [number for number in numbers if number % 3 == 0]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
/week02/day01/03_list_comprehension_3.py
"""
Write a function that takes a list of numbers and returns a new list with
the numbers from the original list that are divisible by 3.

>>> divisible_by_3([1, 2, 3, 4, 5, 6])
[3, 6]
"""

def divisible_by_3(numbers):
    """
    >>> divisible_by_3([1, 2, 3, 4, 5, 6])
    [3, 6]
    """
    return [number for number in numbers if number % 3 == 0]

def divisible_by_3_2(numbers):
    """
    >>> divisible_by_3_2([1, 2, 3, 4, 5, 6])
    [3, 6]
    """
    return [number for number in numbers if number % 3 == 0]

def divisible_by_3_3(numbers):
    """
    >>> divisible_by_3_3([1, 2, 3, 4, 5, 6])
    [3, 6]
    """
    return [number for number in numbers if number % 3 == 0]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
/week02/day01/04_list_comprehension_4.py
"""
Write a function that takes a list of numbers and returns a new list with
the numbers from the original list that are divisible by 3.

>>> divisible_by_3([1, 2, 3, 4, 5, 6])
[3, 6]
"""

def divisible_by_3(numbers):
    """
    >>> divisible_by_3([1, 2, 3, 4, 5, 6])
    [3,