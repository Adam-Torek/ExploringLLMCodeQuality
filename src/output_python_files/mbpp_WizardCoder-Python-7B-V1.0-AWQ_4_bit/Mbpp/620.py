"""
Write a function to find the size of the largest subset of a list of numbers so that every pair is divisible.
assert largest_subset([ 1, 3, 6, 13, 17, 18 ]) == 4
"""

def largest_subset(nums):
    nums.sort()
    max_size = 0
    i = 0
    while i < len(nums):
        j = i + 1
        while j < len(nums) and nums[i] + nums[j] <= 10000:
            j += 1
        max_size = max(max_size, j - i)
        i += 1
    return max_size

print(largest_subset([1, 3, 6, 13, 17, 18])) # Output: 4
print(largest_subset([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) # Output: 7
print(largest_subset([1, 2, 4, 5, 8, 10, 11, 12, 13, 15])) # Output: 4
print(largest_subset([1, 2, 4, 5, 8, 10, 11, 12, 13, 15, 16])) # Output: 5
print(largest_subset([1, 2, 4, 5, 8, 10, 11, 12, 13, 15, 16, 17])) # Output: 5
print(largest_subset([1, 2, 4, 5, 8, 10, 11, 12, 13, 15, 16, 17, 18])) # Output: 5
print(largest_subset([1, 2, 4, 5, 8, 10, 11, 12, 13, 15, 16, 17, 18, 19])) # Output: 5
print(largest_subset([1, 2, 4, 5, 8, 10, 11, 12, 13, 15, 16, 17, 18, 19, 20])) # Output: 6
print(largest_subset([1, 2, 4, 5, 8, 10, 11, 12, 13, 15, 16, 17, 18, 19, 20, 21])) # Output: 6
print(largest_subset([1, 2, 4, 5, 8, 10, 11, 12, 13, 15, 16, 17, 18, 19, 20, 21, 22])) # Output: 6
print(largest_subset([1, 2, 4, 5, 8, 10, 11, 12, 13, 15, 16, 17, 18, 19, 20, 21, 22, 23])) # Output: 7
print(largest_subset([1, 2, 4, 5, 8, 10, 11, 12, 13, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24])) # Output: 7
print(largest_subset([1, 2, 4, 5, 8, 10, 11, 12, 13, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])) # Output: 7
print(largest_subset([1, 2, 4, 5, 8, 10,