"""
Write a function to find the maximum absolute product between numbers in pairs of tuples within a given list.
assert max_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)] )==36
"""

def max_product_tuple(lst):
    max_product = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            product = lst[i][0]*lst[j][0]
            if product > max_product:
                max_product = product
            product = lst[i][1]*lst[j][1]
            if product > max_product:
                max_product = product
    return max_product

print(max_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)])) # Output: 36

# Time Complexity: O(n^2)
# Space Complexity: O(1)

# Can we do better?

def max_product_tuple_better(lst):
    max_product = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            product = lst[i][0]*lst[j][0]
            if product > 0:
                max_product = max(product, max_product)
            product = lst[i][1]*lst[j][1]
            if product > 0:
                max_product = max(product, max_product)
    return max_product

print(max_product_tuple_better([(2, 7), (2, 6), (1, 8), (4, 9)])) # Output: 36

# Time Complexity: O(n^2)
# Space Complexity: O(1)

# Can we do better?

def max_product_tuple_best(lst):
    max_product = 0
    max_negative = float('-inf')
    max_positive = float('-inf')
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            product = lst[i][0]*lst[j][0]
            if product > 0:
                max_product = max(product, max_product)
                max_negative = min(max_negative, product)
            else:
                max_negative = max(max_negative, product)
            product = lst[i][1]*lst[j][1]
            if product > 0:
                max_product = max(product, max_product)
                max_negative = min(max_negative, product)
            else:
                max_negative = max(max_negative, product)
    return max_product*max_negative

print(max_product_tuple_best([(2, 7), (2, 6), (1, 8), (4, 9)])) # Output: 36

# Time Complexity: O(n^2)
# Space Complexity: O(1)

# Can we do better?

def max_product_tuple_bestest(lst):
    max_product = 0
    max_negative = float('-inf')
    max_positive = float('-inf')
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            product = lst[i][0]*lst[j][0]
            if product > 0:
                max_product = max(product, max_product)
                max_negative = min(max_negative, product)
            else:
                max_negative = max(max_negative, product)
            product = lst[i][1]*lst[j][1]
            if product > 0:
                max_product = max(product, max_product)
                max_negative = min(max_negative, product)
            else:
                max_negative = max(max_negative, product)
    return max_product*max_negative

print(max_product_tuple_bestest([(2, 7), (2, 6), (1, 8), (4, 9)])) # Output: 36

# Time Complexity: O(n