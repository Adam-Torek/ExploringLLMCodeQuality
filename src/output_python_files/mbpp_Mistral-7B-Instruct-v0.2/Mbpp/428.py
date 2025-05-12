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

    The gap sequence used in this implementation is 5, 3, 1.
    """
    n = len(arr)
    gap = 5
    while gap > 0:
        for i in range(gap, n):
            j = i
            while j >= 0 and arr[j] < arr[j - gap]:
                arr[j], arr[j - gap] = arr[j - gap], arr[j]
                j -= gap
        gap = gap // 2

    return arr

if __name__ == "__main__":
    arr = [12, 23, 4, 5, 3, 2, 12, 81, 56, 95]
    assert shell_sort(arr) == [2, 3, 4, 5, 12, 12, 23, 56, 81, 95]
    print("Test passed!")