"""
Write a function to find the maximum sum of increasing subsequence from prefix until ith index and also including a given kth element which is after i, i.e., k > i .
assert max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 4, 6) == 11
"""


def max_sum_increasing_subseq(arr, i, k, j):
    if i == j:
        return arr[i]
    if i > j:
        return 0
    if i == k:
        return arr[i]
    if i > k:
        return max(max_sum_increasing_subseq(arr, i, k, j), max_sum_increasing_subseq(arr, i + 1, k, j))
    return max(max_sum_increasing_subseq(arr, i, k, j), arr[i] + max_sum_increasing_subseq(arr, i + 1, k, j))


if __name__ == '__main__':
    print(max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 4, 6))
    print(max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 4, 5))
    print(max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 4, 4))
    print(max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 4, 3))
    print(max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 4, 2))
    print(max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 4, 1))
    print(max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 4, 0))
    print(max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 3, 6))
    print(max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 3, 5))
    print(max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 3, 4))
    print(max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 3, 3))
    print(max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 3, 2))
    print(max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 3, 1))
    print(max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 3, 0))
    print(max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 2, 6))
    print(max_sum_increasing_subseq([1, 101, 2, 3,