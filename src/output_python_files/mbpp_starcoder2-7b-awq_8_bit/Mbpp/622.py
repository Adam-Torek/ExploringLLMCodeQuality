"""
Write a function to find the median of two sorted lists of same size.
assert get_median([1, 12, 15, 26, 38], [2, 13, 17, 30, 45], 5) == 16.0
"""

def get_median(list1, list2, size):
    if size % 2 == 0:
        return (get_kth(list1, list2, size // 2) + get_kth(list1, list2, size // 2 + 1)) / 2
    else:
        return get_kth(list1, list2, size // 2 + 1)

def get_kth(list1, list2, k):
    if len(list1) == 0:
        return list2[k - 1]
    if len(list2) == 0:
        return list1[k - 1]
    if k == 1:
        return min(list1[0], list2[0])
    new_k = k // 2
    if len(list1) >= new_k and len(list2) >= new_k:
        pivot1 = list1[new_k - 1]
        pivot2 = list2[new_k - 1]
        if pivot1 <= pivot2:
            return get_kth(list1[new_k:], list2, k - new_k)
        else:
            return get_kth(list1, list2[new_k:], k - new_k)
    elif len(list1) >= new_k:
        return get_kth(list1[new_k:], list2, k - new_k)
    else:
        return get_kth(list1, list2[new_k:], k - new_k)

assert get_median([1, 12, 15, 26, 38], [2, 13, 17, 30, 45], 5) == 16.0
assert get_median([1, 12, 15, 26, 38], [2, 13, 17, 30, 45], 6) == 17.0
assert get_median([1, 12, 15, 26, 38], [2, 13, 17, 30, 45], 7) == 18.0
assert get_median([1, 12, 15, 26, 38], [2, 13, 17, 30, 45], 8) == 19.0
assert get_median([1, 12, 15, 26, 38], [2, 13, 17, 30, 45], 9) == 20.0
assert get_median([1, 12, 15, 26, 38], [2, 13, 17, 30, 45], 10) == 21.0
assert get_median([1, 12, 15, 26, 38], [2, 13, 17, 30, 45], 11) == 22.0
assert get_median([1, 12, 15, 26, 38], [2, 13, 17, 30, 45], 12) == 23.0
assert get_median([1, 12, 15, 26, 38], [2, 13, 17, 30, 45], 13) == 24.0
assert get_median([1, 12, 15, 26, 38], [2, 13, 17, 30, 45], 14) == 25.0
assert get_median([1, 12, 15, 26, 38], [2, 13, 17, 30, 45], 15) == 26.0
assert get_median([1, 12, 15, 26, 38], [2,