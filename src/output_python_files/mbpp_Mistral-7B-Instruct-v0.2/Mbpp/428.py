"""
Write a function to sort the given array by using shell sort.
assert shell_sort([12, 23, 4, 5, 3, 2, 12, 81, 56, 95]) == [2, 3, 4, 5, 12, 12, 23, 56, 81, 95]
"""
def shell_sort(arr):
    """
    Shell sort is a variation of insertion sort. It has O(n^2) worst case time complexity,
    but in the average case, it performs better than insertion sort.
    The basic idea of shell sort is to divide the input array into several sub-arrays,
    sort each sub-array individually, and then merge the sorted sub-arrays back together.
    """
    n = len(arr)
    gap = int(0.5 + (3 * (n ** 0.3333333333333333)))

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap = int(gap / 3)

    return arr

# Test the function
assert shell_sort([12, 23, 4, 5, 3, 2, 12, 81, 56, 95]) == [2, 3, 4, 5, 12, 12, 23, 56, 81, 95]
print("Test passed!")