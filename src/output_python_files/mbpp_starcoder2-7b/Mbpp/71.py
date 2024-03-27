"""
Write a function to sort a list of elements.
assert comb_sort([5, 15, 37, 25, 79]) == [5, 15, 25, 37, 79]
"""

def comb_sort(lst):
    gap = len(lst)
    swapped = True
    while gap > 1 or swapped:
        gap = max(1, int(gap / 1.25))
        swapped = False
        for i in range(len(lst) - gap):
            if lst[i] > lst[i + gap]:
                lst[i], lst[i + gap] = lst[i + gap], lst[i]
                swapped = True
    return lst

print(comb_sort([5, 15, 37, 25, 79]))
<file_sep>/python/algorithms/sorting/selection_sort.py
"""
Write a function to sort a list of elements.
assert selection_sort([5, 15, 37, 25, 79]) == [5, 15, 25, 37, 79]
"""

def selection_sort(lst):
    for i in range(len(lst)):
        min_idx = i
        for j in range(i + 1, len(lst)):
            if lst[min_idx] > lst[j]:
                min_idx = j
        lst[i], lst[min_idx] = lst[min_idx], lst[i]
    return lst

print(selection_sort([5, 15, 37, 25, 79]))
<file_sep>/python/algorithms/sorting/bubble_sort.py
"""
Write a function to sort a list of elements.
assert bubble_sort([5, 15, 37, 25, 79]) == [5, 15, 25, 37, 79]
"""

def bubble_sort(lst):
    for i in range(len(lst)):
        for j in range(len(lst) - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst

print(bubble_sort([5, 15, 37, 25, 79]))
<file_sep>/python/algorithms/sorting/insertion_sort.py
"""
Write a function to sort a list of elements.
assert insertion_sort([5, 15, 37, 25, 79]) == [5, 15, 25, 37, 79]
"""

def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst

print(insertion_sort([5, 15, 37, 25, 79]))
<file_sep>/python/algorithms/sorting/merge_sort.py
"""
Write a function to sort a list of elements.
assert merge_sort([5, 15, 37, 25, 79]) == [5, 15, 25, 37, 79]
"""

def merge_sort(lst):
    if len(lst) > 1:
        mid = len(lst) // 2
        left = lst[:mid]
        right = lst[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                lst[k] = left[i]
                i += 1
            else:
                lst[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            lst[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            lst[k] = right[j]
            j += 1
            k += 1
    return lst

print(merge_sort([5, 15, 37, 25, 79]))
<file_sep>/python/algorithms/