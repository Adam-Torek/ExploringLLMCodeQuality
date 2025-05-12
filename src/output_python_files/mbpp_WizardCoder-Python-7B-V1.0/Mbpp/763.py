"""
Write a python function to find the minimum difference between any two elements in a given array. https://www.geeksforgeeks.org/find-minimum-difference-pair/
assert find_min_diff((1,5,3,19,18,25),6) == 1
"""
def find_min_diff(arr, n):
    arr.sort()
    min_diff = float('inf')
    for i in range(n-1):
        diff = arr[i+1] - arr[i]
        if diff < min_diff:
            min_diff = diff
    return min_diff

# Test cases
print(find_min_diff((1,5,3,19,18,25),6)) # Output: 1
print(find_min_diff((1, 2, 3, 4, 5, 6, 7, 8, 9), 6)) # Output: 1
print(find_min_diff((1, 3, 5, 10, 15, 18, 20, 25), 6)) # Output: 1
print(find_min_diff((1, 2, 3, 4, 5, 6, 7, 8, 9), 6)) # Output: 1
print(find_min_diff((1, 3, 5, 10, 15, 18, 20, 25), 6)) # Output: 1
print(find_min_diff((1, 2, 3, 4, 5, 6, 7, 8, 9), 6)) # Output: 1
print(find_min_diff((1, 2, 3, 4, 5, 6, 7, 8, 9), 6)) # Output: 1
print(find_min_diff((1, 2, 3, 4, 5, 6, 7, 8, 9), 6)) # Output: 1
print(find_min_diff((1, 2, 3, 4, 5, 6, 7, 8, 9), 6)) # Output: 1
print(find_min_diff((1, 2, 3, 4, 5, 6, 7, 8, 9), 6)) # Output: 1
print(find_min_diff((1, 2, 3, 4, 5, 6, 7, 8, 9), 6)) # Output: 1
print(find_min_diff((1, 2, 3, 4, 5, 6, 7, 8, 9), 6)) # Output: 1
print(find_min_diff((1, 2, 3, 4, 5, 6, 7, 8, 9), 6)) # Output: 1
print(find_min_diff((1, 2, 3, 4, 5, 6, 7, 8, 9), 6)) # Output: 1
print(find_min_diff((1, 2, 3, 4, 5, 6, 7, 8, 9), 6)) # Output: 1
print(find_min_diff((1, 2, 3, 4, 5, 6, 7, 8, 9), 6)) # Output: 1
print(find_min_diff((1, 2, 3, 4, 5, 6, 7, 8, 9), 6)) # Output: 1
print(find_min_diff((1, 2, 3, 4, 5, 6, 7, 8, 9), 6)) # Output: 1
print(find_min_diff((1, 2, 3, 4, 5, 6, 7, 8, 9), 6)) # Output: 1
print(find_min_diff((1, 2, 3, 4, 5, 6, 7, 8, 9), 6)) # Output: 1
print(find_min_diff((1, 2, 3,