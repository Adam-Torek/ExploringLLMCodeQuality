def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    >>> pairs_sum_to_zero([1, 3, 5, 0])
    False
    >>> pairs_sum_to_zero([1, 3, -2, 1])
    False
    >>> pairs_sum_to_zero([1, 2, 3, 7])
    False
    >>> pairs_sum_to_zero([2, 4, -5, 3, 5, 7])
    True
    >>> pairs_sum_to_zero([1])
    False
    """
    # First, we check if the list is empty or contains only one element.
    # If so, we return False.
    if len(l) < 2:
        return False

    # We create a dictionary to store the elements of the list as keys,
    # and their indices as values.
    # This allows us to find the index of an element in O(1) time.
    d = {}
    for i, num in enumerate(l):
        # We check if the negative of the current number is in the dictionary.
        # If so, it means that there are two numbers in the list that sum to zero.
        # We return True and exit the function.
        if -num in d:
            return True
        # We add the current number and its index to the dictionary.
        d[num] = i

    # If we reach this point, it means that no two numbers in the list sum to zero.
    # We return False.
    return False

# Test cases
if __name__ == '__main__':
    import doctest
    doctest.testmod()