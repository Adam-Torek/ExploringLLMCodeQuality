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
    a = None
    b = None
    for num in lst:
        if num < 0:
            if a is None or num > a:
                a = num
        elif num > 0:
            if b is None or num < b:
                b = num
    return a, b


# Test the function
print(largest_smallest_integers([2, 4, 1, 3, 5, 7])) # None, 1
print(largest_smallest_integers([])) # None, None
print(largest_smallest_integers([0])) # None, None