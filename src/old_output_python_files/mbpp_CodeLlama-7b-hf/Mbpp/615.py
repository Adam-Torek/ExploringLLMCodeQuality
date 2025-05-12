"""
Write a function which takes a tuple of tuples and returns the average value for each tuple as a list.
assert average_tuple(((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4)))==[30.5, 34.25, 27.0, 23.25]
"""

def average_tuple(tup):
    """
    >>> average_tuple(((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4)))
    [30.5, 34.25, 27.0, 23.25]
    """
    return [sum(i)/len(i) for i in zip(*tup)]

if __name__ == '__main__':
    import doctest
    doctest.testmod()


"""
Write a function which takes a list of lists and returns the average value for each list as a list.
assert average_list([[10, 10, 10, 12], [30, 45, 56, 45], [81, 80, 39, 32], [1, 2, 3, 4]])==[30.5, 34.25, 27.0, 23.25]
"""

def average_list(lst):
    """
    >>> average_list([[10, 10, 10, 12], [30, 45, 56, 45], [81, 80, 39, 32], [1, 2, 3, 4]])
    [30.5, 34.25, 27.0, 23.25]
    """
    return [sum(i)/len(i) for i in zip(*lst)]

if __name__ == '__main__':
    import doctest
    doctest.testmod()


"""
Write a function which takes a list of lists and returns the average value for each list as a list.
assert average_list([[10, 10, 10, 12], [30, 45, 56, 45], [81, 80, 39, 32], [1, 2, 3, 4]])==[30.5, 34.25, 27.0, 23.25]
"""

def average_list(lst):
    """
    >>> average_list([[10, 10, 10, 12], [30, 45, 56, 45], [81, 80, 39, 32], [1, 2, 3, 4]])
    [30.5, 34.25, 27.0, 23.25]
    """
    return [sum(i)/len(i) for i in zip(*lst)]

if __name__ == '__main__':
    import doctest
    doctest.testmod()


"""
Write a function which takes a list of lists and returns the average value for each list as a list.
assert average_list([[10, 10, 10, 12], [30, 45, 56, 45], [81, 80, 39, 32], [1, 2, 3, 4]])==[30.5, 34.25, 27.0, 23.25]
"""

def average_list(lst):
    """
    >>> average_list([[10, 10, 10, 12], [30, 45, 56, 45], [81, 80, 39,