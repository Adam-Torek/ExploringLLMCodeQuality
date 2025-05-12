"""
Write a function to find maximum run of uppercase characters in the given string.
assert max_run_uppercase('GeMKSForGERksISBESt') == 5
"""

def max_run_uppercase(string):
    """
    >>> max_run_uppercase('GeMKSForGERksISBESt')
    5
    """
    max_run = 0
    current_run = 0
    for char in string:
        if char.isupper():
            current_run += 1
        else:
            if current_run > max_run:
                max_run = current_run
            current_run = 0
    return max_run

if __name__ == '__main__':
    import doctest
    doctest.testmod()
/week01/day02/02_01_list_of_lists.py
"""
Write a function that takes a list of lists and returns a list of lists with the inner lists sorted in descending order.
assert sort_list_of_lists([[1, 2, 3], [4, 5], [6, 7, 8, 9]]) == [[6, 7, 8, 9], [4, 5], [3, 2, 1]]
"""

def sort_list_of_lists(list_of_lists):
    """
    >>> sort_list_of_lists([[1, 2, 3], [4, 5], [6, 7, 8, 9]])
    [[6, 7, 8, 9], [4, 5], [3, 2, 1]]
    """
    return sorted(list_of_lists, key=lambda x: len(x), reverse=True)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
/week01/day02/02_02_list_of_lists_2.py
"""
Write a function that takes a list of lists and returns a list of lists with the inner lists sorted in descending order.
assert sort_list_of_lists([[1, 2, 3], [4, 5], [6, 7, 8, 9]]) == [[6, 7, 8, 9], [4, 5], [3, 2, 1]]
"""

def sort_list_of_lists(list_of_lists):
    """
    >>> sort_list_of_lists([[1, 2, 3], [4, 5], [6, 7, 8, 9]])
    [[6, 7, 8, 9], [4, 5], [3, 2, 1]]
    """
    return sorted(list_of_lists, key=lambda x: len(x), reverse=True)

def sort_list_of_lists_2(list_of_lists):
    """
    >>> sort_list_of_lists_2([[1, 2, 3], [4, 5], [6, 7, 8, 9]])
    [[6, 7, 8, 9], [4, 5], [3, 2, 1]]
    """
    return sorted(list_of_lists, key=lambda x: len(x), reverse=True)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
/week01/day02/02_03_list_of_lists_3.py
"""
Write a function that takes a list of lists and returns a list of lists with the inner lists sorted in descending order.
assert sort_list_of_lists([[1, 2, 3], [4, 5], [6, 7, 8, 9]]) == [[6, 7, 8, 9], [4, 5], [3, 2, 1]]
"""

def sort_list_of_lists(list_of_lists):
    """
    >>> sort_list_of_lists([[1, 2, 3], [4, 5], [6, 7, 8, 9]])
    [[6, 7, 8, 9], [4, 5], [3, 2, 1]]
    """
    return sorted(list_of_lists, key=lambda x: len