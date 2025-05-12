"""
Write a function to find the specified number of largest products from two given lists, selecting one factor from each list.
assert large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],3)==[60, 54, 50]
"""

def large_product(list1, list2, n):
    """
    :param list1: list of integers
    :param list2: list of integers
    :param n: number of largest products to return
    :return: list of n largest products
    """
    if n > len(list1) or n > len(list2):
        raise ValueError("n must be less than or equal to the length of each list")
    if n < 1:
        raise ValueError("n must be greater than 0")
    if len(list1) == 0 or len(list2) == 0:
        raise ValueError("lists must not be empty")
    if len(list1) != len(list2):
        raise ValueError("lists must be the same length")
    if not all(isinstance(x, int) for x in list1):
        raise ValueError("list1 must contain only integers")
    if not all(isinstance(x, int) for x in list2):
        raise ValueError("list2 must contain only integers")
    if not all(x > 0 for x in list1):
        raise ValueError("list1 must contain only positive integers")
    if not all(x > 0 for x in list2):
        raise ValueError("list2 must contain only positive integers")
    if not all(x > 0 for x in list1):
        raise ValueError("list1 must contain only positive integers")
    if not all(x > 0 for x in list2):
        raise ValueError("list2 must contain only positive integers")

    list1.sort(reverse=True)
    list2.sort(reverse=True)
    return [list1[i] * list2[i] for i in range(n)]


if __name__ == "__main__":
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
    print(large_product([1, 2, 3, 4, 5, 6], [3, 6, 8, 9, 10,