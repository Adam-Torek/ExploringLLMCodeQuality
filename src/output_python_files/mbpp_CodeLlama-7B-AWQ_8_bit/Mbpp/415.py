"""
Write a python function to find a pair with highest product from a given array of integers.
assert max_Product([1,2,3,4,7,0,8,4]) == (7,8)
"""


def max_Product(arr):
    """
    :param arr: list of integers
    :return: tuple of two integers
    """
    max_product = 0
    first_index = 0
    second_index = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] * arr[j] > max_product:
                max_product = arr[i] * arr[j]
                first_index = i
                second_index = j
    return arr[first_index], arr[second_index]


if __name__ == '__main__':
    print(max_Product([1, 2, 3, 4, 7, 0, 8, 4]))
    print(max_Product([1, 2, 3, 4, 7, 0, 8, 4, 9, 10]))
    print(max_Product([1, 2, 3, 4, 7, 0, 8, 4, 9, 10, 11]))
    print(max_Product([1, 2, 3, 4, 7, 0, 8, 4, 9, 10, 11, 12]))
    print(max_Product([1, 2, 3, 4, 7, 0, 8, 4, 9, 10, 11, 12, 13]))
    print(max_Product([1, 2, 3, 4, 7, 0, 8, 4, 9, 10, 11, 12, 13, 14]))
    print(max_Product([1, 2, 3, 4, 7, 0, 8, 4, 9, 10, 11, 12, 13, 14, 15]))
    print(max_Product([1, 2, 3, 4, 7, 0, 8, 4, 9, 10, 11, 12, 13, 14, 15, 16]))
    print(max_Product([1, 2, 3, 4, 7, 0, 8, 4, 9, 10, 11, 12, 13, 14, 15, 16, 17]))
    print(max_Product([1, 2, 3, 4, 7, 0, 8, 4, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]))
    print(max_Product([1, 2, 3, 4, 7, 0, 8, 4, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]))
    print(max_Product([1, 2, 3, 4, 7, 0, 8, 4, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))
    print(max_Product([1, 2, 3, 4, 7, 0, 8, 4, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]))
    print(max_Product([1, 2, 3, 4, 7, 0, 8, 4, 9, 10, 11, 12, 13, 14, 15, 16,