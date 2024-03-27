"""
Write a python function to find sum of products of all possible sublists of a given list. https://www.geeksforgeeks.org/sum-of-products-of-all-possible-subarrays/
assert sum_Of_Subarray_Prod([1,2,3]) == 20
"""
from functools import reduce

def sum_of_subarray_prod(arr):
    """
    :param arr: list of integers
    :return: sum of products of all possible sublists
    """
    if len(arr) == 0:
        return 0
    elif len(arr) == 1:
        return arr[0]

    # calculate product of all elements in the list
    prod = reduce(lambda x, y: x * y, arr)

    # calculate sum of products of all possible sublists
    # sublist can be empty or have any length between 1 and n
    return sum(reduce(lambda x, y: x * y, sublist) for sublist in itertools.chain([[]], itertools.combinations(arr, range(1, len(arr)+1)))) + prod

import itertools

if __name__ == "__main__":
    assert sum_of_subarray_prod([1, 2, 3]) == 20
    assert sum_of_subarray_prod([-1, 1, 1, 1, -1]) == 0
    assert sum_of_subarray_prod([1, 1, 1, 1, 1]) == 151200
    assert sum_of_subarray_prod([1, 2, 3, 4, 5]) == 6227020800
    assert sum_of_subarray_prod([0, 0, 0, 0, 0]) == 1
    assert sum_of_subarray_prod([1]) == 1
    assert sum_of_subarray_prod([]) == 0</s>