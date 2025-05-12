"""
Write a function to find the dissimilar elements in the given two tuples.
assert find_dissimilar((3, 4, 5, 6), (5, 7, 4, 10)) == (3, 6, 7, 10)
"""


def find_dissimilar(t1, t2):
    """
    :param t1: tuple
    :param t2: tuple
    :return: tuple
    """
    return tuple(sorted(set(t1) ^ set(t2)))


if __name__ == '__main__':
    print(find_dissimilar((3, 4, 5, 6), (5, 7, 4, 10)))
    print(find_dissimilar((1, 2, 3, 4), (1, 2, 3, 4)))
    print(find_dissimilar((1, 2, 3, 4), (1, 2, 3, 4, 5)))
    print(find_dissimilar((1, 2, 3, 4), (1, 2, 3, 4, 5, 6)))
    print(find_dissimilar((1, 2, 3, 4), (1, 2, 3, 4, 5, 6, 7)))
    print(find_dissimilar((1, 2, 3, 4), (1, 2, 3, 4, 5, 6, 7, 8)))
    print(find_dissimilar((1, 2, 3, 4), (1, 2, 3, 4, 5, 6, 7, 8, 9)))
    print(find_dissimilar((1, 2, 3, 4), (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)))
    print(find_dissimilar((1, 2, 3, 4), (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)))
    print(find_dissimilar((1, 2, 3, 4), (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)))
    print(find_dissimilar((1, 2, 3, 4), (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)))
    print(find_dissimilar((1, 2, 3, 4), (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)))
    print(find_dissimilar((1, 2, 3, 4), (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)))
    print(find_dissimilar((1, 2, 3, 4), (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16)))
    print(find_dissimilar((1, 2, 3, 4), (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17)))
    print(find_dissimilar((1, 2, 3, 4), (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 1