"""
Write a function to find the maximum product formed by multiplying numbers of an increasing subsequence of that array.
assert max_product([3, 100, 4, 5, 150, 6]) == 3000
"""


def max_product(arr):
    """
    :param arr: list of numbers
    :return: maximum product of an increasing subsequence
    """
    if not arr:
        return 0
    if len(arr) == 1:
        return arr[0]

    max_product = arr[0]
    max_product_so_far = arr[0]
    min_product = arr[0]
    min_product_so_far = arr[0]

    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            max_product = max(arr[i], max_product * arr[i])
            min_product = min(arr[i], min_product * arr[i])
        else:
            max_product = max(arr[i], min_product * arr[i])
            min_product = min(arr[i], max_product * arr[i])

        max_product_so_far = max(max_product, max_product_so_far)
        min_product_so_far = min(min_product, min_product_so_far)

    return max_product_so_far


if __name__ == '__main__':
    print(max_product([3, 100, 4, 5, 150, 6]))
    print(max_product([100, 2, 3, 4, 5, 6, 7, 8, 9, 1000]))
    print(max_product([100, 2, 3, 4, 5, 6, 7, 8, 9, 1000, 1000000]))
    print(max_product([100, 2, 3, 4, 5, 6, 7, 8, 9, 1000, 1000000, 10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000