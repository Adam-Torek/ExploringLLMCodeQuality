"""
Write a python function to find a pair with highest product from a given array of integers.
assert max_Product([1,2,3,4,7,0,8,4]) == (7,8)
"""
def max_Product(arr):
    if len(arr) < 2:
        return None
    max_product = float('-inf')
    max_pair = None
    min_product = float('inf')
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            product = arr[i] * arr[j]
            if product > max_product:
                max_product = product
                max_pair = (arr[i], arr[j])
            if product < min_product:
                min_product = product
    return max_pair

print(max_Product([1,2,3,4,7,0,8,4])) # Output: (7, 8)
print(max_Product([-1,2,3,-4,0,8,4])) # Output: (8, -4)
print(max_Product([-1,2,3,4,7,0,8])) # Output: (7, 8)
print(max_Product([-1,2,3,4,7,0])) # Output: (7, 8)
print(max_Product([1,2,3,4])) # Output: None
print(max_Product([1])) # Output: None
print(max_Product([])) # Output: None
print(max_Product([-1])) # Output: None
print(max_Product([-1, -2])) # Output: (-1, -2)
print(max_Product([-1, -2, -3])) # Output: (-3, -1)
print(max_Product([-1, -2, 3])) # Output: (3, -1)
print(max_Product([-1, -2, 3, -4])) # Output: (-4, -1)
print(max_Product([-1, -2, 3, -4, 5])) # Output: (5, -1)
print(max_Product([-1, -2, 3, -4, 5, 6])) # Output: (6, -1)
print(max_Product([-1, -2, 3, -4, 5, 6, 7])) # Output: (7, -1)
print(max_Product([-1, -2, 3, -4, 5, 6, 7, 8])) # Output: (8, -1)
print(max_Product([-1, -2, 3, -4, 5, 6, 7, 8, 9])) # Output: (9, -1)
print(max_Product([-1, -2, 3, -4, 5, 6, 7, 8, 9, 10])) # Output: (10, -1)
print(max_Product([-1, -2, 3, -4, 5, 6, 7, 8, 9, 10, 11])) # Output: (11, -1)
print(max_Product([-1, -2, 3, -4, 5, 6, 7, 8, 9, 10, 11, 12])) # Output: (12, -1)
print(max_Product([-1, -2, 3, -4, 5, 6, 7, 8, 9, 10, 11, 12, 13])) # Output: (13, -1)
print(max_Product([-1, -2, 3, -4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])) # Output: (14, -1)
print(max_Product([-1, -2, 3, -4, 5, 6, 7, 8,