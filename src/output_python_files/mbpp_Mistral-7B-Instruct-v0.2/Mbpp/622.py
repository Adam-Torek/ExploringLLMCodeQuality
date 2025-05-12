"""
Write a function to find the median of two sorted lists of same size.
assert get_median([1, 12, 15, 26, 38], [2, 13, 17, 30, 45], 5) == 16.0
"""
def merge_lists(list1, list2):
    merged_list = []
    i = j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1

    merged_list += list1[i:]
    merged_list += list2[j:]

    return merged_list

def get_median(list1, list2, size):
    merged_list = merge_lists(list1, list2)
    mid = len(merged_list) // 2

    if len(merged_list) % 2 == 0:
        return (merged_list[mid] + merged_list[mid - 1]) / 2.0
    else:
        return merged_list[mid]

assert get_median([1, 12, 15, 26, 38], [2, 13, 17, 30, 45], 5) == 16.0
assert get_median([1, 2, 3, 4, 5], [6, 7, 8, 9, 10], 5) == 6.0
assert get_median([1, 2, 3, 4, 5], [6, 7, 8, 9, 10], 6) == 5.5
assert get_median([1, 2, 3, 4, 5], [6, 7, 8, 9, 10], 1) == 3.0
assert get_median([1, 2, 3, 4, 5], [6, 7, 8, 9, 10], 7) == 6.0