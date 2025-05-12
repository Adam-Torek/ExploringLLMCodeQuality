def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    l' = l[:]
    for i in range(1, len(l), 2):
        l'[i] = sorted(l[i:i+2])[0]
    return l'


def sort_odd(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the even indicies, while its values at the odd indicies are equal
    to the values of the odd indicies of l, but sorted.
    >>> sort_odd([1, 2, 3])
    [1, 2, 3]
    >>> sort_odd([5, 6, 3, 4])
    [5, 6, 3, 4]
    """
    l' = l[:]
    for i in range(1, len(l), 2):
        l'[i] = sorted(l[i:i+2])[-1]
    return l'


def sort_even_odd(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even_odd([1, 2, 3])
    [1, 2, 3]
    >>> sort_even_odd([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    l' = l[:]
    for i in range(1, len(l), 2):
        l'[i] = sorted(l[i:i+2])[0]
    return l'


def sort_odd_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the even indicies, while its values at the odd indicies are equal
    to the values of the odd indicies of l, but sorted.
    >>> sort_odd_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_odd_even([5, 6, 3, 4])
    [5, 6, 3, 4]
    """
    l' = l[:]
    for i in range(1, len(l), 2):
        l'[i] = sorted(l[i:i+2])[-1]
    return l'


def sort_even_odd_even_odd(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even_odd_even_odd([1, 2, 3, 4, 5, 6])
    [1, 2, 3, 4, 5, 6]
    >>> sort_even_odd_even_odd([5, 6, 3, 4, 2, 1])
    [2, 3, 4, 5, 6]
    """
    l' = l[:]
    for i in range(1, len(l), 2):
        l'[i] = sorted(l[i:i+2])[0]
    return l'


def sort_odd_even_odd_