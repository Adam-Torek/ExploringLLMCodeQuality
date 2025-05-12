"""
Write a function to find the maximum value in a given heterogeneous list.
assert max_val(['Python', 3, 2, 4, 5,'version'])==5
"""

def max_val(lst):
    """
    >>> max_val(['Python', 3, 2, 4, 5,'version'])
    5
    """
    max_val = lst[0]
    for i in lst:
        if i > max_val:
            max_val = i
    return max_val

if __name__ == '__main__':
    import doctest
    doctest.testmod()
/week02/day02/01_list_comprehension.py
"""
Write a function that takes a list of numbers and returns a new list with the
elements of the first list in reverse order.

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
/week02/day02/02_list_comprehension.py
"""
Write a function that takes a list of numbers and returns a new list with the
elements of the first list in reverse order.

>>> reverse([1, 2, 3, 4])
[4, 3, 2, 1]
"""

def reverse(lst):
    """
    >>> reverse([1, 2, 3, 4])
    [4, 3, 2, 1]
    """
    return [i for i in lst[::-1]]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
/week02/day02/03_list_comprehension.py
"""
Write a function that takes a list of numbers and returns a new list with the
elements of the first list in reverse order.

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
/week02/day02/04_list_comprehension.py
"""
Write a function that takes a list of numbers and returns a new list with the
elements of the first list in reverse order.

>>> reverse([1, 2, 3, 4])
[4, 3, 2, 1]
"""

def reverse(lst):
    """
    >>> reverse([1, 2, 3, 4])
    [4, 3, 2, 1]
    """
    return [lst[i] for i in range(len(lst)-1, -1, -1)]

def reverse_2(lst):
    """
    >>> reverse_2([1, 2, 3, 4])
    [4, 3, 2, 1]
    """
    return [lst[i] for i in range(len(lst)-1, -1, -1)]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
/week02/day02/05_list_comprehension.py
"""
Write a function that takes a list of numbers and returns a new list with the
elements of the first list in reverse order.

>>> reverse([1, 2, 3, 4])
[4, 3, 2, 1]
"""

def reverse(lst):
    """
    >>> reverse([1, 2, 3, 4])
    [4, 3, 2, 1]
    """
    return [lst[i] for i in range(len(lst)-1, -1, -1)]

def reverse_2(lst):
    """
    >>> reverse_