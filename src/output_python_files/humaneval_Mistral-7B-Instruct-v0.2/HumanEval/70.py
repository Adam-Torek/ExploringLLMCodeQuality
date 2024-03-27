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
    if len(lst) == 0:
        return []
    result = [lst[0]]
    for i in lst[1:]:
        if i < result[-1]:
            result.append(i)
        else:
            j = 0
            while i > result[j]:
                j += 1
            result[j] = i
    return result

# Testing
print(strange_sort_list([1, 2, 3, 4]))
print(strange_sort_list([5, 5, 5, 5]))
print(strange_sort_list([]))
print(strange_sort_list([1, 1, 1, 1, 1]))
print(strange_sort_list([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))</s>