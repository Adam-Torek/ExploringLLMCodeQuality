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
    for tuple in tuples:
        product = tuple[0] * tuple[1]
        max_product = max(max_product, product) if product > 0 else max_product
        max_product = max(max_product, -product)
    return max_product

assert max_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)]) == 36
assert max_product_tuple([(1, 2), (3, 4), (5, 6), (7, 8)]) == 5040
assert max_product_tuple([(1, -1), (2, -3), (3, 4), (5, 6)]) == 120
assert max_product_tuple([(1, 2), (3, 4), (5, 6), (7, 8), (-2, -3)]) == 120
assert max_product_tuple([(1, 2), (3, 4), (5, 6), (7, 8), (-2, 3)]) == 144
assert max_product_tuple([(1, 2), (3, 4), (5, 6), (7, 8), (2, -3)]) == 144
assert max_product_tuple([(1, 2), (3, 4), (5, 6), (7, 8), (2, 3)]) == 36
assert max_product_tuple([(1, 2), (3, 4), (5, 6), (7, 8), (2, 3), (-2, 3)]) == 144
assert max_product_tuple([(1, 2), (3, 4), (5, 6), (7, 8), (2, 3), (-2, 3), (-1, -1)]) == 144
assert max_product_tuple([(1, 2), (3, 4), (5, 6), (7, 8), (2, 3), (-2, 3), (-1, -1), (-1, 1)]) == 144
assert max_product_tuple([(1, 2), (3, 4), (5, 6), (7, 8), (2, 3), (-2, 3), (-1, -1), (-1, 1), (1, 1)]) == 1
assert max_product_tuple([(1, 2), (3, 4), (5, 6), (7, 8), (2, 3), (-2, 3), (-1, -1), (-1, 1), (1, 1), (1, -1)]) == 1
assert max_product_tuple([(1, 2), (3, 4), (5, 6), (7, 8), (2, 3), (-2, 3), (-1, -1), (-1, 1), (1, 1), (1, -1), (1, 1)]) == 1
assert max_product_tuple([(1, 2), (3, 4), (5, 6), (7, 8), (2, 3), (-2, 3), (-1, -1), (-1, 1), (1, 1), (1, -1), (1, 1), (1, -1)]) == 1
assert max_product_tuple([(1, 2), (3, 4), (5, 6), (7, 8), (2, 3), (-2, 3), (-1, -1), (-1, 1), (1, 1), (1, -1), (1, 1), (1, -1), (1, 1