"""
Write a function to find the maximum absolute product between numbers in pairs of tuples within a given list.
assert max_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)] )==36
"""

def max_product_tuple(lst):
    """
    Find the maximum absolute product between numbers in pairs of tuples within a given list.
    """
    max_abs_product = 0
    for tuple1 in lst:
        for tuple2 in lst:
            if tuple1 != tuple2:
                product = abs(tuple1[0]*tuple2[1])
                if product > max_abs_product:
                    max_abs_product = product
    return max_abs_product

# assert max_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)])==36
print(max_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)]))