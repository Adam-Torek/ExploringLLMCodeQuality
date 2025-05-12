"""
Write a function to maximize the given two tuples.
assert maximize_elements(((1, 3), (4, 5), (2, 9), (1, 10)), ((6, 7), (3, 9), (1, 1), (7, 3))) == ((6, 7), (4, 9), (2, 9), (7, 10))
"""


def maximize_elements(tuple1, tuple2):
    """
    :param tuple1: tuple of tuples
    :param tuple2: tuple of tuples
    :return: tuple of tuples
    """
    result = []
    for i in range(len(tuple1)):
        if tuple1[i][0] > tuple2[i][0]:
            result.append(tuple1[i])
        elif tuple1[i][0] < tuple2[i][0]:
            result.append(tuple2[i])
        else:
            if tuple1[i][1] > tuple2[i][1]:
                result.append(tuple1[i])
            else:
                result.append(tuple2[i])
    return result


if __name__ == '__main__':
    print(maximize_elements(((1, 3), (4, 5), (2, 9), (1, 10)), ((6, 7), (3, 9), (1, 1), (7, 3))))
    print(maximize_elements(((1, 3), (4, 5), (2, 9), (1, 10)), ((6, 7), (3, 9), (1, 1), (7, 3), (1, 1))))
    print(maximize_elements(((1, 3), (4, 5), (2, 9), (1, 10)), ((6, 7), (3, 9), (1, 1), (7, 3), (1, 1), (1, 1))))
    print(maximize_elements(((1, 3), (4, 5), (2, 9), (1, 10)), ((6, 7), (3, 9), (1, 1), (7, 3), (1, 1), (1, 1), (1, 1))))
    print(maximize_elements(((1, 3), (4, 5), (2, 9), (1, 10)), ((6, 7), (3, 9), (1, 1), (7, 3), (1, 1), (1, 1), (1, 1), (1, 1))))
    print(maximize_elements(((1, 3), (4, 5), (2, 9), (1, 10)), ((6, 7), (3, 9), (1, 1), (7, 3), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1))))
    print(maximize_elements(((1, 3), (4, 5), (2, 9), (1, 10)), ((6, 7), (3, 9), (1, 1), (7, 3), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1))))
    print(maximize_elements(((1, 3), (4, 5), (2, 9), (1, 10)), ((6, 7), (3, 9), (1, 1), (7, 3), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1))))
    print(maximize_elements(((1, 3), (4, 5), (2, 9), (1, 10)), ((6, 7), (3, 9), (1, 1), (7, 3), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1),