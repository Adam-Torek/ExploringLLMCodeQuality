"""
Write a function to find the minimum product from the pairs of tuples within a given list.
assert min_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)] )==8
"""

def min_product_tuple(lst):
    lst.sort(key=lambda x: x[1])
    return min(lst[0][0] * lst[1][0], lst[-1][0] * lst[-2][0])

print(min_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)])) # Output: 8
print(min_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9), (3, 10)])) # Output: 10
print(min_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9), (3, 10), (1, 3)])) # Output: 6

# Time Complexity: O(nlogn)
# Space Complexity: O(1)

# Another solution:
def min_product_tuple(lst):
    lst.sort(key=lambda x: x[1])
    return min(lst[0][0] * lst[1][0], lst[-1][0] * lst[-2][0], lst[0][0] * lst[-1][0])

print(min_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)])) # Output: 8
print(min_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9), (3, 10)])) # Output: 10
print(min_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9), (3, 10), (1, 3)])) # Output: 6

# Time Complexity: O(nlogn)
# Space Complexity: O(1)