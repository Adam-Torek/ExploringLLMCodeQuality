def strange_sort_list(lst):
    '''
    Given list of integers, return list in strange order.
    Strange sorting, is when you start with the minimum value,
    then maximum of the remaining integers, then minimum and so on.

    Examples:
    strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    strange_sort_list([]) == []
    '''
    # your code here
    if len(lst) == 0:
        return []
    else:
        lst.sort()
        return lst[0:1] + lst[-1:] + strange_sort_list(lst[1:-1])


def strange_sort_list_2(lst):
    '''
    Given list of integers, return list in strange order.
    Strange sorting, is when you start with the minimum value,
    then maximum of the remaining integers, then minimum and so on.

    Examples:
    strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    strange_sort_list([]) == []
    '''
    # your code here
    if len(lst) == 0:
        return []
    else:
        lst.sort()
        return [lst[0]] + [lst[-1]] + strange_sort_list_2(lst[1:-1])


def strange_sort_list_3(lst):
    '''
    Given list of integers, return list in strange order.
    Strange sorting, is when you start with the minimum value,
    then maximum of the remaining integers, then minimum and so on.

    Examples:
    strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    strange_sort_list([]) == []
    '''
    # your code here
    if len(lst) == 0:
        return []
    else:
        lst.sort()
        return [lst[0]] + [lst[-1]] + strange_sort_list_3(lst[1:-1])


def strange_sort_list_4(lst):
    '''
    Given list of integers, return list in strange order.
    Strange sorting, is when you start with the minimum value,
    then maximum of the remaining integers, then minimum and so on.

    Examples:
    strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    strange_sort_list([]) == []
    '''
    # your code here
    if len(lst) == 0:
        return []
    else:
        lst.sort()
        return [lst[0]] + [lst[-1]] + strange_sort_list_4(lst