"""
Write a python function to find the product of the array multiplication modulo n.
assert find_remainder([ 100, 10, 5, 25, 35, 14 ],11) ==9
"""


def find_remainder(arr, n):
    """
    :param arr: list of integers
    :param n: integer
    :return: integer
    """
    product = 1
    for i in arr:
        product = (product * i) % n
    return product


if __name__ == '__main__':
    print(find_remainder([100, 10, 5, 25, 35, 14], 11))
    print(find_remainder([100, 10, 5, 25, 35, 14], 10))
    print(find_remainder([100, 10, 5, 25, 35, 14], 100))
    print(find_remainder([100, 10, 5, 25, 35, 14], 1000))
    print(find_remainder([100, 10, 5, 25, 35, 14], 10000))
    print(find_remainder([100, 10, 5, 25, 35, 14], 100000))
    print(find_remainder([100, 10, 5, 25, 35, 14], 1000000))
    print(find_remainder([100, 10, 5, 25, 35, 14], 10000000))
    print(find_remainder([100, 10, 5, 25, 35, 14], 100000000))
    print(find_remainder([100, 10, 5, 25, 35, 14], 1000000000))
    print(find_remainder([100, 10, 5, 25, 35, 14], 10000000000))
    print(find_remainder([100, 10, 5, 25, 35, 14], 100000000000))
    print(find_remainder([100, 10, 5, 25, 35, 14], 1000000000000))
    print(find_remainder([100, 10, 5, 25, 35, 14], 10000000000000))
    print(find_remainder([100, 10, 5, 25, 35, 14], 100000000000000))
    print(find_remainder([100, 10, 5, 25, 35, 14], 1000000000000000))
    print(find_remainder([100, 10, 5, 25, 35, 14], 10000000000000000))
    print(find_remainder([100, 10, 5, 25, 35, 14], 100000000000000000))
    print(find_remainder([100, 10, 5, 25, 35, 14], 1000000000000000000))
    print(find_remainder([100, 10, 5, 25,