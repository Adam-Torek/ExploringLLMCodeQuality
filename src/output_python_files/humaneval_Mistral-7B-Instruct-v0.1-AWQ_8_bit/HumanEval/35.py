def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    if not l:
        return None
    else:
        return max(l)

def min_element(l: list):
    """Return minimum element in the list.
    >>> min_element([1, 2, 3])
    1
    >>> min_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    -10
    """
    if not l:
        return None
    else:
        return min(l)

def sum_list(l: list):
    """Return sum of all elements in the list.
    >>> sum_list([1, 2, 3])
    6
    >>> sum_list([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    113
    """
    if not l:
        return 0
    else:
        return sum(l)

def product_list(l: list):
    """Return product of all elements in the list.
    >>> product_list([1, 2, 3])
    6
    >>> product_list([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    0
    """
    if not l:
        return 1
    else:
        return product(l)

def average_list(l: list):
    """Return average of all elements in the list.
    >>> average_list([1, 2, 3])
    2.0
    >>> average_list([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    1.0
    """
    if not l:
        return 0
    else:
        return sum(l) / len(l)

def length_list(l: list):
    """Return length of the list.
    >>> length_list([1, 2, 3])
    3
    >>> length_list([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    11
    """
    if not l:
        return 0
    else:
        return len(l)

def reverse_list(l: list):
    """Return reversed list.
    >>> reverse_list([1, 2, 3])
    [3, 2, 1]
    >>> reverse_list([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [-10, -3, -2, 3, 9, 0, 123, 1, -5, 3, 5]
    """
    if not l:
        return []
    else:
        return l[::-1]

def insert_list(l: list, x: int, i: int):
    """Return new list with x inserted at index i.
    >>> insert_list([1, 2, 3], 4, 2)
    [1, 2, 4, 3]
    >>> insert_list([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10], 10, 6)
    [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10, 10]
    """
    if not l:
        return []
    else:
        return l[:i] + [x] + l[i:]

def remove_list