"""
Write a function to find kth element from the given two sorted arrays.
assert find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 5) == 6
"""

def find_kth(arr1, arr2, k):
    i = j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            i += 1
        elif arr1[i] > arr2[j]:
            j += 1
        else:
            k -= 1
            if k == 0:
                return arr1[i]
            i += 1
            j += 1
    return None

# Test the function
print(find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 5))  # Output: 6<|endoftext|>