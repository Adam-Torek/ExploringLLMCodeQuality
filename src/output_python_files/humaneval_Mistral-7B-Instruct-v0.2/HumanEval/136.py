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
        largest_neg = max(negatives)
    else:
        largest_neg = None

    if positives:
        smallest_pos = min(positives)
    else:
        smallest_pos = None

    return largest_neg, smallest_pos

# Testing
print(largest_smallest_integers([2, 4, 1, 3, 5, 7]))
print(largest_smallest_integers([]))
print(largest_smallest_integers([0]))
print(largest_smallest_integers([-1, -2, -3, 1, 2, 3]))
print(largest_smallest_integers([-1, 1, 2, 3, 4, 5]))
print(largest_smallest_integers([-1, -2, -3, -4, -5, -6]))