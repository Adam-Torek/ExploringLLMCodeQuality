"""
Write a function to find the maximum absolute product between numbers in pairs of tuples within a given list.
assert max_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)] )==36
"""

def max_product_tuple(tuples):
    """
    tuples: a list of tuples
    returns: the maximum absolute product of two numbers in tuples
    """
    max_product = 0
    for i in range(len(tuples)):
        for j in range(i+1, len(tuples)):
            product = abs(tuples[i][0] * tuples[j][1])
            if product > max_product:
                max_product = product
    return max_product


def test_max_product_tuple():
    assert max_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)]) == 36
    assert max_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9), (1, 1)]) == 36
    assert max_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9), (1, 1), (1, 1)]) == 36
    assert max_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9), (1, 1), (1, 1), (1, 1)]) == 36
    assert max_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9), (1, 1), (1, 1), (1, 1), (1, 1)]) == 36
    assert max_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1)]) == 36
    assert max_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1)]) == 36
    assert max_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1)]) == 36
    assert max_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1)]) == 36
    assert max_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1)]) == 36
    assert max_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1)]) == 36
    assert max_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1