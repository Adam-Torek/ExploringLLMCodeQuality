"""
Write a function to check if the given tuples contain the k or not.
assert check_K((10, 4, 5, 6, 8), 6) == True
"""


def check_K(tup, k):
    """
    :param tup: tuple
    :param k: int
    :return: bool
    """
    return k in tup


if __name__ == '__main__':
    print(check_K((10, 4, 5, 6, 8), 6))
    print(check_K((10, 4, 5, 6, 8), 10))
    print(check_K((10, 4, 5, 6, 8), 1))
    print(check_K((10, 4, 5, 6, 8), 8))
    print(check_K((10, 4, 5, 6, 8), 5))
    print(check_K((10, 4, 5, 6, 8), 4))
    print(check_K((10, 4, 5, 6, 8), 3))
    print(check_K((10, 4, 5, 6, 8), 2))
    print(check_K((10, 4, 5, 6, 8), 1))
    print(check_K((10, 4, 5, 6, 8), 0))
    print(check_K((10, 4, 5, 6, 8), -1))
    print(check_K((10, 4, 5, 6, 8), -10))
    print(check_K((10, 4, 5, 6, 8), -100))
    print(check_K((10, 4, 5, 6, 8), -1000))
    print(check_K((10, 4, 5, 6, 8), -10000))
    print(check_K((10, 4, 5, 6, 8), -100000))
    print(check_K((10, 4, 5, 6, 8), -1000000))
    print(check_K((10, 4, 5, 6, 8), -10000000))
    print(check_K((10, 4, 5, 6, 8), -100000000))
    print(check_K((10, 4, 5, 6, 8), -1000000000))
    print(check_K((10, 4, 5, 6, 8), -10000000000))
    print(check_K((10, 4, 5, 6, 8), -100000000000))
    print(check_K((10, 4, 5, 6, 8), -1000000000000))
    print(check_K((10, 4, 5, 6, 8), -10000000000000))
    print(check_K((10, 4, 5, 6, 8), -100000000000000))
    print(check_K((10, 4, 5, 6, 8), -1000000000000000))
    print(check_K((10, 4, 5, 6, 8), -10000000000000000))
    print(check_K((10, 4, 5, 6, 8), -100000000000000000))
    print(check_K((10, 4, 5, 6, 8), -1000