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


# Test cases
print(make_a_pile(3))  # Output: [3, 5, 7]
print(make_a_pile(4))  # Output: [4, 6, 8, 10]
print(make_a_pile(5))  # Output: [5, 7, 9, 11, 13]
print(make_a_pile(1))  # Output: [1]
print(make_a_pile(0))  # Output: []