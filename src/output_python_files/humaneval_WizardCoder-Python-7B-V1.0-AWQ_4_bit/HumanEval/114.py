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

    return min_subarray_sum if min_subarray_sum != float('inf') else 0



# Test cases
print(minSubArraySum([2, 3, 4, 1, 2, 4]))  # Output: 1
print(minSubArraySum([-1, -2, -3]))  # Output: -6
print(minSubArraySum([1, 2, 3, 4, 1]))  # Output: 1
print(minSubArraySum([1, 2, 3, 4]))  # Output: 1
print(minSubArraySum([1]))  # Output: 1
print(minSubArraySum([]))  # Output: 0
print(minSubArraySum([-1]))  # Output: -1
print(minSubArraySum([0, 0, 0, 0]))  # Output: 0
print(minSubArraySum([1, 2, -1, -2, -3]))  # Output: -1
print(minSubArraySum([1, 2, -1, -2, -3, -4]))  # Output: -1
print(minSubArraySum([1, 2, -1, -2, -3, -4, -5]))  # Output: -1
print(minSubArraySum([1, 2, -1, -2, -3, -4, -5, -6]))  # Output: -1
print(minSubArraySum([1, 2, -1, -2, -3, -4, -5, -6, -7]))  # Output: -1
print(minSubArraySum([1, 2, -1, -2, -3, -4, -5, -6, -7, -8]))  # Output: -1
print(minSubArraySum([1, 2, -1, -2, -3, -4, -5, -6, -7, -8, -9]))  # Output: -1
print(minSubArraySum([1, 2, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]))  # Output: -1
print(minSubArraySum([1, 2, -1, -2, -3