"""
Write a function to find the minimum product from the pairs of tuples within a given list.
assert min_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)] )==8
"""
def min_product_tuple(tuples):
    """
    :param tuples: list of tuples
    :return: minimum product of tuples
    """
    min_product = float('inf')
    for tuple in tuples:
        product = tuple[0] * tuple[1]
        if product < min_product:
            min_product = product
    return min_product

if __name__ == "__main__":
    assert min_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)]) == 8
    assert min_product_tuple([(1, 2), (3, 4), (5, 6), (7, 8)]) == 12
    assert min_product_tuple([(1, 1), (1, 1), (1, 1), (1, 1)]) == 1
    assert min_product_tuple([]) == 0
    assert min_product_tuple([(0, 0)]) == 0
    assert min_product_tuple([(1, -1), (-1, 1)]) == 1
    assert min_product_tuple([(1, 1), (1, -1), (-1, 1), (-1, -1)]) == 1
    assert min_product_tuple([(1, 1), (1, -1), (-1, 1), (-1, -1), (0, 0)]) == 0
    assert min_product_tuple([(1, 1), (1, -1), (-1, 1), (-1, -1), (0, 0), (1, 1)]) == 1
    assert min_product_tuple([(1, 1), (1, -1), (-1, 1), (-1, -1), (0, 0), (1, 1), (1, 1)]) == 1
    assert min_product_tuple([(1, 1), (1, -1), (-1, 1), (-1, -1), (0, 0), (1, 1), (1, 1), (1, 1)]) == 1
    assert min_product_tuple([(1, 1), (1, -1), (-1, 1), (-1, -1), (0, 0), (1, 1), (1, 1), (1, 1), (1, 1)]) == 1
    assert min_product_tuple([(1, 1), (1, -1), (-1, 1), (-1, -1), (0, 0), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1)]) == 1
    assert min_product_tuple([(1, 1), (1, -1), (-1, 1), (-1, -1), (0, 0), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1)]) == 1
    assert min_product_tuple([(1, 1), (1, -1), (-1, 1), (-1, -1), (0, 0), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1)]) == 1
    assert min_product_tuple([(1, 1), (1, -1), (-1, 1), (-1, -1), (0, 0), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1,