"""
Write a function to get all lucid numbers smaller than or equal to a given integer.
assert get_ludic(10) == [1, 2, 3, 5, 7]
"""


def get_ludic(n):
    """
    :param n: int
    :return: list
    """
    ludic = [1]
    for i in range(2, n + 1):
        if i not in ludic:
            ludic.append(i)
            for j in range(2, i):
                if i % j == 0:
                    ludic.remove(i)
    return ludic


if __name__ == '__main__':
    print(get_ludic(10))
    print(get_ludic(100))
    print(get_ludic(1000))
    print(get_ludic(10000))
    print(get_ludic(100000))
    print(get_ludic(1000000))
    print(get_ludic(10000000))
    print(get_ludic(100000000))
    print(get_ludic(1000000000))
    print(get_ludic(10000000000))
    print(get_ludic(100000000000))
    print(get_ludic(1000000000000))
    print(get_ludic(10000000000000))
    print(get_ludic(100000000000000))
    print(get_ludic(1000000000000000))
    print(get_ludic(10000000000000000))
    print(get_ludic(100000000000000000))
    print(get_ludic(1000000000000000000))
    print(get_ludic(10000000000000000000))
    print(get_ludic(100000000000000000000))
    print(get_ludic(1000000000000000000000))
    print(get_ludic(10000000000000000000000))
    print(get_ludic(100000000000000000000000))
    print(get_ludic(1000000000000000000000000))
    print(get_ludic(10000000000000000000000000))
    print(get_ludic(100000000000000000000000000))
    print(get_ludic(1000000000000000000000000000))
    print(get_ludic(10000000000000000000000000000))
    print(get_ludic(100000000000000000000000000000))
    print(get_ludic(1000000000000000000000000000000))
    print(get_ludic(100000000000000000