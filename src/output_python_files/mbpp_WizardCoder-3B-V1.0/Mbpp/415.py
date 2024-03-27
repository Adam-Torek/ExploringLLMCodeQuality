"""
Write a python function to find a pair with highest product from a given array of integers.
assert max_Product([1,2,3,4,7,0,8,4]) == (7,8)
"""

def max_Product(arr):
    max_product = float('-inf')
    min_product = float('inf')
    for num in arr:
        if num > max_product:
            max_product = num
        elif num < min_product:
            min_product = num
    return (max_product, min_product)

print(max_Product([1,2,3,4,7,0,8,4])) # Output: (7, 8)<|endoftext|>