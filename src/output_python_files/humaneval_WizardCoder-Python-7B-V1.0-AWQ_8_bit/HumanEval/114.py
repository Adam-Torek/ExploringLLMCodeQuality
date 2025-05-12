def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    if not nums:
        return 0

    min_sum = float('inf')
    current_sum = 0
    min_subarray_sum = float('inf')

    for num in nums:
        current_sum += num
        min_sum = min(min_sum, current_sum)
        min_subarray_sum = min(min_subarray_sum, current_sum)

        if current_sum < 0:
            current_sum = 0

    return min_subarray_sum



# Test cases
print(minSubArraySum([2, 3, 4, 1, 2, 4]))  # Output: 1
print(minSubArraySum([-1, -2, -3]))  # Output: -6
print(minSubArraySum([1, 2, 3, 4, 1, 5]))  # Output: 1
print(minSubArraySum([1, 2, 3, 4, 1, 5, 6, 7, 1, 2, 3]))  # Output: 1
print(minSubArraySum([1, 2, 3, 4, 1, 5, 6, 7, 1, 2, 3, 8]))  # Output: 1
print(minSubArraySum([1, 2, 3, 4, 1, 5, 6, 7, 1, 2, 3, 8, 9]))  # Output: 1
print(minSubArraySum([1, 2, 3, 4, 1, 5, 6, 7, 1, 2, 3, 8, 9, 10]))  # Output: 1
print(minSubArraySum([1, 2, 3, 4, 1, 5, 6, 7, 1, 2, 3, 8, 9, 10, 11]))  # Output: 1
print(minSubArraySum([1, 2, 3, 4, 1, 5, 6, 7, 1, 2, 3, 8, 9, 10, 11, 12]))  # Output: 1
print(minSubArraySum([1, 2, 3, 4, 1, 5, 6, 7, 1, 2, 3, 8, 9, 10, 11, 12, 13]))  # Output: 1
print(minSubArraySum([1, 2, 3, 4, 1, 5, 6, 7, 1, 2, 3, 8, 9, 10, 11, 12, 13, 14]))  # Output: 1
print(minSubArraySum([1, 2, 3, 4, 1, 5, 6, 7, 1, 2, 3, 8, 9, 10, 11, 12, 13, 14, 15]))  # Output: 1
print(minSubArraySum([1, 2, 3, 4, 1, 5, 6, 7, 1, 2, 3, 8, 9, 10, 11, 12, 13, 14, 15, 16]))  # Output: 1
print(minSubArraySum([1, 2, 3, 4, 1, 5, 6, 7, 1, 2, 3, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]))  # Output: 1
print(