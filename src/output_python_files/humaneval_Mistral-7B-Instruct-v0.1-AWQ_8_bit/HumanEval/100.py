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
    if n % 2 == 0:
        return [n, n+2, n+4]
    else:
        return [n, n+2, n+3]


def main():
    for n in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        print(make_a_pile(n))


if __name__ == '__main__':
    main()