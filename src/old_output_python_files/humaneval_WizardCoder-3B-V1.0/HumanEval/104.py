def unique_digits(x):
    """Given a list of positive integers x. return a sorted list of all 
    elements that hasn't any even digit.

    Note: Returned list should be sorted in increasing order.
    
    For example:
    >>> unique_digits([15, 33, 1422, 1])
    [1, 15, 33]
    >>> unique_digits([152, 323, 1422, 10])
    []
    """

#     # Remove even digits from the list
#     x = [num for num in x if num % 2!= 0]

#     # Sort the list in increasing order
#     x.sort()

#     return x

#     # Alternative solution using set
#     return sorted(set(x) - set([num for num in x if num % 2 == 0]))

    # Another solution using list comprehension
    return sorted([num for num in x if num % 2!= 0])<|endoftext|>