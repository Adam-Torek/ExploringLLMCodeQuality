def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    >>> pairs_sum_to_zero([1, 3, 5, 0])
    False
    >>> pairs_sum_to_zero([1, 3, -2, 1])
    False
    >>> pairs_sum_to_zero([1, 2, 3, 7])
    False
    >>> pairs_sum_to_zero([2, 4, -5, 3, 5, 7])
    True
    >>> pairs_sum_to_zero([1])
    False
    """
    # your code here
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            if l[i] + l[j] == 0:
                return True
    return False


def pairs_sum_to_zero_2(l):
    """
    pairs_sum_to_zero_2 takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    >>> pairs_sum_to_zero_2([1, 3, 5, 0])
    False
    >>> pairs_sum_to_zero_2([1, 3, -2, 1])
    False
    >>> pairs_sum_to_zero_2([1, 2, 3, 7])
    False
    >>> pairs_sum_to_zero_2([2, 4, -5, 3, 5, 7])
    True
    >>> pairs_sum_to_zero_2([1])
    False
    """
    # your code here
    d = {}
    for i in l:
        if i in d:
            return True
        else:
            d[i*-1] = True
    return False


def pairs_sum_to_zero_3(l):
    """
    pairs_sum_to_zero_3 takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    >>> pairs_sum_to_zero_3([1, 3, 5, 0])
    False
    >>> pairs_sum_to_zero_3([1, 3, -2, 1])
    False
    >>> pairs_sum_to_zero_3([1, 2, 3, 7])
    False
    >>> pairs_sum_to_zero_3([2, 4, -5, 3, 5, 7])
    True
    >>> pairs_sum_to_zero_3([1])
    False
    """
    # your code here
    d = {}
    for i in l:
        if i in d:
            return True
        else:
            d[0-i] = True
    return False


def pairs_sum_to_zero_4(l):
    """
    pairs_sum_to_zero_4 takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    >>> pairs_sum_to_zero_4([1, 3, 5, 0])
    False
    >>> pairs_sum_to_zero_4([1, 3, -2, 1])
    False
    >>> pairs_sum_to_zero_4([1, 2, 3, 7])
    False
    >>> pairs_sum_to_zero_4([2, 4, -5, 3, 5, 7])
    True
    >>> pairs_sum_to_zero_4([1])
    False
    """
    # your code here
    d = {}
    for i in l:
        if i in d:
            return True
        else:
            d[i] = True
    return False


def pairs_sum_to_zero_5(l):
    """
    pairs_sum_to_zero_5 takes a list of integers as an input.
    it returns True if