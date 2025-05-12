"""
Write a function to find the maximum sum of increasing subsequence from prefix until ith index and also including a given kth element which is after i, i.e., k > i .
assert max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 4, 6) == 11
"""

def max_sum_increasing_subseq(arr, i, k, n):
    """
    :param arr: list of integers
    :param i: index of prefix sum
    :param k: index of kth element
    :param n: length of array
    :return: maximum sum of increasing subsequence from prefix until ith index and also including a given kth element which is after i, i.e., k > i
    """
    if i == n:
        return max(arr[i-1:])
    else:
        return max(arr[i-1:k] + arr[k+1:])

assert max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 4, 6) == 11