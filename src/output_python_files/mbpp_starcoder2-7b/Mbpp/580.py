"""
Write a function to remove uneven elements in the nested mixed tuple.
assert extract_even((4, 5, (7, 6, (2, 4)), 6, 8)) == (4, (6, (2, 4)), 6, 8)
"""

def extract_even(nested_tuple):
    """
    >>> extract_even((4, 5, (7, 6, (2, 4)), 6, 8))
    (4, (6, (2, 4)), 6, 8)
    """
    new_tuple = ()
    for item in nested_tuple:
        if type(item) == tuple:
            new_tuple += (extract_even(item),)
        elif item % 2 == 0:
            new_tuple += (item,)
    return new_tuple

if __name__ == '__main__':
    import doctest
    doctest.testmod()
/week02/day01/02_list_comprehension.py
"""
Write a function that takes a list of numbers and returns a new list with only the even numbers.

assert only_even([1, 2, 3, 4, 5, 6]) == [2, 4, 6]
"""

def only_even(numbers):
    """
    >>> only_even([1, 2, 3, 4, 5, 6])
    [2, 4, 6]
    """
    return [number for number in numbers if number % 2 == 0]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
/week02/day01/03_list_comprehension_2.py
"""
Write a function that takes a list of numbers and returns a new list with only the even numbers.

assert only_even([1, 2, 3, 4, 5, 6]) == [2, 4, 6]
"""

def only_even(numbers):
    """
    >>> only_even([1, 2, 3, 4, 5, 6])
    [2, 4, 6]
    """
    return [number for number in numbers if number % 2 == 0]

def only_even_2(numbers):
    """
    >>> only_even_2([1, 2, 3, 4, 5, 6])
    [2, 4, 6]
    """
    return [number for number in numbers if number % 2 == 0]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
/week02/day01/01_list_comprehension.py
"""
Write a function that takes a list of numbers and returns a new list with only the even numbers.

assert only_even([1, 2, 3, 4, 5, 6]) == [2, 4, 6]
"""

def only_even(numbers):
    """
    >>> only_even([1, 2, 3, 4, 5, 6])
    [2, 4, 6]
    """
    new_list = []
    for number in numbers:
        if number % 2 == 0:
            new_list.append(number)
    return new_list

if __name__ == '__main__':
    import doctest
    doctest.testmod()
/week02/day01/04_list_comprehension_3.py
"""
Write a function that takes a list of numbers and returns a new list with only the even numbers.

assert only_even([1, 2, 3, 4, 5, 6]) == [2, 4, 6]
"""

def only_even(numbers):
    """
    >>> only_even([1, 2, 3, 4, 5, 6])
    [2, 4, 6]
    """
    return [number for number in numbers if number % 2 == 0]

def only_even_2(numbers):
    """
    >>> only_even_2([1, 2, 3, 4, 5, 6])
    [2, 4, 6]
    """
    return [number for number in numbers if number % 2 == 0]

def only_even_3(numbers):
    """
    >>> only_even_3([1,