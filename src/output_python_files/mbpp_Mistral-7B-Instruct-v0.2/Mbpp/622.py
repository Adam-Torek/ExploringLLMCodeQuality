"""
Write a function to find the median of two sorted lists of same size.
assert get_median([1, 12, 15, 26, 38], [2, 13, 17, 30, 45], 5) == 16.0
"""
def merge_lists(list1, list2):
    merged = []
    i = j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1
    merged += list1[i:]
    merged += list2[j:]
    return merged

def get_median(list1, list2, size):
    merged = merge_lists(list1, list2)
    if len(merged) % 2 == 0:
        return (merged[len(merged)//2] + merged[len(merged)//2 - 1]) / 2
    else:
        return merged[len(merged)//2]

assert get_median([1, 12, 15, 26, 38], [2, 13, 17, 30, 45], 5) == 16.0
assert get_median([1, 12, 15, 26, 38], [2, 13, 17, 30, 45], 6) == 16.5
assert get_median([1, 12, 15, 26, 38], [2, 13, 17, 30, 45], 4) == 15.0
assert get_median([1, 12, 15, 26, 38], [2, 13, 17, 30, 45], 3) == 15.0
assert get_median([1, 12, 15, 26, 38], [2, 13, 17, 30, 45], 2) == 15.0
assert get_median([1, 12, 15, 26, 38], [2, 13, 17, 30, 45], 1) == 15.0
assert get_median([1, 12, 15, 26, 38], [2, 13, 17, 30, 45], 7) == 17.0
assert get_median([1, 12, 15, 26, 38], [2, 13, 17, 30, 45], 8) == 17.0
assert get_median([1, 12, 15, 26, 38], [2, 13, 17, 30, 45], 9) == 17.0
assert get_median([1, 12, 15, 26, 38], [2, 13, 17, 30, 45], 10) == 17.0
assert get_median([1, 12, 15, 26, 38], [2, 13, 17, 30, 45], 11) == 17.0
assert get_median([1, 12, 15, 26, 38], [2, 13, 17, 30, 45], 12) == 17.0
assert get_median([1, 12, 15, 26, 38], [2, 13, 17, 30, 45], 13) == 17.0
assert get_median([1, 12, 15, 26, 38], [2, 13, 17, 30, 45],