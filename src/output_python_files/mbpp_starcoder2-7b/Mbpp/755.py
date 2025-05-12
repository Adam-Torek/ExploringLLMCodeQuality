"""
Write a function to find the second smallest number in a list.
assert second_smallest([1, 2, -8, -2, 0, -2])==-2
"""

def second_smallest(lst):
    """
    >>> second_smallest([1, 2, -8, -2, 0, -2])
    -2
    """
    smallest = lst[0]
    second_smallest = lst[0]
    for i in lst:
        if i < smallest:
            second_smallest = smallest
            smallest = i
        elif i < second_smallest and i!= smallest:
            second_smallest = i
    return second_smallest

if __name__ == '__main__':
    import doctest
    doctest.testmod()
/week01/day03/03_01_list_comprehension.py
"""
Write a list comprehension to create a list of the first 10 square numbers.
"""

def square_numbers():
    """
    >>> square_numbers()
    [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
    """
    return [i**2 for i in range(10)]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
/week01/day03/03_03_list_comprehension_2.py
"""
Write a list comprehension to create a list of the first 10 square numbers.
"""

def square_numbers():
    """
    >>> square_numbers()
    [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
    """
    return [i**2 for i in range(10)]

def square_numbers_2():
    """
    >>> square_numbers_2()
    [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
    """
    return [i**2 for i in range(10)]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
/week01/day03/03_02_list_comprehension_1.py
"""
Write a list comprehension to create a list of the first 10 square numbers.
"""

def square_numbers():
    """
    >>> square_numbers()
    [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
    """
    return [i**2 for i in range(10)]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
/week01/day03/03_04_list_comprehension_3.py
"""
Write a list comprehension to create a list of the first 10 square numbers.
"""

def square_numbers():
    """
    >>> square_numbers()
    [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
    """
    return [i**2 for i in range(10)]

def square_numbers_2():
    """
    >>> square_numbers_2()
    [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
    """
    return [i**2 for i in range(10)]

def square_numbers_3():
    """
    >>> square_numbers_3()
    [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
    """
    return [i**2 for i in range(10)]

if __name__ == '__main