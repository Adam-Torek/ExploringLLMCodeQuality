"""
Write a function to find the minimum product from the pairs of tuples within a given list.
assert min_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)] )==8
"""

def min_product_tuple(lst):
    lst.sort(key=lambda x: x[1])
    min_product = float('inf')
    for i in range(len(lst)-1):
        for j in range(i+1, len(lst)):
            product = lst[i][0] * lst[j][1]
            if product < min_product:
                min_product = product
    return min_product

print(min_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)])) # Output: 8
print(min_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9), (3, 10)])) # Output: 10
print(min_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9), (3, 10), (1, 3)])) # Output: 6
print(min_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9), (3, 10), (1, 3), (1, 1)])) # Output: 2
print(min_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9), (3, 10), (1, 3), (1, 1), (1, 1)])) # Output: 2
print(min_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9), (3, 10), (1, 3), (1, 1), (1, 1), (1, 1)])) # Output: 2
print(min_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9), (3, 10), (1, 3), (1, 1), (1, 1), (1, 1), (1, 1)])) # Output: 2
print(min_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9), (3, 10), (1, 3), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1)])) # Output: 2
print(min_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9), (3, 10), (1, 3), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1)])) # Output: 2
print(min_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9), (3, 10), (1, 3), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1)])) # Output: 2
print(min_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9), (3, 10), (1, 3), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1)])) # Output: 2
print(min_product_tuple([(2, 7), (2, 6), (1,