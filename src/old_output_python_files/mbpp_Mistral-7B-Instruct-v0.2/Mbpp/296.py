"""
Write a python function to count inversions in an array.
assert get_Inv_Count([1,20,6,4,5]) == 5
"""
def get_Inv_Count(arr):
    count = 0
    n = len(arr)
    i = 0
    while i < n:
        j = i + 1
        while j < n and arr[i] > arr[j]:
            count += 1
            j += 1
        i += 1
    return count

# Test case
assert get_Inv_Count([1,20,6,4,5]) == 5
print("Test passed")