"""
Write a python function to find the product of the array multiplication modulo n.
assert find_remainder([ 100, 10, 5, 25, 35, 14 ],11) ==9
"""


def find_remainder(arr, n):
    """
    :param arr: array of integers
    :param n: modulo
    :return: product of the array modulo n
    """
    return reduce(lambda x, y: (x * y) % n, arr)


if __name__ == '__main__':
    print(find_remainder([100, 10, 5, 25, 35, 14], 11))
    print(find_remainder([100, 10, 5, 25, 35, 14], 10))
    print(find_remainder([100, 10, 5, 25, 35, 14], 9))
    print(find_remainder([100, 10, 5, 25, 35, 14], 8))
    print(find_remainder([100, 10, 5, 25, 35, 14], 7))
    print(find_remainder([100, 10, 5, 25, 35, 14], 6))
    print(find_remainder([100, 10, 5, 25, 35, 14], 5))
    print(find_remainder([100, 10, 5, 25, 35, 14], 4))
    print(find_remainder([100, 10, 5, 25, 35, 14], 3))
    print(find_remainder([100, 10, 5, 25, 35, 14], 2))
    print(find_remainder([100, 10, 5, 25, 35, 14], 1))
    print(find_remainder([100, 10, 5, 25, 35, 14], 0))
    print(find_remainder([100, 10, 5, 25, 35, 14], -1))
    print(find_remainder([100, 10, 5, 25, 35, 14], -2))
    print(find_remainder([100, 10, 5, 25, 35, 14], -3))
    print(find_remainder([100, 10, 5, 25, 35, 14], -4))
    print(find_remainder([100, 10, 5, 25, 35, 14], -5))
    print(find_remainder([100, 10, 5, 25, 35, 14], -6))
    print(find_remainder([100, 10, 5, 25, 35, 14], -7))
    print(find_remainder([100, 10, 5, 25, 35, 14], -8))
    print(find_remainder([100, 10, 5, 25, 35, 14], -9))
    print(find_remainder([100, 10, 5, 25, 35, 14], -10))
    print(find_remainder([100, 10, 5, 25, 35, 14], -11))
    print