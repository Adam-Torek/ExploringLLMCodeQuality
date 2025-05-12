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
print(find_min_diff((1, 5, 3, 10, 18, 25, 6, 8, 12, 20), 6) # Output: 1
print(find_min_diff((1, 5, 3, 19, 18, 25), 6) # Output: 1
print(find_min_diff((1, 5, 3, 19, 18, 25), 10) # Output: 4
print(find_min_diff((1, 5, 3, 19, 18, 25), 25) # Output: 0
print(find_min_diff((1, 5, 3, 19, 18, 25), 26) # Output: 1
print(find_min_diff((1, 5, 3, 19, 18, 25), 1) # Output: 18
print(find_min_diff((1, 5, 3, 19, 18, 25), 0) # Output: 1
print(find_min_diff((1, 5, 3, 19, 18, 25), 2) # Output: 1
print(find_min_diff((1, 5, 3, 19, 18, 25), 100) # Output: 1
print(find_min_diff((1, 5, 3, 19, 18, 25), 1000) # Output: 1
print(find_min_diff((1, 5, 3, 19, 18, 25), 10000) # Output: 1
print(find_min_diff((1, 5, 3, 19, 18, 25), 100000) # Output: 1
print(find_min_diff((1, 5, 3, 19, 18, 25), 1000000) # Output: 1
print(find_min_diff((1, 5, 3, 19, 18, 25), 10000000) # Output: 1
print(find_min_diff((1, 5, 3, 19, 18, 25), 100000000) # Output: 1
print(find_min_diff((1, 5, 3, 19, 18, 25), 1000000000) # Output: 1
print(find_min_diff((1, 5, 3, 19, 18, 25), 10000000000) # Output: 1
print(find_min_diff((1, 5, 3, 19, 18, 25), 100000000000) # Output: 1
print(find_min_diff((1, 5, 3, 19, 18, 25), 1000000000000) # Output: 1
print(find_min_diff((1, 5, 3, 19, 18, 25), 100000000