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
    if not lst:
        return []
    min_val = min(lst)
    max_val = max(lst)
    lst.remove(min_val)
    lst.remove(max_val)
    return [min_val, max_val] + strange_sort_list(lst)



def test_strange_sort_list():
    assert strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    assert strange_sort_list([5, 5, 5, 5]) == [5, 5, 5]
    assert strange_sort_list([]) == []
    assert strange_sort_list([1, 2, 3, 4, 5, 6, 7, 8, 9]) == [1, 9, 2, 8, 3, 7, 4, 5, 6]
    assert strange_sort_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]
    assert strange_sort_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == [1, 11, 2, 9, 3, 8, 4, 7, 5, 6]
    assert strange_sort_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == [1, 12, 2, 11, 3, 10, 4, 9, 7, 6]
    assert strange_sort_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]) == [1, 13, 2, 12, 3, 11, 4, 10, 9, 7]
    assert strange_sort_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]) == [1, 14, 2, 13, 3, 12, 4, 11, 9, 8]
    assert strange_sort_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10,