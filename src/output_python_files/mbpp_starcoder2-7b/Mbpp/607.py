"""
Write a function to search a string for a regex pattern. The function should return the matching subtring, a start index and an end index.
assert find_literals('The quick brown fox jumps over the lazy dog.', 'fox') == ('fox', 16, 19)
"""

def find_literals(string, pattern):
    """
    >>> find_literals('The quick brown fox jumps over the lazy dog.', 'fox')
    ('fox', 16, 19)
    """
    return re.search(pattern, string).group(), re.search(pattern, string).start(), re.search(pattern, string).end()

if __name__ == '__main__':
    import doctest
    doctest.testmod()
/week_02/day_01/02_list_comprehension.py
"""
Write a function that takes a list of numbers and returns a new list with only the even numbers.
"""

def even_numbers(numbers):
    """
    >>> even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    [2, 4, 6, 8, 10]
    """
    return [number for number in numbers if number % 2 == 0]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
/week_02/day_01/01_list_comprehension.py
"""
Write a function that takes a list of numbers and returns a new list with only the odd numbers.
"""

def odd_numbers(numbers):
    """
    >>> odd_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    [1, 3, 5, 7, 9]
    """
    return [number for number in numbers if number % 2!= 0]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
/week_02/day_01/03_list_comprehension.py
"""
Write a function that takes a list of numbers and returns a new list with only the positive numbers.
"""

def positive_numbers(numbers):
    """
    >>> positive_numbers([-1, 2, -3, 4, -5, 6, -7, 8, -9, 10])
    [2, 4, 6, 8, 10]
    """
    return [number for number in numbers if number > 0]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
/week_02/day_01/04_list_comprehension.py
"""
Write a function that takes a list of numbers and returns a new list with only the negative numbers.
"""

def negative_numbers(numbers):
    """
    >>> negative_numbers([-1, 2, -3, 4, -5, 6, -7, 8, -9, 10])
    [-1, -3, -5, -7, -9]
    """
    return [number for number in numbers if number < 0]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
/week_02/day_01/05_list_comprehension.py
"""
Write a function that takes a list of numbers and returns a new list with only the numbers that are divisible by 3.
"""

def divisible_by_three(numbers):
    """
    >>> divisible_by_three([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    [3, 6, 9]
    """
    return [number for number in numbers if number % 3 == 0]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
/week_02/day_01/06_list_comprehension.py
"""
Write a function that takes a list of numbers and returns a new list with only the numbers that are divisible by 3 and 5.
"""

def divisible_by_three_and_five(numbers):
    """
    >>> divisible_by_three_and_five([1,