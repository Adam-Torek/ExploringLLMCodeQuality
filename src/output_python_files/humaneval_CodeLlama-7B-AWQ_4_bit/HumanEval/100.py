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
    # TODO: Write your code here
    if n == 0:
        return []
    elif n == 1:
        return [1]
    else:
        return [n] + make_a_pile(n + 1)


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
    # TODO: Write your code here
    if n == 0:
        return []
    elif n == 1:
        return [1]
    else:
        return [n] + make_a_pile_2(n + 1)


def make_a_pile_3(n):
    """
    Given a positive integer n, you have to make a pile of n levels of stones.
    The first level has n stones.
    The number of stones in the next level is:
        - the next odd number if n is odd.
        - the next even number if n is even.
    Return the number of stones in each level in a list, where element at index
    i represents the number of stones in the level (i+1).

    Examples:
    >>> make_a_pile_3(3)
    [3, 5, 7]
    """
    # TODO: Write your code here
    if n == 0:
        return []
    elif n == 1:
        return [1]
    else:
        return [n] + make_a_pile_3(n + 1)


def make_a_pile_4(n):
    """
    Given a positive integer n, you have to make a pile of n levels of stones.
    The first level has n stones.
    The number of stones in the next level is:
        - the next odd number if n is odd.
        - the next even number if n is even.
    Return the number of stones in each level in a list, where element at index
    i represents the number of stones in the level (i+1).

    Examples:
    >>> make_a_pile_4(3)
    [3, 5, 7]
    """
    # TODO: Write your code here
    if n == 0:
        return []
    elif n == 1:
        return [1]
    else:
        return [n] + make_a_pile_4(n + 1)


def make_a_pile_5(n):
    """
    Given a positive integer n, you have to make a pile of n levels of stones.
    The first level has n stones.
    The number of stones in the next level is:
        - the next odd number if n is odd.
        - the next even number if n is even.
    Return the number of stones in each level in a list, where element at index
    i represents the number of stones in the level (i+1).

    Examples:
    >>> make_a_pile_5(3)
    [3, 5, 7]
    """
    # TODO: Write your code here
    if