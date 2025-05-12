"""
Write a function to find the specified number of largest products from two given lists, selecting one factor from each list.
assert large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],3)==[60, 54, 50]
"""


def large_product(list1, list2, n):
    """
    :param list1: list of numbers
    :param list2: list of numbers
    :param n: number of largest products to return
    :return: list of n largest products
    """
    if len(list1) < n or len(list2) < n:
        raise ValueError("Lists must be at least as long as n")
    if len(list1) == n and len(list2) == n:
        return [list1[i] * list2[i] for i in range(n)]
    if len(list1) > len(list2):
        list1, list2 = list2, list1
    list1.sort(reverse=True)
    list2.sort(reverse=True)
    return [list1[i] * list2[i] for i in range(n)]


if __name__ == '__main__':
    print(large_product([1, 2, 3, 4, 5, 6], [3, 6, 8, 9, 10, 6], 3))
    print(large_product([1, 2, 3, 4, 5, 6], [3, 6, 8, 9, 10, 6], 4))
    print(large_product([1, 2, 3, 4, 5, 6], [3, 6, 8, 9, 10, 6], 5))
    print(large_product([1, 2, 3, 4, 5, 6], [3, 6, 8, 9, 10, 6], 6))
    print(large_product([1, 2, 3, 4, 5, 6], [3, 6, 8, 9, 10, 6], 7))
    print(large_product([1, 2, 3, 4, 5, 6], [3, 6, 8, 9, 10, 6], 8))
    print(large_product([1, 2, 3, 4, 5, 6], [3, 6, 8, 9, 10, 6], 9))
    print(large_product([1, 2, 3, 4, 5, 6], [3, 6, 8, 9, 10, 6], 10))
    print(large_product([1, 2, 3, 4, 5, 6], [3, 6, 8, 9, 10, 6], 11))
    print(large_product([1, 2, 3, 4, 5, 6], [3, 6, 8, 9, 10, 6], 12))
    print(large_product([1, 2, 3, 4, 5, 6], [3, 6, 8, 9, 10, 6], 13))
    print(large_product([1, 2, 3, 4, 5, 6], [3, 6, 8, 9, 10, 6], 14))
    print(large_product([1, 2, 3, 4, 5, 6], [3, 6, 8, 9, 10, 6], 15))
    print(large_product([1, 2, 3, 4, 5, 6], [3, 6, 8, 9, 10, 6], 16))
    print(large_product([1, 2, 3, 4, 5, 6], [3, 6, 8, 9, 10, 6], 17))