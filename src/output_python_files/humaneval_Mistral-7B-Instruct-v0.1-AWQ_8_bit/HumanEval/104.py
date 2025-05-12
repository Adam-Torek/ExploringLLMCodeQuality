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
    # create a set of digits
    digits = set()
    # iterate over the list
    for num in x:
        # check if the number has any even digit
        if any(num % digit == 0 for digit in range(10)):
            continue
        # check if the number has any digit
        if not any(num % digit == 0 for digit in range(10)):
            digits.add(num)
    # return the sorted list of unique digits
    return sorted(list(digits))


if __name__ == '__main__':
    print(unique_digits([15, 33, 1422, 1]))
    print(unique_digits([152, 323, 1422, 10]))