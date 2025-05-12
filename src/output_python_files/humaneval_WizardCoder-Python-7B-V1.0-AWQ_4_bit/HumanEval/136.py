def largest_smallest_integers(lst):
    '''
    Create a function that returns a tuple (a, b), where 'a' is
    the largest of negative integers, and 'b' is the smallest
    of positive integers in a list.
    If there is no negative or positive integers, return them as None.

    Examples:
    largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)
    largest_smallest_integers([]) == (None, None)
    largest_smallest_integers([0]) == (None, None)
    '''
    neg_int = None
    pos_int = None
    for i in lst:
        if i < 0:
            if neg_int is None or i > neg_int:
                neg_int = i
        elif i > 0:
            if pos_int is None or i < pos_int:
                pos_int = i
    return (neg_int, pos_int)


# Test cases
print(largest_smallest_integers([2, 4, 1, 3, 5, 7])) # (None, 1)
print(largest_smallest_integers([])) # (None, None)
print(largest_smallest_integers([0])) # (None, None)
print(largest_smallest_integers([-1, 2, 3, 4, 5, 6, 7, 8, 9])) # (-1, 1)
print(largest_smallest_integers([-5, -3, -2, -1, 0, 1, 2, 3, 4])) # (-5, 0)
print(largest_smallest_integers([-1, -2, -3, -4, -5, 1, 2, 3, 4])) # (-5, 1)
print(largest_smallest_integers([1, 2, 3, 4, 5, 6, 7, 8, 9])) # (None, None)
print(largest_smallest_integers([-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9])) # (-1, 1)
print(largest_smallest_integers([-5, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9])) # (-5, 1)
print(largest_smallest_integers([-1, -2, -3, -4, -5, -6, -7, -8, -9])) # (-9, None)
print(largest_smallest_integers([1, 2, 3, 4, 5, 6, 7, 8, 9])) # (None, None)
print(largest_smallest_integers([-1, -2, -3, -4, -5, -6, -7, -8, -9])) # (-9, None)
print(largest_smallest_integers([1, 2, 3, 4, 5, 6, 7, 8, 9])) # (None, None)
print(largest_smallest_integers([-1, -2, -3, -4, -5, -6, -7, -8, -9])) # (-9, None)
print(largest_smallest_integers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) # (None, 1)
print(largest_smallest_integers([-1, -2, -3, -4, -5, -6, -7, -8, -9, 10])) # (-9, 1)
print(largest_smallest_integers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) # (None, None)
print(largest_smallest_integers([-1, -2, -3, -4, -5, -6, -7