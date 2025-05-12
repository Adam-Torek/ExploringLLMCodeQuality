"""
Write a function to sort a list of elements.
assert comb_sort([5, 15, 37, 25, 79]) == [5, 15, 25, 37, 79]
"""

def comb_sort(arr):
    n = len(arr)
    gap = n
    shrink = 1.3
    sorted = False
    while not sorted:
        gap = int(gap / shrink)
        if gap <= 1:
            sorted = True
        else:
            gap = max(1, gap)
        i = 0
        sorted = True
        while i < n - gap:
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                sorted = False
            i += 1
    for i in range(1, n):
        if arr[i - 1] > arr[i]:
            sorted = False
            arr[i - 1], arr[i] = arr[i], arr[i - 1]
    if not sorted:
        comb_sort(arr)
    return arr

print(comb_sort([5, 15, 37, 25, 79])) # [5, 15, 25, 37, 79]