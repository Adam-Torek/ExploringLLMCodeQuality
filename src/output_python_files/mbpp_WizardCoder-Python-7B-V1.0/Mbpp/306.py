"""
Write a function to find the maximum sum of increasing subsequence from prefix until ith index and also including a given kth element which is after i, i.e., k > i .
assert max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 4, 6) == 11
"""

def max_sum_increasing_subseq(arr, i, k, x):
    n = len(arr)
    dp = [0] * n
    dp[i] = arr[i]
    for j in range(i-1, -1, -1, -1):
        for l in range(j+1, i):
            if arr[l] < arr[j]:
                dp[j] = max(dp[j], dp[l] + arr[j])
    max_sum = dp[0]
    for j in range(1, i):
        if arr[j] > x:
            max_sum = max(max_sum, dp[j])
    return max_sum

# Test cases
print(max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 4, 6)) # Output: 11
print(max_sum_increasing_subseq([1, 2, 3, 4, 5, 100, 6, 7, 8, 9, 10 ], 7, 4, 6)) # Output: 30
print(max_sum_increasing_subseq([1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ], 7, 4, 6)) # Output: 30
print(max_sum_increasing_subseq([1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ], 7, 4, 10)) # Output: 30
print(max_sum_increasing_subseq([1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ], 7, 4, 1)) # Output: 10
print(max_sum_increasing_subseq([1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ], 7, 4, 0)) # Output: 10
print(max_sum_increasing_subseq([1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ], 7, 4, 100)) # Output: 30
print(max_sum_increasing_subseq([1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ], 7, 4, 5)) # Output: 14
print(max_sum_increasing_subseq([1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ], 7, 4, 8)) # Output: 17
print(max_sum_increasing_subseq([1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ], 7, 4, 9)) # Output: 19
print(max_sum_increasing_subseq([1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ], 7, 4, 10)) # Output: 30
print(max_sum_increasing_subseq([1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ], 7, 4, 11)) # Output: 30
print(max_sum_increasing_subseq([1, 2, 3, 4, 5, 6, 7, 8