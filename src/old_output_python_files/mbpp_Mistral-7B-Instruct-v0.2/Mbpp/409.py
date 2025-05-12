"""
Write a function to find the minimum product from the pairs of tuples within a given list.
assert min_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)] )==8
"""
def min_product_tuple(tuples):
    """
    :param tuples: list of tuples
    :return: minimum product from the pairs of tuples
    """
    return min(a*b for a, b in tuples)

if __name__ == "__main__":
    assert min_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)]) == 8
    assert min_product_tuple([(1, 2), (3, 4), (5, 6), (7, 8)]) == 12
    assert min_product_tuple([(1, 1), (1, 1), (1, 1), (1, 1)]) == 1
    assert min_product_tuple([]) is None
    assert min_product_tuple([(1, 2)]) == 2
    assert min_product_tuple([(1, 1)]) == 1
    assert min_product_tuple([(1, 1), (1, 1)]) == 1
    assert min_product_tuple([(1, 1), (1, 1), (1, 1)]) == 1
    assert min_product_tuple([(1, 1), (1, 1), (1, 1), (1, 1), (1, 1)]) == 1
    assert min_product_tuple([(1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1)]) == 1
    assert min_product_tuple([(1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1)]) == 1
    assert min_product_tuple([(1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1)]) == 1
    assert min_product_tuple([(1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1)]) == 1
    assert min_product_tuple([(1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1)]) == 1
    assert min_product_tuple([(1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1)]) == 1
    assert min_product_tuple([(1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1)]) == 1
    assert min_product_tuple([(1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1)]) == 1
    assert min_product_tuple([(1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (