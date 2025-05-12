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
    digits = []
    for num in x:
        for digit in str(num):
            if digit not in digits and int(digit) % 2 != 0:
                digits.append(digit)
    return [int(digit) for digit in ''.join(sorted(digits))]

# Testing
if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print(unique_digits([15, 33, 1422, 1]))
    print(unique_digits([152, 323, 1422, 10]))