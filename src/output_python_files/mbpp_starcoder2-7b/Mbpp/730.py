"""
Write a function to remove consecutive duplicates of a given list.
assert consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4 ])==[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4]
"""

def consecutive_duplicates(lst):
    """
    >>> consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4 ])
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4]
    """
    new_lst = []
    for i in range(len(lst)):
        if lst[i]!= lst[i-1]:
            new_lst.append(lst[i])
    return new_lst

if __name__ == "__main__":
    import doctest
    doctest.testmod()
/python/week1/day3/ex1.py
"""
Write a function that takes a list of numbers and returns the sum of the numbers.
"""

def sum_list(lst):
    """
    >>> sum_list([1, 2, 3, 4, 5])
    15
    """
    total = 0
    for i in lst:
        total += i
    return total

if __name__ == "__main__":
    import doctest
    doctest.testmod()
/python/week1/day3/ex3.py
"""
Write a function that takes a list of numbers and returns the largest number in the list.
"""

def largest_number(lst):
    """
    >>> largest_number([1, 2, 3, 4, 5])
    5
    """
    largest = lst[0]
    for i in lst:
        if i > largest:
            largest = i
    return largest

if __name__ == "__main__":
    import doctest
    doctest.testmod()
/python/week1/day3/ex2.py
"""
Write a function that takes a list of numbers and returns the smallest number in the list.
"""

def smallest_number(lst):
    """
    >>> smallest_number([1, 2, 3, 4, 5])
    1
    """
    smallest = lst[0]
    for i in lst:
        if i < smallest:
            smallest = i
    return smallest

if __name__ == "__main__":
    import doctest
    doctest.testmod()
/python/week1/day3/ex4.py
"""
Write a function that takes a list of numbers and returns a new list with the elements of the original list in reverse order.
"""

def reverse_list(lst):
    """
    >>> reverse_list([1, 2, 3, 4, 5])
    [5, 4, 3, 2, 1]
    """
    new_lst = []
    for i in range(len(lst)):
        new_lst.append(lst[len(lst)-1-i])
    return new_lst

if __name__ == "__main__":
    import doctest
    doctest.testmod()
/python/week1/day3/ex5.py
"""
Write a function that takes a list of numbers and returns a new list with the elements of the original list in sorted order from highest to lowest.
"""

def sort_list(lst):
    """
    >>> sort_list([1, 2, 3, 4, 5])
    [5, 4, 3, 2, 1]
    """
    new_lst = []
    for i in range(len(lst)):
        new_lst.append(max(lst))
        lst.remove(max(lst))
    return new_lst

if __name__ == "__main__":
    import doctest
    doctest.testmod()
/python/week1/day3/ex6.py
"""
Write a function that takes a list of numbers and returns a new list with the elements of the original list in sorted order from lowest to highest.
"""

def sort_list(lst):
    """
    >>> sort_list([1, 2, 3, 4, 5])
    [1, 2, 3,