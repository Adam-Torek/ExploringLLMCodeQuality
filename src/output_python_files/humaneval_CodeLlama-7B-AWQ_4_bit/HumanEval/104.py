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
    # your code here
    return sorted(list(set([int(i) for i in str(x) if int(i) % 2 != 0])))


if __name__ == '__main__':
    print(unique_digits([15, 33, 1422, 1]))
    print(unique_digits([152, 323, 1422, 10]))
    print(unique_digits([15, 33, 1422, 1, 15, 33, 1422, 1]))
    print(unique_digits([15, 33, 1422, 1, 15, 33, 1422, 1, 15, 33, 1422, 1]))
    print(unique_digits([15, 33, 1422, 1, 15, 33, 1422, 1, 15, 33, 1422, 1, 15, 33, 1422, 1]))
    print(unique_digits([15, 33, 1422, 1, 15, 33, 1422, 1, 15, 33, 1422, 1, 15, 33, 1422, 1, 15, 33, 1422, 1]))
    print(unique_digits([15, 33, 1422, 1, 15, 33, 1422, 1, 15, 33, 1422, 1, 15, 33, 1422, 1, 15, 33, 1422, 1, 15, 33, 1422, 1]))
    print(unique_digits([15, 33, 1422, 1, 15, 33, 1422, 1, 15, 33, 1422, 1, 15, 33, 1422, 1, 15, 33, 1422, 1, 15, 33, 1422, 1, 15, 33, 1422, 1]))
    print(unique_digits([15, 33, 1422, 1, 15, 33, 1422, 1, 15, 33, 1422, 1, 15, 33, 1422, 1, 15, 33, 1422, 1, 15, 33, 14