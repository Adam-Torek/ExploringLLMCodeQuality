def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    if len(l) == 0:
        return None
    max_num = l[0]
    for num in l:
        if num > max_num:
            max_num = num
    return max_num


if __name__ == "__main__":
    import doctest
    doctest.testmod()