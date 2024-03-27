def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    l_copy = l.copy()
    even_indices = [i for i, x in enumerate(l_copy) if i % 2 == 0]
    even_values = [l_copy[i] for i in even_indices]
    even_values.sort()
    for i, x in enumerate(l_copy):
        if i % 2 == 0:
            l_copy[i] = even_values[i // 2]
    return l_copy


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print(sort_even([5, 6, 3, 4]))
    print(sort_even([1, 2, 3]))
    print(sort_even([1, 2, 3, 4, 5, 6]))
    print(sort_even([1, 2, 3, 4, 5, 6, 7]))
    print(sort_even([1, 2, 3, 4, 5, 6, 7, 8]))</s>