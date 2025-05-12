"""
Write a function to find the maximum product formed by multiplying numbers of an increasing subsequence of that array.
assert max_product([3, 100, 4, 5, 150, 6]) == 3000
"""


def max_product(arr):
    if len(arr) == 0:
        return 0
    if len(arr) == 1:
        return arr[0]
    if len(arr) == 2:
        return max(arr[0], arr[1])

    max_product = arr[0]
    min_product = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > max_product:
            max_product = arr[i]
        if arr[i] < min_product:
            min_product = arr[i]
        if max_product < min_product:
            max_product = max_product * min_product
            min_product = arr[i]
    return max_product


if __name__ == '__main__':
    print(max_product([3, 100, 4, 5, 150, 6]))
    print(max_product([1, 2, 3, 4, 5]))
    print(max_product([1, 2, 3, 4, 5, 6]))
    print(max_product([1, 2, 3, 4, 5, 6, 7]))
    print(max_product([1, 2, 3, 4, 5, 6, 7, 8]))
    print(max_product([1, 2, 3, 4, 5, 6, 7, 8, 9]))
    print(max_product([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    print(max_product([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))
    print(max_product([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))
    print(max_product([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]))
    print(max_product([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]))
    print(max_product([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]))
    print(max_product([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]))
    print(max_product([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]))
    print(max_product([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]))
    print(max_product([1, 2, 3, 4, 5,