"""
Write a function to find minimum k records from tuple list. https://www.geeksforgeeks.org/python-find-minimum-k-records-from-tuple-list/ - in this case a verbatim copy of test cases
assert min_k([('Manjeet', 10), ('Akshat', 4), ('Akash', 2), ('Nikhil', 8)], 2) == [('Akash', 2), ('Akshat', 4)]
"""
from heapq import nsmallest

def min_k(arr, k):
    """
    :param arr: list of tuples
    :param k: int
    :return: list of tuples
    """
    return list(nsmallest(k, arr))

if __name__ == "__main__":
    assert min_k([('Manjeet', 10), ('Akshat', 4), ('Akash', 2), ('Nikhil', 8)], 2) == [('Akash', 2), ('Akshat', 4)]
    assert min_k([(1, 1), (1, 2), (1, 3), (1, 4), (1, 5)], 3) == [(1, 1), (1, 2), (1, 3)]
    assert min_k([(1, 1), (1, 2), (1, 3), (1, 4), (1, 5)], 5) == [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5)]
    assert min_k([(1, 1), (1, 2), (1, 3), (1, 4), (1, 5)], 10) == [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5)]
    assert min_k([], 1) == []
    assert min_k([], 2) == []
    assert min_k([], 3) == []
    assert min_k([], 10) == []
    assert min_k([], k=1) == []
    assert min_k([], k=2) == []
    assert min_k([], k=3) == []
    assert min_k([], k=10) == []
    assert min_k([], k=-1) == []
    assert min_k([], k=float('inf')) == []
    assert min_k([], k=0) == []
    assert min_k([], k=None) == []
    assert min_k([], k=5.5) == []
    assert min_k([], k='string') == []
    assert min_k([], k=True) == []
    assert min_k([], k=False) == []
    assert min_k([], k=object()) == []
    assert min_k([], k=list()) == []
    assert min_k([], k=tuple()) == []
    assert min_k([], k=dict()) == []
    assert min_k([], k=set()) == []
    assert min_k([], k=range(10)) == []
    assert min_k([], k=xrange(10)) == []
    assert min_k([], k=itertools.count(1)) == []
    assert min_k([], k=itertools.cycle([1, 2, 3])) == []
    assert min_k([], k=itertools.islice(itertools.repeat((1, 1), 10), 2)) == []
    assert min_k([], k=itertools.accumulate([(1, 1), (1, 2), (1, 3), (1, 4), (1, 5)], lambda x, y: (x[0] + y[0], x[1] + y[1]))) == []
    assert min_k([], k=itertools.groupby([(1, 1), (1, 2), (1, 3), (1, 4), (1, 5)])) == []
    assert min_k([], k=itertools.product(