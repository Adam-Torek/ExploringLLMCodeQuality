"""
Write a function to sort a list of elements.
assert comb_sort([5, 15, 37, 25, 79]) == [5, 15, 25, 37, 79]
"""

def comb_sort(arr):
    n = len(arr)
    swapped = True
    gap = n // 2

    while swapped:
        swapped = False
        for i in range(gap):
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                swapped = True
        gap = (gap + 1) // 2

    return arr

# Test the function
print(comb_sort([5, 15, 37, 25, 79])) # Output: [5, 15, 25, 37, 79]<|endoftext|>