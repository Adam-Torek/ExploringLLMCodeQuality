"""
Write a function to find the specified number of largest products from two given lists, selecting one factor from each list.
assert large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],3)==[60, 54, 50]
"""

def large_product(list1, list2, n):
    """
    :param list1: list of integers
    :param list2: list of integers
    :param n: number of largest products to be returned
    :return: list of n largest products
    """
    result = []
    for i in range(len(list1)):
        for j in range(len(list2)):
            product = list1[i] * list2[j]
            result.append(product)
    result.sort(reverse=True)
    return result[:n]

assert large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],3)==[60, 54, 50]