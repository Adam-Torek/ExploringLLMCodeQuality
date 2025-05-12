"""
Write a function to find the maximum sum of increasing subsequence from prefix until ith index and also including a given kth element which is after i, i.e., k > i .
assert max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 4, 6) == 11
"""


def max_sum_increasing_subseq(arr, n, k, i):
    if i == k:
        return arr[i]
    if i == 0:
        return max(arr[i], arr[i + 1])
    return max(max_sum_increasing_subseq(arr, n, k, i + 1), arr[i] + max_sum_increasing_subseq(arr, n, k, i + 1))


if __name__ == '__main__':
    print(max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 4, 6))
    print(max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 4, 5))
    print(max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 4, 4))
    print(max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 4, 3))
    print(max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 4, 2))
    print(max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 4, 1))
    print(max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 4, 0))
    print(max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 4, -1))
    print(max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 4, -2))
    print(max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 4, -3))
    print(max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 4, -4))
    print(max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 4, -5))
    print(max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 4, -6))
    print(max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 4, -7))
    print(max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 4, -8))
    print(max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 4, -9))
    print(max_sum_increasing_subseq([1, 101, 2, 3, 100,