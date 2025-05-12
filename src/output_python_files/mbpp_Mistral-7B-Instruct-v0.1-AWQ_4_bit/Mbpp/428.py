"""
Write a function to sort the given array by using shell sort.
assert shell_sort([12, 23, 4, 5, 3, 2, 12, 81, 56, 95]) == [2, 3, 4, 5, 12, 12, 23, 56, 81, 95]
"""
def shell_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i, n):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

# Test the function
arr = [12, 23, 4, 5, 3, 2, 12, 81, 56, 95]
print(shell_sort(arr))