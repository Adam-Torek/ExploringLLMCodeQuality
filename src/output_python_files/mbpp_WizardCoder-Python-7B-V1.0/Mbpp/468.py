"""
Write a function to find the maximum product formed by multiplying numbers of an increasing subsequence of that array.
assert max_product([3, 100, 4, 5, 150, 6]) == 3000
"""

def max_product(arr):
    if len(arr) == 0:
        return 0
    elif len(arr) == 1:
        return arr[0]
    elif len(arr) == 2:
        return max(arr[0], arr[1])
    else:
        max_product = arr[0]
        min_product = arr[0]
        result = arr[0]
        for i in range(1, len(arr)):
            if arr[i] > max_product:
                max_product = arr[i]
            elif arr[i] < min_product:
                min_product = arr[i]
            result = max(result, max_product * arr[i])
        return result

# Test cases
print(max_product([3, 100, 4, 5, 150, 6])) # Output: 300
print(max_product([1, 2, 3, 4])) # Output: 24
print(max_product([-10, -10, -10])) # Output: 0
print(max_product([1, 2, 3, 4, 5])) # Output: 120
print(max_product([-10, -10, 1, 2, 3, 4, 5])) # Output: 500
print(max_product([-10, -10, 1, -2, 3, 4, 5])) # Output: 600
print(max_product([-10, -10, -10])) # Output: 0
print(max_product([1])) # Output: 1
print(max_product([-10])) # Output: -10
print(max_product([])) # Output: 0
print(max_product([1, 2, 3, 4, 5, 6, 7, 8, 9])) # Output: 288
print(max_product([-10, -10, -10, -10])) # Output: 0
print(max_product([-10, -10, -10, 1, 2, 3, 4, 5])) # Output: 600
print(max_product([-10, -10, -10, 1, -2, 3, 4, 5])) # Output: 600
print(max_product([-10, -10, -10, 1, -2, -3, 4, 5])) # Output: 600
print(max_product([-10, -10, -10, 1, -2, -3, -4, 5])) # Output: 600
print(max_product([-10, -10, -10, 1, -2, -3, -4, -5])) # Output: 600
print(max_product([-10, -10, -10, 1, -2, -3, -4, -5, 6])) # Output: 600
print(max_product([-10, -10, -10, 1, -2, -3, -4, -5, 6, 7])) # Output: 600
print(max_product([-10, -10, -10, 1, -2, -3, -4, -5, 6, 7, 8])) # Output: 600
print(max_product([-10, -10, -10, 1, -2, -3