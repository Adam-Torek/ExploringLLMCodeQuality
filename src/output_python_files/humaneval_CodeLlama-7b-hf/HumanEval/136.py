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
    # Your code here
    a = None
    b = None
    for i in lst:
        if i < 0:
            if a is None:
                a = i
            else:
                if i > a:
                    a = i
        else:
            if b is None:
                b = i
            else:
                if i < b:
                    b = i
    return a, b


def largest_smallest_integers_v2(lst):
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
    # Your code here
    a = None
    b = None
    for i in lst:
        if i < 0:
            if a is None:
                a = i
            else:
                if i > a:
                    a = i
        else:
            if b is None:
                b = i
            else:
                if i < b:
                    b = i
    return a, b


def largest_smallest_integers_v3(lst):
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
    # Your code here
    a = None
    b = None
    for i in lst:
        if i < 0:
            if a is None:
                a = i
            else:
                if i > a:
                    a = i
        else:
            if b is None:
                b = i
            else:
                if i < b:
                    b = i
    return a, b


def largest_smallest_integers_v4(lst):
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
    # Your code here
    a = None
    b = None
    for i in lst:
        if i < 0:
            if a is None:
                a = i
            else:
                if i > a:
                    a = i
        else:
            if b is None:
                b = i
            else:
                if i < b:
                    b = i