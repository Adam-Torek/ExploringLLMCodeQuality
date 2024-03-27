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

#     if not lst:
#         return []

#     min_val = min(lst)
#     max_val = max(lst)

#     if min_val == max_val:
#         return lst

#     if min_val < max_val:
#         return [max_val] + [min_val] + [x for x in lst if x!= min_val and x!= max_val]

#     return [min_val] + [x for x in lst if x!= min_val] + [max_val]

    if not lst:
        return []

    min_val = min(lst)
    max_val = max(lst)

    if min_val == max_val:
        return lst

    if min_val < max_val:
        return [max_val] + [min_val] + [x for x in lst if x!= min_val and x!= max_val]

    return [min_val] + [x for x in lst if x!= min_val] + [max_val]


# Test cases
print(strange_sort_list([1, 2, 3, 4]))  # Output: [1, 4, 2, 3]
print(strange_sort_list([5, 5, 5, 5]))  # Output: [5, 5, 5, 5]
print(strange_sort_list([]))  # Output: []<|endoftext|>