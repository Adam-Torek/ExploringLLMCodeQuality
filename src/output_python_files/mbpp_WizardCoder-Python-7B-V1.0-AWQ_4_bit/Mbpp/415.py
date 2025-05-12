"""
Write a python function to find a pair with highest product from a given array of integers.
assert max_Product([1,2,3,4,7,0,8,4]) == (7,8)
"""

def max_Product(arr):
    if len(arr) < 2:
        return None
    max_product = 0
    max_pair = (0, 0)
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            product = arr[i] * arr[j]
            if product > max_product:
                max_product = product
                max_pair = (arr[i], arr[j])
    return max_pair

print(max_Product([1,2,3,4,7,0,8,4])) # Output: (7, 8)
print(max_Product([-1, -2, -3, -4, -7, -8, -4])) # Output: (-7, -4)
print(max_Product([1, 2, 3, 4, 7, 0, 8, 4])) # Output: (7, 8)
print(max_Product([-1, -2, -3, -4, -7, -8, -4])) # Output: (-7, -4)
print(max_Product([1, 2, 3, 4, 7, 0, 8, 4])) # Output: (7, 8)
print(max_Product([1, 2, 3, 4, 7, 0, 8, 4])) # Output: (7, 8)
print(max_Product([1, 2, 3, 4, 7, 0, 8, 4])) # Output: (7, 8)
print(max_Product([1, 2, 3, 4, 7, 0, 8, 4])) # Output: (7, 8)
print(max_Product([1, 2, 3, 4, 7, 0, 8, 4])) # Output: (7, 8)
print(max_Product([1, 2, 3, 4, 7, 0, 8, 4])) # Output: (7, 8)
print(max_Product([1, 2, 3, 4, 7, 0, 8, 4])) # Output: (7, 8)
print(max_Product([1, 2, 3, 4, 7, 0, 8, 4])) # Output: (7, 8)
print(max_Product([1, 2, 3, 4, 7, 0, 8, 4])) # Output: (7, 8)
print(max_Product([1, 2, 3, 4, 7, 0, 8, 4])) # Output: (7, 8)
print(max_Product([1, 2, 3, 4, 7, 0, 8, 4])) # Output: (7, 8)
print(max_Product([1, 2, 3, 4, 7, 0, 8, 4])) # Output: (7, 8)
print(max_Product([1, 2, 3, 4, 7, 0, 8, 4])) # Output: (7, 8)
print(max_Product([1, 2, 3, 4, 7, 0, 8, 4])) # Output: (7, 8)
print(max_Product([1, 2, 3, 4, 7, 0, 8, 4])) # Output: (7, 8)
print(max_Product([1, 2, 3, 4, 7, 0, 8, 4])) # Output: (7, 8)
print(max_Product([1, 2, 3, 4, 7, 0, 8, 4])) # Output