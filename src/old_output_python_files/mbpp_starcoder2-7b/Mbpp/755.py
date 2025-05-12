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
<file_sep>/week_03/day_01/02_list_to_dict.py
"""
Write a function that takes a list of strings and returns a dictionary with
each string as a key and its length as a value.
assert list_to_dict(["a", "bb", "ccc"]) == {"a": 1, "bb": 2, "ccc": 3}
"""

def list_to_dict(lst):
    """
    >>> list_to_dict(["a", "bb", "ccc"])
    {'a': 1, 'bb': 2, 'ccc': 3}
    """
    return {i: len(i) for i in lst}

if __name__ == '__main__':
    import doctest
    doctest.testmod()
<file_sep>/week_03/day_01/01_list_to_dict.py
"""
Write a function that takes a list of strings and returns a dictionary with
each string as a key and its length as a value.
assert list_to_dict(["a", "bb", "ccc"]) == {"a": 1, "bb": 2, "ccc": 3}
"""

def list_to_dict(lst):
    """
    >>> list_to_dict(["a", "bb", "ccc"])
    {'a': 1, 'bb': 2, 'ccc': 3}
    """
    d = {}
    for i in lst:
        d[i] = len(i)
    return d

if __name__ == '__main__':
    import doctest
    doctest.testmod()
<file_sep>/week_03/day_01/03_list_to_dict.py
"""
Write a function that takes a list of strings and returns a dictionary with
each string as a key and its length as a value.
assert list_to_dict(["a", "bb", "ccc"]) == {"a": 1, "bb": 2, "ccc": 3}
"""

def list_to_dict(lst):
    """
    >>> list_to_dict(["a", "bb", "ccc"])
    {'a': 1, 'bb': 2, 'ccc': 3}
    """
    return {i: len(i) for i in lst}

if __name__ == '__main__':
    import doctest
    doctest.testmod()
<file_sep>/week_03/day_01/04_list_to_dict.py
"""
Write a function that takes a list of strings and returns a dictionary with
each string as a key and its length as a value.
assert list_to_dict(["a", "bb", "ccc"]) == {"a": 1, "bb": 2, "ccc": 3}
"""

def list_to_dict(lst):
    """
    >>> list_to_dict(["a", "bb", "ccc"])
    {'a': 1, 'bb': 2, 'ccc': 3}
    """
    return {i: len(i) for i in lst}

if __name__ == '__main__':
    import doctest
    doctest.testmod()
<file_sep>/week_03/day_01/05_list_to_dict.py
"""
Write a function that takes a list of strings and returns a dictionary with
each string as a key and its length as a value.
assert list_to_dict(["a", "bb", "ccc"]) == {"a": 1, "bb": 2, "ccc": 3}
"""

def list_to_dict(lst):
    """
    >>> list_to_dict(["a", "bb", "ccc"])
    {'a': 1, 'bb': 2, 'ccc': 3}
    """
    return {