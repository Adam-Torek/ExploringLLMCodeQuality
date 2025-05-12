def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    l_prime = list(l)
    l_prime.sort()
    return l_prime


def sort_odd(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the even indicies, while its values at the odd indicies are equal
    to the values of the odd indicies of l, but sorted.
    >>> sort_odd([1, 2, 3])
    [1, 2, 3]
    >>> sort_odd([5, 6, 3, 4])
    [5, 6, 3, 4]
    """
    l_prime = list(l)
    l_prime.sort()
    return l_prime


def sort_even_odd(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even_odd([1, 2, 3])
    [1, 2, 3]
    >>> sort_even_odd([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    l_prime = list(l)
    l_prime.sort()
    return l_prime


def sort_even_odd_reverse(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted in descending order.
    >>> sort_even_odd_reverse([1, 2, 3])
    [3, 2, 1]
    >>> sort_even_odd_reverse([5, 6, 3, 4])
    [6, 5, 4, 3]
    """
    l_prime = list(l)
    l_prime.sort(reverse=True)
    return l_prime


def sort_even_odd_reverse_sorted(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted in descending order.
    >>> sort_even_odd_reverse_sorted([1, 2, 3])
    [3, 2, 1]
    >>> sort_even_odd_reverse_sorted([5, 6, 3, 4])
    [6, 5, 4, 3]
    """
    l_prime = list(l)
    l_prime.sort(reverse=True)
    return l_prime


def sort_even_odd_reverse_sorted_reverse(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted in descending order.
    >>> sort_even_odd_reverse_sorted_reverse([1, 2, 3])
    [3, 2, 1]
    >>> sort_even_odd_reverse_sorted_reverse([5, 6, 3, 4])
    [6, 5, 4, 3]
    """
    l_prime = list(l)
    l_prime.sort(reverse=True)
    return l_prime


def sort_even_odd