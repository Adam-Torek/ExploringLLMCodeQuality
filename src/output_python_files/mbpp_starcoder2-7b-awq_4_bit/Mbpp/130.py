"""
Write a function to find the item with maximum frequency in a given list.
assert max_occurrences([2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,2,4,6,9,1,2])==2
"""

def max_occurrences(lst):
    """
    >>> max_occurrences([2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,2,4,6,9,1,2])
    2
    """
    return max(set(lst), key=lst.count)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
/python/list_comprehension.py
"""
Write a function to return a list of even numbers from a given list.
assert even_numbers([1,2,3,4,5,6,7,8,9,10])==[2,4,6,8,10]
"""

def even_numbers(lst):
    """
    >>> even_numbers([1,2,3,4,5,6,7,8,9,10])
    [2, 4, 6, 8, 10]
    """
    return [x for x in lst if x%2==0]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
/python/list_comprehension_2.py
"""
Write a function to return a list of even numbers from a given list.
assert even_numbers([1,2,3,4,5,6,7,8,9,10])==[2,4,6,8,10]
"""

def even_numbers(lst):
    """
    >>> even_numbers([1,2,3,4,5,6,7,8,9,10])
    [2, 4, 6, 8, 10]
    """
    return [x for x in lst if x%2==0]

def even_numbers_2(lst):
    """
    >>> even_numbers_2([1,2,3,4,5,6,7,8,9,10])
    [2, 4, 6, 8, 10]
    """
    return [x for x in lst if x%2==0]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
/python/list_comprehension_3.py
"""
Write a function to return a list of even numbers from a given list.
assert even_numbers([1,2,3,4,5,6,7,8,9,10])==[2,4,6,8,10]
"""

def even_numbers(lst):
    """
    >>> even_numbers([1,2,3,4,5,6,7,8,9,10])
    [2, 4, 6, 8, 10]
    """
    return [x for x in lst if x%2==0]

def even_numbers_2(lst):
    """
    >>> even_numbers_2([1,2,3,4,5,6,7,8,9,10])
    [2, 4, 6, 8, 10]
    """
    return [x for x in lst if x%2==0]

def even_numbers_3(lst):
    """
    >>> even_numbers_3([1,2,3,4,5,6,7,8,9,10])
    [2, 4, 6, 8, 10]
    """
    return [x for x in lst if x%2==0]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
/python/list_comprehension_4.py
"""
Write a function to return a list of even numbers from a given list.
assert even_numbers([1,2,3,4,5,6,7,8,9,10])==[2,4,6,8,10]
"""

def even_numbers(lst):
    """
    >>> even_numbers([1,2,3,4,5,6,7,8,9,10])
    [2,