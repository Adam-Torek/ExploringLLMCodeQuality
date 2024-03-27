"""
Write a function to find the maximum sum of increasing subsequence from prefix until ith index and also including a given kth element which is after i, i.e., k > i .
assert max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 4, 6) == 11
"""


def max_sum_increasing_subseq(arr, i, k, n):
    if i == n:
        return 0
    if k == n:
        return arr[i]
    return max(max_sum_increasing_subseq(arr, i + 1, k, n), arr[i] + max_sum_increasing_subseq(arr, i + 1, k + 1, n))


if __name__ == '__main__':
    print(max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 4, 6))
    print(max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 4, 7))
    print(max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 4, 8))
    print(max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 4, 9))
    print(max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 4, 10))
    print(max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 4, 11))
    print(max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 4, 12))
    print(max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 4, 13))
    print(max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 4, 14))
    print(max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 4, 15))
    print(max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 4, 16))
    print(max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 4, 17))
    print(max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 4, 18))
    print(max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 4, 19))
    print(max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 4, 20))
    print(max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 4, 21))
    print(max_sum_increasing_subseq([1, 101, 2, 3, 1