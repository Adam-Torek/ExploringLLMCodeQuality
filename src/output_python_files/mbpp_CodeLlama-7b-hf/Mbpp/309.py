"""
Write a python function to find the maximum of two numbers.
assert maximum(5,10) == 10
"""


def maximum(a, b):
    """
    :param a: int
    :param b: int
    :return: int
    """
    if a > b:
        return a
    else:
        return b


if __name__ == '__main__':
    print(maximum(5, 10))
    print(maximum(10, 5))
    print(maximum(10, 10))
    print(maximum(10, 100))
    print(maximum(100, 10))
    print(maximum(100, 100))
    print(maximum(100, 1000))
    print(maximum(1000, 100))
    print(maximum(1000, 1000))
    print(maximum(1000, 10000))
    print(maximum(10000, 1000))
    print(maximum(10000, 10000))
    print(maximum(10000, 100000))
    print(maximum(100000, 10000))
    print(maximum(100000, 100000))
    print(maximum(100000, 1000000))
    print(maximum(1000000, 100000))
    print(maximum(1000000, 1000000))
    print(maximum(1000000, 10000000))
    print(maximum(10000000, 1000000))
    print(maximum(10000000, 10000000))
    print(maximum(10000000, 100000000))
    print(maximum(100000000, 10000000))
    print(maximum(100000000, 100000000))
    print(maximum(100000000, 1000000000))
    print(maximum(1000000000, 100000000))
    print(maximum(1000000000, 1000000000))
    print(maximum(1000000000, 10000000000))
    print(maximum(10000000000, 1000000000))
    print(maximum(10000000000, 10000000000))
    print(maximum(10000000000, 100000000000))
    print(maximum(100000000000, 10000000000))
    print(maximum(100000000000, 100000000000))
    print(maximum(100000000000, 1000000000000))
    print(maximum(1000000000000, 100000000000))
    print(maximum(1000000000000, 1000000000000))
    print(maximum(1000000000000, 10000000000000))
    print(maximum(10000