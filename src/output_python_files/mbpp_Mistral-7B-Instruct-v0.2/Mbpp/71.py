"""
Write a function to sort a list of elements.
assert comb_sort([5, 15, 37, 25, 79]) == [5, 15, 25, 37, 79]
"""
def comb_sort(arr):
    n = len(arr)
    gap = int(n * 1.3)
    while gap > 1:
        for i in range(n - gap):
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
        gap = int(gap / 1.3)
    return arr

assert comb_sort([5, 15, 37, 25, 79]) == [5, 15, 25, 37, 79]</s>