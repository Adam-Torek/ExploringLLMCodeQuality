"""
Write a python function to find the sum of all odd natural numbers within the range l and r.
assert sum_in_range(2,5) == 8
"""


def sum_in_range(l, r):
    """
    :param l: int
    :param r: int
    :return: int
    """
    if l > r:
        return 0
    return (l + r) * (r - l + 1) // 2


if __name__ == '__main__':
    print(sum_in_range(2, 5))
    print(sum_in_range(1, 10))
    print(sum_in_range(1, 100))
    print(sum_in_range(1, 1000))
    print(sum_in_range(1, 10000))
    print(sum_in_range(1, 100000))
    print(sum_in_range(1, 1000000))
    print(sum_in_range(1, 10000000))
    print(sum_in_range(1, 100000000))
    print(sum_in_range(1, 1000000000))
    print(sum_in_range(1, 10000000000))
    print(sum_in_range(1, 100000000000))
    print(sum_in_range(1, 1000000000000))
    print(sum_in_range(1, 10000000000000))
    print(sum_in_range(1, 100000000000000))
    print(sum_in_range(1, 1000000000000000))
    print(sum_in_range(1, 10000000000000000))
    print(sum_in_range(1, 100000000000000000))
    print(sum_in_range(1, 1000000000000000000))
    print(sum_in_range(1, 10000000000000000000))
    print(sum_in_range(1, 100000000000000000000))
    print(sum_in_range(1, 1000000000000000000000))
    print(sum_in_range(1, 10000000000000000000000))
    print(sum_in_range(1, 100000000000000000000000))
    print(sum_in_range(1, 1000000000000000000000000))
    print(sum_in_range(1, 10000000000000000000000000))
    print(sum_in_range(1, 100000000000000000000000000))
    print(sum_in_range(1, 1000000000000000000000000000))
    print(sum_in_range(1, 10000000000000000000000000000))
    print(sum_in_range(1, 100000000000000000000000000000))