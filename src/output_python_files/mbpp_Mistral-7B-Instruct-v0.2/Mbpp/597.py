"""
Write a function to find kth element from the given two sorted arrays.
assert find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 5) == 6
"""
def merge_arrays(arr1, arr2):
    merged = []
    i = j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1

    merged += arr1[i:]
    merged += arr2[j:]
    return merged

def find_kth(arr1, arr2, k):
    merged = merge_arrays(arr1, arr2)
    return merged[k - 1]

if __name__ == "__main__":
    assert find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 5) == 6
    assert find_kth([1, 2, 3, 4, 5], [6, 7, 8, 9, 10], 7) == 8
    assert find_kth([1, 2, 3, 4, 5], [6, 7, 8, 9, 10], 11) == 9
    assert find_kth([], [1], 1) == 1
    assert find_kth([], [], 1) == None
    assert find_kth([1], [], 1) == 1
    assert find_kth([1], [], 2) == None
    assert find_kth([], [1], 1) == 1
    assert find_kth([], [1], 2) == None
    assert find_kth([1], [], 1) == 1
    assert find_kth([1], [], 2) == None
    assert find_kth([1], [1], 1) == 1
    assert find_kth([1], [1], 2) == 1
    assert find_kth([1], [1], 3) == None
    assert find_kth([1], [1], 4) == None
    assert find_kth([1], [1], 5) == None
    assert find_kth([1], [1], 6) == None
    assert find_kth([1], [1], 7) == None
    assert find_kth([1], [1], 8) == None
    assert find_kth([1], [1], 9) == None
    assert find_kth([1], [1], 10) == None
    assert find_kth([1], [1], 11) == None
    assert find_kth([1], [1], 12) == None
    assert find_kth([1], [1], 13) == None
    assert find_kth([1], [1], 14) == None
    assert find_kth([1], [1], 15) == None
    assert find_kth([1], [1], 16) == None
    assert find_kth([1], [1], 17) == None
    assert find_kth([1], [1], 18) == None
    assert find_kth([1], [1], 19) == None
    assert find_kth([1], [1], 20) == None
    assert find_kth([1], [1], 21) == None
    assert find_kth([1], [1], 22) == None
    assert find_kth([1], [1], 23) == None
    assert find_kth([1], [1], 24) == None
    assert find_kth([1], [1], 25) == None
    assert find_kth([1], [1], 26) == None
    assert find_kth([1], [1], 27) == None
    assert find_kth([1], [1], 28) == None