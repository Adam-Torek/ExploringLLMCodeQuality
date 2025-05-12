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
    assert find_kth([], [1], 1) == 1
    assert find_kth([1], [], 1) == 1
    assert find_kth([1, 2, 3], [4, 5, 6], 5) == 5
    assert find_kth([1, 2, 3], [4, 5, 6], 6) == 6
    assert find_kth([1, 2, 3], [4, 5, 6], 7) == 6
    assert find_kth([1, 2, 3], [4, 5, 6], 8) == 6
    assert find_kth([1, 2, 3], [4, 5, 6], 10) == 6
    assert find_kth([1, 2, 3], [4, 5, 6], 11) == 6
    assert find_kth([1, 2, 3], [4, 5, 6], 12) == 6
    assert find_kth([1, 2, 3], [4, 5, 6], 13) == 6
    assert find_kth([1, 2, 3], [4, 5, 6], 14) == 6
    assert find_kth([1, 2, 3], [4, 5, 6], 15) == 6
    assert find_kth([1, 2, 3], [4, 5, 6], 16) == 6
    assert find_kth([1, 2, 3], [4, 5, 6], 17) == 6
    assert find_kth([1, 2, 3], [4, 5, 6], 18) == 6
    assert find_kth([1, 2, 3], [4, 5, 6], 19) == 6
    assert find_kth([1, 2, 3], [4, 5, 6], 20) == 6
    assert find_kth([1, 2, 3], [4, 5, 6], 21) == 6
    assert find_kth([1, 2, 3], [4, 5, 6], 22) == 6
    assert find_kth([1, 2, 3], [4, 5, 6], 23) == 6
    assert find_kth([1, 2, 3], [4, 5, 6], 24) == 6
    assert find_kth([1, 2, 3], [4, 5, 6], 25) == 6
    assert find_kth([1, 2, 3], [4, 5, 6], 26) == 6
    assert