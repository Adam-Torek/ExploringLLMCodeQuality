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

#     if len(lst) == 0:
#         return []
#     elif len(lst) == 1:
#         return lst
#     else:
#         min_val = min(lst)
#         max_val = max(lst)
#         min_index = lst.index(min_val)
#         max_index = lst.index(max_val)
#         if min_index < max_index:
#             return [min_val] + strange_sort_list(lst[:min_index] + lst[min_index+1:max_index] + lst[max_index+1:]) + [max_val]
#         else:
#             return [max_val] + strange_sort_list(lst[:max_index] + lst[max_index+1:min_index] + lst[min_index+1:]) + [min_val]

#     return [min(lst)] + strange_sort_list(lst[1:]) + [max(lst)]

#     if len(lst) == 0:
#         return []
#     elif len(lst) == 1:
#         return lst
#     else:
#         min_val = min(lst)
#         max_val = max(lst)
#         min_index = lst.index(min_val)
#         max_index = lst.index(max_val)
#         if min_index < max_index:
#             return [min_val] + strange_sort_list(lst[:min_index] + lst[min_index+1:max_index] + lst[max_index+1:]) + [max_val]
#         else:
#             return [max_val] + strange_sort_list(lst[:max_index] + lst[max_index+1:min_index] + lst[min_index+1:]) + [min_val]

#     return [min(lst)] + strange_sort_list(lst[1:]) + [max(lst)]

#     if len(lst) == 0:
#         return []
#     elif len(lst) == 1:
#         return lst
#     else:
#         min_val = min(lst)
#         max_val = max(lst)
#         min_index = lst.index(min_val)
#         max_index = lst.index(max_val)
#         if min_index < max_index:
#             return [min_val] + strange_sort_list(lst[:min_index] + lst[min_index+1:max_index] + lst[max_index+1:]) + [max_val]
#         else:
#             return [max_val] + strange_sort_list(lst[:max_index] + lst[max_index+1:min_index] + lst[min_index+1:]) + [min_val]

#     return [min(lst)] + strange_sort_list(lst[1:]) + [max(lst)]