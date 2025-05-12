def is_sorted(lst):
    '''
    Given a list of numbers, return whether or not they are sorted
    in ascending order. If list has more than 1 duplicate of the same
    number, return False. Assume no negative numbers and only integers.

    Examples
    is_sorted([5]) ➞ True
    is_sorted([1, 2, 3, 4, 5]) ➞ True
    is_sorted([1, 3, 2, 4, 5]) ➞ False
    is_sorted([1, 2, 3, 4, 5, 6]) ➞ True
    is_sorted([1, 2, 3, 4, 5, 6, 7]) ➞ True
    is_sorted([1, 3, 2, 4, 5, 6, 7]) ➞ False
    is_sorted([1, 2, 2, 3, 3, 4]) ➞ True
    is_sorted([1, 2, 2, 2, 3, 4]) ➞ False
    '''
    if len(lst) < 2:
        return True
    for i in range(len(lst)-1):
        if lst[i] > lst[i+1]:
            return False
    return True


def is_sorted_by_sum(lst):
    '''
    Given a list of numbers, return whether or not they are sorted
    in ascending order by their sum. If list has more than 1 duplicate
    of the same number, return False. Assume no negative numbers and only integers.

    Examples
    is_sorted_by_sum([5]) ➞ True
    is_sorted_by_sum([1, 2, 3, 4, 5]) ➞ True
    is_sorted_by_sum([1, 3, 2, 4, 5]) ➞ False
    is_sorted_by_sum([1, 2, 3, 4, 5, 6]) ➞ True
    is_sorted_by_sum([1, 2, 3, 4, 5, 6, 7]) ➞ True
    is_sorted_by_sum([1, 3, 2, 4, 5, 6, 7]) ➞ False
    is_sorted_by_sum([1, 2, 2, 3, 3, 4]) ➞ True
    is_sorted_by_sum([1, 2, 2, 2, 3, 4]) ➞ False
    '''
    if len(lst) < 2:
        return True
    for i in range(len(lst)-1):
        if lst[i] + lst[i+1] != lst[i+1] + lst[i]:
            return False
    return True


def is_sorted_by_sum_and_count(lst):
    '''
    Given a list of numbers, return whether or not they are sorted
    in ascending order by their sum and count. If list has more than 1
    duplicate of the same number, return False. Assume no negative numbers
    and only integers.

    Examples
    is_sorted_by_sum_and_count([5]) ➞ True
    is_sorted_by_sum_and_count([1, 2, 3, 4, 5]) ➞ True
    is_sorted_by_sum_and_count([1, 3, 2, 4, 5]) ➞ False
    is_sorted_by_sum_and_count([1, 2, 3, 4, 5, 6]) ➞ True
    is_sorted_by_sum_and_count([1, 2, 3, 4, 5, 6, 7]) ➞ True
    is_sorted_by_sum_and_count([1, 3, 2, 4,