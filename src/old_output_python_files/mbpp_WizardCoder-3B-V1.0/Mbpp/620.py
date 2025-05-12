"""
Write a function to find the size of the largest subset of a list of numbers so that every pair is divisible.
assert largest_subset([ 1, 3, 6, 13, 17, 18 ]) == 4
"""

def largest_subset(nums):
    nums.sort()
    n = len(nums)
    dp = [1] * n
    max_size = 1

    for i in range(1, n):
        for j in range(i):
            if nums[i] % nums[j] == 0:
                dp[i] = max(dp[i], dp[j] + 1)
                max_size = max(max_size, dp[i])

    return max_size

# Test cases
assert largest_subset([ 1, 3, 6, 13, 17, 18 ]) == 4
assert largest_subset([ 1, 2, 3, 4, 5 ]) == 1
assert largest_subset([ 1, 2, 3, 4, 5, 6 ]) == 2
assert largest_subset([ 1, 2, 3, 4, 5, 6, 7 ]) == 3
assert largest_subset([ 1, 2, 3, 4, 5, 6, 7, 8 ]) == 4
assert largest_subset([ 1, 2, 3, 4, 5, 6, 7, 8, 9 ]) == 5
assert largest_subset([ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]) == 6<|endoftext|>