def make_a_pile(n):
    """
    Given a positive integer n, you have to make a pile of n levels of stones.
    The first level has n stones.
    The number of stones in the next level is:
        - the next odd number if n is odd.
        - the next even number if n is even.
    Return the number of stones in each level in a list, where element at index
    i represents the number of stones in the level (i+1).

    Examples:
    >>> make_a_pile(3)
    [3, 5, 7]
    """
    result = []
    for i in range(n):
        if n % 2 == 0:
            result.append(n + 2 * i)
        else:
            result.append(n + 2 * i + 1)
    return result



def make_a_pile_2(n):
    """
    Given a positive integer n, you have to make a pile of n levels of stones.
    The first level has n stones.
    The number of stones in the next level is:
        - the next odd number if n is odd.
        - the next even number if n is even.
    Return the number of stones in each level in a list, where element at index
    i represents the number of stones in the level (i+1).

    Examples:
    >>> make_a_pile_2(3)
    [3, 5, 7]
    """
    return [n + 2 * i for i in range(n)]



if __name__ == "__main__":
    import doctest

    doctest.testmod()