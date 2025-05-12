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
    negatives = [num for num in lst if num < 0]
    positives = [num for num in lst if num > 0]

    if not negatives and not positives:
        return None, None

    if negatives:
        largest_negative = max(negatives)
    else:
        largest_negative = None

    if positives:
        smallest_positive = min(positives)
    else:
        smallest_positive = None

    return largest_negative, smallest_positive

# Testing
print(largest_smallest_integers([2, 4, 1, 3, 5, 7])) # (None, 1)
print(largest_smallest_integers([])) # (None, None)
print(largest_smallest_integers([0])) # (None, None)
print(largest_smallest_integers([-1, -2, -3, 1, 2, 3])) # (-3, 1)
print(largest_smallest_integers([-1, 1, 2, 3, 4, 5])) # (-1, 1)
print(largest_smallest_integers([-1, -2, -3, -4, 1, 2, 3, 4, 5])) # (-4, 1)
print(largest_smallest_integers([-1, -2, -3, -4, -5, 1, 2, 3, 4, 5])) # (-5, 1)
print(largest_smallest_integers([-1, -2, -3, -4, -5, -6, 1, 2, 3, 4, 5])) # (-6, 1)
print(largest_smallest_integers([-1, -2, -3, -4, -5, -6, -7, 1, 2, 3, 4, 5])) # (-7, 1)
print(largest_smallest_integers([-1, -2, -3, -4, -5, -6, -7, -8, 1, 2, 3, 4, 5])) # (-8, 1)
print(largest_smallest_integers([-1, -2, -3, -4, -5, -6, -7, -8, -9, 1, 2, 3, 4, 5])) # (-9, 1)
print(largest_smallest_integers([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, 1, 2, 3, 4, 5])) # (-10, 1)
print(largest_smallest_integers([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, 1, 2, 3, 4, 5])) # (-11, 1)
print(largest_smallest_integers([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, 1, 2, 3, 4, 5])) # (-12, 1)
print(largest_smallest_integers([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13,