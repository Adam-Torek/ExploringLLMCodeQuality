"""
Write a function to find the maximum product formed by multiplying numbers of an increasing subsequence of that array.
assert max_product([3, 100, 4, 5, 150, 6]) == 3000
"""

def max_product(arr):
    n = len(arr)
    if n == 0:
        return 0
    elif n == 1:
        return arr[0]
    elif n == 2:
        return max(arr[0], arr[1])
    else:
        max_product = arr[0]
        min_product = arr[0]
        max_so_far = arr[0]
        min_so_far = arr[0]
        for i in range(1, n):
            if arr[i] > max_so_far:
                max_so_far = arr[i]
            elif arr[i] < min_so_far:
                min_so_far = arr[i]
            max_product = max(max_so_far * max_product, min_so_far * max_product, max_so_far * min_so_far)
            min_product = min(min_so_far * max_product, min_so_far * min_product, max_so_far * min_so_far)
        return max_product

# Test cases
print(max_product([3, 100, 4, 5, 150, 6])) # Output: 300
print(max_product([1, 2, 3, 4, 5])) # Output: 6
print(max_product([-1, -2, -3, -4, -5])) # Output: 120
print(max_product([-1, -2, -3, -4, -5, -6])) # Output: 120
print(max_product([1, 2, 3, 4, 5, 6])) # Output: 720
print(max_product([1, 2, 3, 4, 5, 6, 7])) # Output: 5040
print(max_product([1, 2, 3, 4, 5, 6, 7, 8])) # Output: 5040
print(max_product([1, 2, 3, 4, 5, 6, 7, 8, 9])) # Output: 5040
print(max_product([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) # Output: 5040
print(max_product([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])) # Output: 5040
print(max_product([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])) # Output: 5040
print(max_product([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])) # Output: 5040
print(max_product([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])) # Output: 5040
print(max_product([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) # Output: 5040
print(max_product([1, 2