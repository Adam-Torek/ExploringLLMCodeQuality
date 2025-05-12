"""
Write a function to find the minimum product from the pairs of tuples within a given list.
assert min_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)] )==8
"""


def min_product_tuple(tuples):
    """
    :param tuples: list of tuples
    :return: minimum product of tuples
    """
    return min(map(lambda x: x[0] * x[1], tuples))


if __name__ == '__main__':
    print(min_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)]))
    print(min_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9), (1, 1)]))
    print(min_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9), (1, 1), (1, 1)]))
    print(min_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9), (1, 1), (1, 1), (1, 1)]))
    print(min_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9), (1, 1), (1, 1), (1, 1), (1, 1)]))
    print(min_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1)]))
    print(min_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1)]))
    print(min_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1)]))
    print(min_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1)]))
    print(min_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1)]))
    print(min_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1)]))
    print(min_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1)]))
    print(min_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1,