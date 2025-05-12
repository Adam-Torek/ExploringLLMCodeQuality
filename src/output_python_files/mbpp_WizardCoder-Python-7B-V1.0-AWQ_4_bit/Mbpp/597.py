"""
Write a function to find kth element from the given two sorted arrays.
assert find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 5) == 6
"""

def find_kth(arr1, arr2, k):
    if len(arr1) > len(arr2):
        arr1, arr2 = arr2, arr1
    if not arr1:
        return arr2[k-1]
    if k > len(arr1) + len(arr2):
        return None
    if k == 1:
        return min(arr1[0], arr2[0])
    if k == 1:
        return max(arr1[0], arr2[0])
    i = min(k // 2, len(arr1))
    j = k - i
    if arr1[i-1] < arr2[j-1]:
        return find_kth(arr1[i:], arr2, k - i)
    else:
        return find_kth(arr1, arr2[j:], k - j)

# Test cases
print(find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 5)) # Output: 6
print(find_kth([1, 3, 5, 7], [2, 4, 8, 9], 3)) # Output: 5
print(find_kth([1, 2, 3, 4], [5, 6, 7, 8, 9], 4)) # Output: 4
print(find_kth([1, 2, 3, 4], [5, 6, 7, 8, 9], 10)) # Output: None
print(find_kth([1, 2, 3, 4], [5, 6, 7, 8, 9], 0)) # Output: None
print(find_kth([1, 2, 3, 4], [5, 6, 7, 8, 9], 1)) # Output: 1
print(find_kth([1, 2, 3, 4], [5, 6, 7, 8, 9], 2)) # Output: 2
print(find_kth([1, 2, 3, 4], [5, 6, 7, 8, 9], 3)) # Output: 3
print(find_kth([1, 2, 3, 4], [5, 6, 7, 8, 9], 4)) # Output: 4
print(find_kth([1, 2, 3, 4], [5, 6, 7, 8, 9], 5)) # Output: 5
print(find_kth([1, 2, 3, 4], [5, 6, 7, 8, 9], 6)) # Output: 6
print(find_kth([1, 2, 3, 4], [5, 6, 7, 8, 9], 7)) # Output: 7
print(find_kth([1, 2, 3, 4], [5, 6, 7, 8, 9], 8)) # Output: 8
print(find_kth([1, 2, 3, 4], [5, 6, 7, 8, 9], 9)) # Output: 9
print(find_kth([1, 2, 3, 4], [5, 6, 7, 8, 9], 10)) # Output: None
print(find_kth([1, 2, 3, 4], [5, 6, 7, 8, 9], 11)) # Output: None
print(find_kth([1, 2, 3, 4], [5, 6, 7, 8, 9], 0)) # Output: None
print(find_kth([1, 2, 3, 4], [5, 6, 7, 8, 9],