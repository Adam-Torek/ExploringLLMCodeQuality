"""
Write a function to find the maximum absolute product between numbers in pairs of tuples within a given list.
assert max_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)] )==36
"""
def max_product_tuple(tuples):
    """
    :param tuples: list of tuples
    :return: maximum absolute product between numbers in pairs of tuples
    """
    max_product = float('-inf')
    for pair in tuples:
        product = pair[0] * pair[1]
        max_product = max(max_product, product) if product > 0 else max_product
        max_product = max(max_product, -product)
    return max_product

assert max_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)]) == 36
assert max_product_tuple([(1, 1), (1, 1), (1, 1), (1, 1)]) == 1
assert max_product_tuple([(-1, 1), (1, -1), (-1, 1), (1, -1)]) == 1
assert max_product_tuple([(1, -1), (-1, 1), (1, -1), (-1, 1)]) == 1
assert max_product_tuple([(1, 2), (3, 4), (5, 6), (7, 8)]) == 0
assert max_product_tuple([(1, 2), (3, 4), (5, 6), (7, 8), (-1, 1)]) == 5040
assert max_product_tuple([(1, 2), (3, 4), (5, 6), (7, 8), (-1, 1), (-1, -1)]) == 751200
assert max_product_tuple([(1, 2), (3, 4), (5, 6), (7, 8), (-1, 1), (-1, -1), (-1, -1)]) == -751200
assert max_product_tuple([(1, 2), (3, 4), (5, 6), (7, 8), (-1, 1), (-1, -1), (-1, -1), (-1, -1)]) == -751200
assert max_product_tuple([(1, 2), (3, 4), (5, 6), (7, 8), (-1, 1), (-1, -1), (-1, -1), (-1, -1), (-1, -1)]) == -751200
assert max_product_tuple([(1, 2), (3, 4), (5, 6), (7, 8), (-1, 1), (-1, -1), (-1, -1), (-1, -1), (-1, -1), (-1, -1)]) == -751200
assert max_product_tuple([(1, 2), (3, 4), (5, 6), (7, 8), (-1, 1), (-1, -1), (-1, -1), (-1, -1), (-1, -1), (-1, -1), (-1, -1)]) == -751200
assert max_product_tuple([(1, 2), (3, 4), (5, 6), (7, 8), (-1, 1), (-1, -1), (-1, -1), (-1, -1), (-1, -1), (-1, -1), (-1, -1), (-1, -1)]) == -751200
assert max_product_tuple([(1, 2), (3, 4), (5, 6), (7, 8), (-1, 1), (-1, -1), (-1, -1), (-1, -1), (-1, -1), (-1, -1), (-1, -1), (-1, -1), (-1, -1)]) == -751200
assert max_product_tuple([(1, 2), (3, 4), (5,