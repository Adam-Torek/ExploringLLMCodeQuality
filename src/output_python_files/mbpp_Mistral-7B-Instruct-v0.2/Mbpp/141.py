"""
Write a function to sort a list of elements.
assert pancake_sort([15, 79, 25, 38, 69]) == [15, 25, 38, 69, 79]
"""
def pancake_sort(arr):
    n = len(arr)
    for i in range(n-1, 0, -1):
        j = arr.index(i+1)
        arr[i], arr[j] = arr[j], arr[i]
        arr[i:] = arr[i:][::-1]
    return arr

# Test case
assert pancake_sort([15, 79, 25, 38, 69]) == [15, 25, 38, 69, 79]
print("Test passed!")