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
    max_product_index = 0
    min_product = 0
    min_product_index = 0
    for i in range(len(arr)):
        if arr[i] > max_product:
            max_product = arr[i]
            max_product_index = i
        if arr[i] < min_product:
            min_product = arr[i]
            min_product_index = i
    return arr[max_product_index], arr[min_product_index]


if __name__ == '__main__':
    print(max_Product([1, 2, 3, 4, 7, 0, 8, 4]))
    print(max_Product([1, 2, 3, 4, 7, 0, 8, 4, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]))
    print(max_Product([1, 2, 3, 4, 7, 0, 8, 4, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94