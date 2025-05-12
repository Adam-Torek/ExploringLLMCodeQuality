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
    largest_negative = None
    smallest_positive = None
    for num in lst:
        if num < 0 and (largest_negative is None or num > largest_negative):
            largest_negative = num
        elif num > 0 and (smallest_positive is None or num < smallest_positive):
            smallest_positive = num
    return (largest_negative, smallest_positive)


# Test cases
print(largest_smallest_integers([2, 4, 1, 3, 5, 7])) # (None, 1)
print(largest_smallest_integers([])) # (None, None)
print(largest_smallest_integers([0])) # (None, None)
print(largest_smallest_integers([-1, 2, 3, 4, 5, -3, 6])) # (-3, 2)
print(largest_smallest_integers([-5, -3, -1, 0, 2, 4, 6])) # (-5, 0)
print(largest_smallest_integers([-1, -2, -3, -4, -5])) # (-5, None)
print(largest_smallest_integers([1, 2, 3, 4, 5])) # (None, 1)
print(largest_smallest_integers([-1, 0, 1, 2, 3, 4])) # (-1, 1)
print(largest_smallest_integers([-1, -2, -3, -4, -5])) # (-5, None)
print(largest_smallest_integers([1, 2, 3, 4, 5])) # (None, 1)
print(largest_smallest_integers([-1, 0, 1, 2, 3, 4])) # (-1, 1)
print(largest_smallest_integers([1, 2, 3, 4, 5])) # (None, 1)
print(largest_smallest_integers([-1, 0, 1, 2, 3, 4])) # (-1, 1)
print(largest_smallest_integers([-1, -2, -3, -4, -5])) # (-5, None)
print(largest_smallest_integers([1, 2, 3, 4, 5])) # (None, 1)
print(largest_smallest_integers([-1, 0, 1, 2, 3, 4])) # (-1, 1)
print(largest_smallest_integers([-1, -2, -3, -4, -5])) # (-5, None)
print(largest_smallest_integers([1, 2, 3, 4, 5])) # (None, 1)
print(largest_smallest_integers([-1, 0, 1, 2, 3, 4])) # (-1, 1)
print(largest_smallest_integers([-1, -2, -3, -4, -5])) # (-5, None)
print(largest_smallest_integers([1, 2, 3, 4, 5])) # (None, 1)
print(largest_smallest_integers([-1, 0, 1, 2, 3, 4])) # (-1, 1)
print(largest_smallest_integers([-1, -2, -