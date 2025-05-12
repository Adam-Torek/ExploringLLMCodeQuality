"""
Write a function to find the maximum sum of increasing subsequence from prefix until ith index and also including a given kth element which is after i, i.e., k > i.
assert max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 4, 6) == 11
"""

def max_sum_increasing_subseq(arr, k, i, j):
    """
    :param arr: list of integers
    :param k: index of element to be included in increasing subsequence
    :param i: start index of increasing subsequence
    :param j: end index of increasing subsequence
    :return: maximum sum of increasing subsequence
    """
    if i > j:
        return 0
    if k > j:
        return 0
    if k == j:
        return arr[k]
    if k == i:
        return arr[k] + max_sum_increasing_subseq(arr, k, i, j - 1)
    return max(arr[k] + max_sum_increasing_subseq(arr, k, i, k - 1), max_sum_increasing_subseq(arr, k, k + 1, j))


def test_max_sum_increasing_subseq():
    assert max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 4, 6) == 11
    assert max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 4, 5) == 10
    assert max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 4, 4) == 101
    assert max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 4, 3) == 101
    assert max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 4, 2) == 101
    assert max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 4, 1) == 101
    assert max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 4, 0) == 101
    assert max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 3, 6) == 101
    assert max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 3, 5) == 101
    assert max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 3, 4) == 101
    assert max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 3, 3) == 101
    assert max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 3, 2) == 101
    assert max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 3, 1) == 101
    assert max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 3, 0) == 101
    assert max_sum_increasing_subseq([1, 101, 2,