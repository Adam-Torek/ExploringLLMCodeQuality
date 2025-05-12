"""
Write a function to find the maximum absolute product between numbers in pairs of tuples within a given list.
assert max_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)] )==36
"""


def max_product_tuple(tuples):
    """
    :param tuples: list of tuples
    :return: maximum absolute product between numbers in pairs of tuples
    """
    max_product = 0
    for i in range(len(tuples)):
        for j in range(i + 1, len(tuples)):
            product = abs(tuples[i][0] * tuples[i][1]) * abs(tuples[j][0] * tuples[j][1])
            if product > max_product:
                max_product = product
    return max_product


if __name__ == '__main__':
    print(max_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)]))
    print(max_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9), (1, 1)]))
    print(max_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9), (1, 1), (1, 1)]))
    print(max_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9), (1, 1), (1, 1), (1, 1)]))
    print(max_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9), (1, 1), (1, 1), (1, 1), (1, 1)]))
    print(max_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1)]))
    print(max_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1)]))
    print(max_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1)]))
    print(max_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1)]))
    print(max_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1)]))
    print(max_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1)]))
    print(max_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1