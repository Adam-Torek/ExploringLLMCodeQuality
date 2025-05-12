"""
Write a python function to find sum of products of all possible sublists of a given list. https://www.geeksforgeeks.org/sum-of-products-of-all-possible-subarrays/
assert sum_Of_Subarray_Prod([1,2,3]) == 20
"""
from functools import reduce

def sum_Of_Subarray_Prod(arr):
    """
    :param arr: list of integers
    :return: sum of all possible subarray products
    """
    if len(arr) == 0:
        return 0
    elif len(arr) == 1:
        return arr[0]

    # calculate product of all elements in the list
    prod = reduce(lambda x, y: x * y, arr)

    # calculate sum of all subarrays products
    # subarray_sum_prod = [sum([reduce(lambda x, y: x * y, sublist) for sublist in power_set(arr)]) for _ in range(2**len(arr))]
    subarray_sum_prod = []
    for i in range(1, 1 << len(arr)):
        sublist = [arr[j] for j in range(len(arr)) if i & (1 << j)]
        subarray_sum_prod.append(reduce(lambda x, y: x * y, sublist) if len(sublist) > 0 else 1)

    return sum(subarray_sum_prod)

def power_set(arr):
    """
    :param arr: list of integers
    :return: list of all possible subsets of the given list
    """
    n = len(arr)
    power_set = [[]]
    for i in range(1, 1 << n):
        subset = []
        for j in range(n):
            if i & (1 << j):
                subset.append(arr[j])
        power_set.append(subset)
    return power_set

if __name__ == "__main__":
    assert sum_Of_Subarray_Prod([1, 2, 3]) == 20
    assert sum_Of_Subarray_Prod([1, 2, 3, 4]) == 232
    assert sum_Of_Subarray_Prod([1, 2, 3, 4, 5]) == 15504
    assert sum_Of_Subarray_Prod([1, 2, 3, 4, 5, 6]) == 348672000
    assert sum_Of_Subarray_Prod([1, 2, 3, 4, 5, 6, 7]) == 11240007277776000000
    assert sum_Of_Subarray_Prod([1, 2, 3, 4, 5, 6, 7, 8]) == 112400072777760768000000000
    assert sum_Of_Subarray_Prod([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 11240007277776076800000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000