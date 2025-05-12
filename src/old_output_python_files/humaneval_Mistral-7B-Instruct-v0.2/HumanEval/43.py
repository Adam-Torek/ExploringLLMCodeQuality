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
    # First, we check if the list is empty or has only one element.
    # In both cases, the answer is False.
    if len(l) < 2:
        return False

    # We create a dictionary to store the elements of the list as keys,
    # and their indices as values. This allows us to find the index of
    # an element in O(1) time.
    elements = {}
    for i, el in enumerate(l):
        # We check if the negative of the current element is in the dictionary.
        # If it is, then we have found a pair of elements that sum to zero.
        if el in elements:
            return True
        # We add the current element to the dictionary.
        elements[abs(el)] = i

    # If we have reached this point, it means that no pair of elements
    # in the list sums to zero.
    return False

# Test cases
if __name__ == '__main__':
    import doctest
    doctest.testmod()