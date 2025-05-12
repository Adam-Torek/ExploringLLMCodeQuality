"""
Write a function to find perfect squares between two given numbers.
assert perfect_squares(1,30)==[1, 4, 9, 16, 25]
"""


def perfect_squares(a, b):
    """
    :param a: int
    :param b: int
    :return: list
    """
    result = []
    for i in range(a, b + 1):
        if i ** 0.5 == int(i ** 0.5):
            result.append(i)
    return result


if __name__ == '__main__':
    print(perfect_squares(1, 30))
    print(perfect_squares(1, 10))
    print(perfect_squares(1, 1))
    print(perfect_squares(1, 0))
    print(perfect_squares(1, -1))
    print(perfect_squares(1, -10))
    print(perfect_squares(1, -100))
    print(perfect_squares(1, -1000))
    print(perfect_squares(1, -10000))
    print(perfect_squares(1, -100000))
    print(perfect_squares(1, -1000000))
    print(perfect_squares(1, -10000000))
    print(perfect_squares(1, -100000000))
    print(perfect_squares(1, -1000000000))
    print(perfect_squares(1, -10000000000))
    print(perfect_squares(1, -100000000000))
    print(perfect_squares(1, -1000000000000))
    print(perfect_squares(1, -10000000000000))
    print(perfect_squares(1, -100000000000000))
    print(perfect_squares(1, -1000000000000000))
    print(perfect_squares(1, -10000000000000000))
    print(perfect_squares(1, -100000000000000000))
    print(perfect_squares(1, -1000000000000000000))
    print(perfect_squares(1, -10000000000000000000))
    print(perfect_squares(1, -100000000000000000000))
    print(perfect_squares(1, -1000000000000000000000))
    print(perfect_squares(1, -10000000000000000000000))
    print(perfect_squares(1, -100000000000000000000000))
    print(perfect_squares(1, -1000000000000000000000000))
    print(perfect_squares(1, -10000000000000000000000000))
    print(perfect_squares(1, -100000000000000000000000000))
    print(perfect_squares(1, -1000000000000000000000000000))
    print(perfect_squares(1, -1