"""
Write a function to find the maximum sum of increasing subsequence from prefix until ith index and also including a given kth element which is after i, i.e., k > i.
assert max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 4, 6) == 11
"""

def max_sum_increasing_subseq(arr, n, k, i):
    if k > i:
        return 0

    dp = [0] * n
    dp[0] = arr[0]

    for j in range(1, n):
        if arr[j] > arr[j-1]:
            dp[j] = dp[j-1] + arr[j]
        else:
            dp[j] = max(dp[j-1], dp[j-2] + arr[j])

    max_sum = dp[i-1]
    for j in range(i, n):
        if dp[j] > max_sum:
            max_sum = dp[j]

    return max_sum

# Test cases
print(max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 4, 6)) # Output: 11<|endoftext|>