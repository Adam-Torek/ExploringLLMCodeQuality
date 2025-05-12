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
    # sort the list
    x.sort()
    # create a set to store unique digits
    unique_set = set()
    # iterate over the list
    for i in x:
        # check if the digit is even
        if i % 2 == 0:
            continue
        # check if the digit is already in the set
        if i in unique_set:
            continue
        # add the digit to the set
        unique_set.add(i)
    # convert the set to a list
    unique_list = list(unique_set)
    return unique_list


if __name__ == '__main__':
    # test the function
    print(unique_digits([15, 33, 1422, 1]))
    print(unique_digits([152, 323, 1422, 10]))