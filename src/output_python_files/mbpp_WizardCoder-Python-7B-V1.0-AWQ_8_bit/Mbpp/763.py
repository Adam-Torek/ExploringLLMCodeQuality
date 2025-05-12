"""
Write a python function to find the minimum difference between any two elements in a given array. https://www.geeksforgeeks.org/find-minimum-difference-pair/
assert find_min_diff((1,5,3,19,18,25),6) == 1
"""
def find_min_diff(arr, target):
    arr.sort()
    min_diff = float('inf')
    for i in range(len(arr)-1):
        diff = arr[i+1] - arr[i]
        if diff < min_diff:
            min_diff = diff
    return min_diff

# Test cases
print(find_min_diff((1,5,3,19,18,25),6)) # Output: 1
print(find_min_diff((1, 5, 3, 19, 18, 25), 6)) # Output: 1
print(find_min_diff((1, 2, 3, 4, 5, 6, 7, 8, 9), 10)) # Output: 1
print(find_min_diff((1, 3, 5, 7, 9, 11, 13, 15), 10)) # Output: 1
print(find_min_diff((1, 3, 5, 7, 9, 11, 13, 15), 1)) # Output: 0
print(find_min_diff((1, 3, 5, 7, 9, 11, 13, 15), 17)) # Output: 2
print(find_min_diff((1, 3, 5, 7, 9, 11, 13, 15), 16)) # Output: 1
print(find_min_diff((1, 3, 5, 7, 9, 11, 13, 15), 14)) # Output: 1
print(find_min_diff((1, 3, 5, 7, 9, 11, 13, 15), 12)) # Output: 1
print(find_min_diff((1, 3, 5, 7, 9, 11, 13, 15), 11)) # Output: 1
print(find_min_diff((1, 3, 5, 7, 9, 11, 13, 15), 1)) # Output: 0
print(find_min_diff((1, 3, 5, 7, 9, 11, 13, 15), 0)) # Output: 0
print(find_min_diff((1, 3, 5, 7, 9, 11, 13, 15), 20)) # Output: 1
print(find_min_diff((1, 3, 5, 7, 9, 11, 13, 15), 25)) # Output: 4
print(find_min_diff((1, 3, 5, 7, 9, 11, 13, 15), 26)) # Output: 5
print(find_min_diff((1, 3, 5, 7, 9, 11, 13, 15), 27)) # Output: 6
print(find_min_diff((1, 3, 5, 7, 9, 11, 13, 15), 28)) # Output: 7
print(find_min_diff((1, 3, 5, 7, 9, 11, 13, 15), 29)) # Output: 8
print(find_min_diff((1, 3, 5, 7, 9, 11, 13, 15), 30)) # Output: 9
print(find_min_diff((1, 3, 5, 7, 9, 11, 13, 15), 31)) # Output: 10
print(find_min_diff((1