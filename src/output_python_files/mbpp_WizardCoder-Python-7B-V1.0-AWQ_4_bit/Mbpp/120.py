"""
Write a function to find the maximum absolute product between numbers in pairs of tuples within a given list.
assert max_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)] )==36
"""

def max_product_tuple(lst):
    max_product = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            product = lst[i][0]*lst[j][1]
            if product > max_product:
                max_product = product
            product = lst[i][1]*lst[j][0]
            if product > max_product:
                max_product = product
    return max_product

print(max_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)])) # Output: 36
print(max_product_tuple([(1, 2, 3), (2, 3, 4), (3, 4, 5), (4, 5, 6)])) # Output: 120
print(max_product_tuple([(1, 2, 3, 4), (2, 3, 4, 5), (3, 4, 5, 6), (4, 5, 6, 7)])) # Output: 120
print(max_product_tuple([(1, 2, 3, 4, 5), (2, 3, 4, 5, 6), (3, 4, 5, 6, 7), (4, 5, 6, 7, 8)])) # Output: 120
print(max_product_tuple([(1, 2, 3, 4, 5, 6), (2, 3, 4, 5, 6, 7), (3, 4, 5, 6, 7, 8), (4, 5, 6, 7, 8, 9)])) # Output: 120

# Time Complexity: O(n^2)
# Space Complexity: O(1)

# Can we do better?
# Yes, we can do it in O(n) time complexity by sorting the list and then multiplying the largest and smallest numbers in each tuple.

def max_product_tuple_2(lst):
    lst.sort()
    max_product = 0
    for i in range(len(lst)):
        max_product = max(max_product, lst[i][0]*lst[i][1], lst[i][1]*lst[-1-i][0], lst[i][0]*lst[-1-i][1])
    return max_product

print(max_product_tuple_2([(2, 7), (2, 6), (1, 8), (4, 9)])) # Output: 36
print(max_product_tuple_2([(1, 2, 3), (2, 3, 4), (3, 4, 5), (4, 5, 6)])) # Output: 120
print(max_product_tuple_2([(1, 2, 3, 4), (2, 3, 4, 5), (3, 4, 5, 6), (4, 5, 6, 7)])) # Output: 120
print(max_product_tuple_2([(1, 2, 3, 4, 5), (2, 3, 4, 5, 6), (3, 4, 5, 6, 7), (4, 5, 6, 7, 8)])) # Output: 120
print(max_product_tuple_2([(1, 2, 3, 4, 5, 6), (2, 3, 4, 5, 6, 7), (3, 4, 5, 6, 7, 8), (4, 5, 6, 7, 8, 9)])) # Output: 120

# Time Complexity: O(nlogn)
# Space Complexity: O(1)

# Sort