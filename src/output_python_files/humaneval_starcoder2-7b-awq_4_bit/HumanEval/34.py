def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """

def reverse(l: list):
    """Return a reversed list
    >>> reverse([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [123, 0, 9, 3, 3, 2, 5, 3, 5]
    """

def reverse_inplace(l: list):
    """Reverse a list in place
    >>> l = [5, 3, 5, 2, 3, 3, 9, 0, 123]
    >>> reverse_inplace(l)
    >>> l
    [123, 0, 9, 3, 3, 2, 5, 3, 5]
    """

def rotate(l: list, n: int):
    """Rotate a list by n positions
    >>> rotate([5, 3, 5, 2, 3, 3, 9, 0, 123], 3)
    [3, 3, 9, 0, 123, 5, 3, 5, 2]
    """

def rotate_inplace(l: list, n: int):
    """Rotate a list by n positions in place
    >>> l = [5, 3, 5, 2, 3, 3, 9, 0, 123]
    >>> rotate_inplace(l, 3)
    >>> l
    [3, 3, 9, 0, 123, 5, 3, 5, 2]
    """

def rotate_left(l: list, n: int):
    """Rotate a list to the left by n positions
    >>> rotate_left([5, 3, 5, 2, 3, 3, 9, 0, 123], 3)
    [2, 3, 3, 9, 0, 123, 5, 3, 5]
    """

def rotate_left_inplace(l: list, n: int):
    """Rotate a list to the left by n positions in place
    >>> l = [5, 3, 5, 2, 3, 3, 9, 0, 123]
    >>> rotate_left_inplace(l, 3)
    >>> l
    [2, 3, 3, 9, 0, 123, 5, 3, 5]
    """

def rotate_right(l: list, n: int):
    """Rotate a list to the right by n positions
    >>> rotate_right([5, 3, 5, 2, 3, 3, 9, 0, 123], 3)
    [3, 3, 9, 0, 123, 5, 3, 5, 2]
    """

def rotate_right_inplace(l: list, n: int):
    """Rotate a list to the right by n positions in place
    >>> l = [5, 3, 5, 2, 3, 3, 9, 0, 123]
    >>> rotate_right_inplace(l, 3)
    >>> l
    [3, 3, 9, 0