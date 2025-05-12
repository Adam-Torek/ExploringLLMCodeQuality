"""
Write a function to find the maximum sum of increasing subsequence from prefix until ith index and also including a given kth element which is after i, i.e., k > i .
assert max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 4, 6) == 11
"""
def max_sum_increasing_subseq(arr, k, i, memo={}):
    if i == len(arr) or k > len(arr):
        return 0

    if (i, k) in memo:
        return memo[(i, k)]

    if k > i:
        max_sum_k = max_sum_increasing_subseq(arr, k, i + 1, memo)
        max_sum_i = max(arr[i], max_sum_increasing_subseq(arr, k, i + 1, memo))
        memo[(i, k)] = max_sum_i + max_sum_k
        return memo[(i, k)]

    max_sum_i = arr[i]
    max_sum_j = max_sum_increasing_subseq(arr, k, i + 1, memo)
    memo[(i, k)] = max(max_sum_i, max_sum_j)
    if k <= i + 1:
        memo[(i, k)] = max(memo[(i, k)], arr[k] + memo[(i, k - 1)])

    return memo[(i, k)]

arr = [1, 101, 2, 3, 100, 4, 5]
k = 7
i = 4
print(max_sum_increasing_subseq(arr, k, i))