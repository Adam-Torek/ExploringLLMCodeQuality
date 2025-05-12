"""
Write a python function to count inversions in an array.
assert get_Inv_Count([1,20,6,4,5]) == 5
"""

def merge_sort(arr):
    if len(arr) <= 1:
        return arr, 0

    mid = len(arr) // 2
    left, left_inv_count = merge_sort(arr[:mid])
    right, right_inv_count = merge_sort(arr[mid:])

    merged, inv_count = merge(left, right, left_inv_count, right_inv_count)
    return merged, inv_count

def merge(left, right, left_inv_count, right_inv_count):
    merged = []
    i = j = inv_count = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            inv_count += len(left) - i
            j += 1

    merged += left[i:]
    merged += right[j:]
    return merged, inv_count + left_inv_count + right_inv_count

def get_Inv_Count(arr):
    sorted_arr, inv_count = merge_sort(arr)
    return inv_count

# Test cases
assert get_Inv_Count([1,20,6,4,5]) == 5
assert get_Inv_Count([1,2,3,4,5]) == 0
assert get_Inv_Count([5,4,3,2,1]) == 6
assert get_Inv_Count([1,3,2,4,5]) == 10
assert get_Inv_Count([1,2,4,6,5,3]) == 11
assert get_Inv_Count([5,4,3,2,1]) == 6
assert get_Inv_Count([1,2,3,4,5]) == 0
assert get_Inv_Count([1,3,2,2,1]) == 2
assert get_Inv_Count([1,2,4,3,5]) == 3
assert get_Inv_Count([3,2,1,5,4]) == 6
assert get_Inv_Count([4,3,2,1]) == 6
assert get_Inv_Count([1,2,3,3,2,1]) == 4
assert get_Inv_Count([1,2,3,3,4,5]) == 3
assert get_Inv_Count([1,2,3,4,5,5,4,3,2,1]) == 10
assert get_Inv_Count([1,2,3,4,5,6,7,8,9,10]) == 24
assert get_Inv_Count([10,9,8,7,6,5,4,3,2,1]) == 22
assert get_Inv_Count([10,9,8,7,6,5,4,3,2,1,1,2,3,4,5,6,7,8,9,10]) == 55
assert get_Inv_Count([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]) == 100