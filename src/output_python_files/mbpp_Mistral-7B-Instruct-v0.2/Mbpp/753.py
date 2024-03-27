"""
Write a function to find minimum k records from tuple list. https://www.geeksforgeeks.org/python-find-minimum-k-records-from-tuple-list/ - in this case a verbatim copy of test cases
assert min_k([('Manjeet', 10), ('Akshat', 4), ('Akash', 2), ('Nikhil', 8)], 2) == [('Akash', 2), ('Akshat', 4)]
"""
from heapq import nlargest

def min_k(arr, k):
    """
    :param arr: list of tuples
    :param k: number of tuples to return
    :return: list of tuples
    """
    return list(nlargest(k, arr))

if __name__ == "__main__":
    assert min_k([('Manjeet', 10), ('Akshat', 4), ('Akash', 2), ('Nikhil', 8)], 2) == [('Akshat', 4), ('Manjeet', 10)]
    assert min_k([(1, 2), (3, 4), (1, 5), (3, 6), (1, 7)], 3) == [(1, 7), (1, 5), (1, 2)]
    assert min_k([(1, 2), (3, 4), (1, 5), (3, 6), (1, 7)], 5) == [(1, 7), (1, 5), (1, 2), (3, 6), (3, 4)]
    assert min_k([(1, 2), (3, 4), (1, 5), (3, 6), (1, 7)], 10) == [(1, 7), (1, 5), (1, 2), (3, 6), (3, 4), (1, 2), (1, 2), (1, 2), (1, 2), (1, 2)]
    assert min_k([], 1) == []
    assert min_k([(1, 2), (3, 4), (1, 5), (3, 6), (1, 7)], 11) == [(1, 7), (1, 5), (1, 2), (3, 6), (3, 4), (1, 2), (1, 2), (1, 2), (1, 2), (1, 2), (1, 2)]
    assert min_k([(1, 2), (3, 4), (1, 5), (3, 6), (1, 7)], -1) == [(1, 7), (1, 5), (1, 2), (3, 6), (3, 4), (1, 2), (1, 2), (1, 2), (1, 2), (1, 2)]
    assert min_k([(1, 2), (3, 4), (1, 5), (3, 6), (1, 7)], 0) == []
    assert min_k([(1, 2), (3, 4), (1, 5), (3, 6), (1, 7)], 6) == [(3, 6), (3, 4), (1, 5), (1, 2), (1, 2), (1, 2)]
    assert min_k([(1, 2), (3, 4), (1, 5), (3, 6), (1, 7)], 12) == [(1, 7), (1, 5), (1, 2), (3, 6), (3, 4), (1, 2), (1, 2), (1, 2), (1, 2), (1, 2), (1, 2), (1, 2), (1, 2)]
    assert min_k([(1, 2), (3, 4), (1, 5), (3, 6), (1, 7)], 13) == [(1, 7),