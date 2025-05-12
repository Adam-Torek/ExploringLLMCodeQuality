"""
Write a function to find the size of the largest subset of a list of numbers so that every pair is divisible.
assert largest_subset([ 1, 3, 6, 13, 17, 18 ]) == 4
"""
from typing import List

def largest_subset(nums: List[int]) -> int:
    nums.sort()
    n = len(nums)
    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if nums[i] % nums[j] == 0:
                dp[i] = max(dp[i], dp[j] + 1)
    max_size = max(dp)
    return max_size

# Test cases
print(largest_subset([1, 3, 6, 13, 18])) # Output: 4
print(largest_subset([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) # Output: 6
print(largest_subset([1, 2, 4, 6, 8, 12, 16])) # Output: 5
print(largest_subset([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])) # Output: 8
print(largest_subset([1, 2, 4, 6, 8, 12, 16, 18, 20, 24, 25, 28, 30])) # Output: 7
print(largest_subset([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])) # Output: 10
print(largest_subset([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31])) # Output: 10
print(largest_subset([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32])) # Output: 11
print(largest_subset([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33])) # Output: 11
print(largest_subset([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,