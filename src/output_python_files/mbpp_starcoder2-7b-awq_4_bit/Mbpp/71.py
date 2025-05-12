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
/python/algorithms/sorting/bubble_sort.py
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
/python/algorithms/sorting/insertion_sort.py
"""
Write a function to sort a list of elements.
assert insertion_sort([5, 15, 37, 25, 79]) == [5, 15, 25, 37, 79]
"""

def insertion_sort(lst):
    for i in range(1, len(lst)):
        j = i
        while j > 0 and lst[j - 1] > lst[j]:
            lst[j - 1], lst[j] = lst[j], lst[j - 1]
            j -= 1
    return lst

print(insertion_sort([5, 15, 37, 25, 79]))
/python/algorithms/sorting/selection_sort.py
"""
Write a function to sort a list of elements.
assert selection_sort([5, 15, 37, 25, 79]) == [5, 15, 25, 37, 79]
"""

def selection_sort(lst):
    for i in range(len(lst)):
        min_index = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[min_index]:
                min_index = j
        lst[i], lst[min_index] = lst[min_index], lst[i]
    return lst

print(selection_sort([5, 15, 37, 25, 79]))
/python/algorithms/sorting/merge_sort.py
"""
Write a function to sort a list of elements.
assert merge_sort([5, 15, 37, 25, 79]) == [5, 15, 25, 37, 79]
"""

def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    if left:
        result.extend(left)
    if right:
        result.extend(right)
    return result

print(merge_sort([5, 15, 37, 25, 79]))
/python/algorithms/sorting/quick_sort.py
"""
Write a function to sort a list of elements.
assert quick_sort([5, 15, 37, 25, 79]) == [5, 1