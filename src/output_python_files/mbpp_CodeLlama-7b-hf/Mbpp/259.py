"""
Write a function to maximize the given two tuples.
assert maximize_elements(((1, 3), (4, 5), (2, 9), (1, 10)), ((6, 7), (3, 9), (1, 1), (7, 3))) == ((6, 7), (4, 9), (2, 9), (7, 10))
"""


def maximize_elements(t1, t2):
    """
    :param t1: tuple of tuples
    :param t2: tuple of tuples
    :return: tuple of tuples
    """
    t1_max = max(t1)
    t2_max = max(t2)
    if t1_max[0] == t2_max[0]:
        return t1_max[1] > t2_max[1] and t1 or t2_max
    else:
        return t1_max[0] > t2_max[0] and t1 or t2_max


if __name__ == '__main__':
    print(maximize_elements(((1, 3), (4, 5), (2, 9), (1, 10)), ((6, 7), (3, 9), (1, 1), (7, 3))))
    print(maximize_elements(((1, 3), (4, 5), (2, 9), (1, 10)), ((6, 7), (3, 9), (1, 1), (7, 3), (1, 10))))
    print(maximize_elements(((1, 3), (4, 5), (2, 9), (1, 10)), ((6, 7), (3, 9), (1, 1), (7, 3), (1, 10), (1, 10))))
    print(maximize_elements(((1, 3), (4, 5), (2, 9), (1, 10)), ((6, 7), (3, 9), (1, 1), (7, 3), (1, 10), (1, 10), (1, 10))))
    print(maximize_elements(((1, 3), (4, 5), (2, 9), (1, 10)), ((6, 7), (3, 9), (1, 1), (7, 3), (1, 10), (1, 10), (1, 10), (1, 10))))
    print(maximize_elements(((1, 3), (4, 5), (2, 9), (1, 10)), ((6, 7), (3, 9), (1, 1), (7, 3), (1, 10), (1, 10), (1, 10), (1, 10), (1, 10))))
    print(maximize_elements(((1, 3), (4, 5), (2, 9), (1, 10)), ((6, 7), (3, 9), (1, 1), (7, 3), (1, 10), (1, 10), (1, 10), (1, 10), (1, 10), (1, 10))))
    print(maximize_elements(((1, 3), (4, 5), (2, 9), (1, 10)), ((6, 7), (3, 9), (1, 1), (7, 3), (1, 10), (1, 10), (1, 10), (1, 10), (1, 10), (1, 10), (1, 10))))
    print(maximize_elements(((1, 3), (4, 5), (2, 9), (1, 10)), ((6, 7), (3, 9), (1, 1), (7, 3), (1, 10), (1, 10), (1, 10), (1, 10), (1, 10), (1, 10), (