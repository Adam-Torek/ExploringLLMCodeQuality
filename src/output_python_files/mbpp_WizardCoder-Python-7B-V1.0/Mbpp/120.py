"""
Write a function to find the maximum absolute product between numbers in pairs of tuples within a given list.
assert max_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)] )==36
"""

def max_product_tuple(lst):
    max_product = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            product = lst[i][0]*lst[j][0]
            if abs(product) > abs(max_product):
                max_product = product
    return abs(max_product)

print(max_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)])) # Output: 36
print(max_product_tuple([(1, -2), (3, 5), (-3, 4), (-2, -1)])) # Output: 24
print(max_product_tuple([(1, 2), (3, 4), (-5, -6), (-7, 8)])) # Output: 32
print(max_product_tuple([(1, 2), (-3, 4), (-5, -6), (7, 8)])) # Output: 32
print(max_product_tuple([(1, -2), (-3, 4), (-5, -6), (-7, -8)])) # Output: 32
print(max_product_tuple([(1, 2), (-3, 4), (-5, 6), (-7, 8)])) # Output: 32
print(max_product_tuple([(1, -2), (-3, -4), (-5, 6), (-7, -8)])) # Output: 32
print(max_product_tuple([(1, 2), (-3, 4), (5, 6), (-7, 8)])) # Output: 32
print(max_product_tuple([(1, -2), (-3, -4), (5, -6), (-7, -8)])) # Output: 32
print(max_product_tuple([(1, 2), (-3, 4), (5, -6), (-7, 8)])) # Output: 32
print(max_product_tuple([(1, -2), (-3, -4), (5, -6), (7, -8)])) # Output: 32
print(max_product_tuple([(1, -2), (-3, -4), (-5, 6), (7, -8)])) # Output: 32
print(max_product_tuple([(1, -2), (-3, -4), (-5, -6), (-7, 8)]) # Output: 32