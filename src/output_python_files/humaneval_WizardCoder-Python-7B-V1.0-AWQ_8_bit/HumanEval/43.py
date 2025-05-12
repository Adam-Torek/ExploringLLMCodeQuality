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
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            if l[i] + l[j] == 0:
                return True
    return False


# Test cases
print(pairs_sum_to_zero([1, 3, 5, 0])) # False
print(pairs_sum_to_zero([1, 3, -2, 1])) # False
print(pairs_sum_to_zero([1, 2, 3, 7])) # False
print(pairs_sum_to_zero([2, 4, -5, 3, 5, 7])) # True
print(pairs_sum_to_zero([1])) # False


# Test cases with negative numbers
print(pairs_sum_to_zero([-1, 2, 3, -4])) # True
print(pairs_sum_to_zero([-1, 2, 3, 4])) # False
print(pairs_sum_to_zero([-1, -2, 3, -4])) # True
print(pairs_sum_to_zero([-1, -2, 3, 4])) # False

# Test cases with repeated numbers
print(pairs_sum_to_zero([1, 2, 3, 4, 3, 5, 6, 7, 8, 9, 10, 11, 12])) # True
print(pairs_sum_to_zero([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])) # False
print(pairs_sum_to_zero([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 11])) # True
print(pairs_sum_to_zero([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 12])) # True
print(pairs_sum_to_zero([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])) # False

# Test cases with zero
print(pairs_sum_to_zero([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])) # True
print(pairs_sum_to_zero([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 0])) # True
print(pairs_sum_to_zero([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 1])) # True
print(pairs_sum_to_zero([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, -1])) # True
print(pairs_sum_to_zero([0, 1, 2, 3, 4, 5