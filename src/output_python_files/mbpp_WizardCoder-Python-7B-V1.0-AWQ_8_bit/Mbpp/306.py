"""
Write a function to find the maximum sum of increasing subsequence from prefix until ith index and also including a given kth element which is after i, i.e., k > i .
assert max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 4, 6) == 11
"""

def max_sum_increasing_subseq(arr, i, k, x):
    n = len(arr)
    dp = [0] * n
    dp[0] = arr[0]
    for j in range(1, n):
        dp[j] = max(dp[j-1], arr[j])
    max_sum = dp[0]
    for j in range(1, n):
        if j < i:
            continue
        if j == i:
            dp[j] = arr[j]
        else:
            dp[j] = max(dp[j-1], arr[j] + dp[j-i])
        if j == k:
            max_sum = max(max_sum, dp[j])
    return max_sum

# Test case
assert max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 4, 6) == 11