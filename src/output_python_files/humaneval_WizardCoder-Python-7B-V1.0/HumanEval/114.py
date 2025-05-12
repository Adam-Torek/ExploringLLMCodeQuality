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
    min_sum = float('inf')
    for num in nums:
        current_sum += num
        min_sum = min(min_sum, current_sum)
        if current_sum < 0:
            current_sum = 0
    return min_sum


# Test cases
print(minSubArraySum([2, 3, 4, 1, 2, 4])) # 1
print(minSubArraySum([-1, -2, -3])) # -6
print(minSubArraySum([0, 1, 0, 1, 1])) # 0
print(minSubArraySum([1, 2, 3, 4, 1, 4, 1, 3, 2, 1, 2, 3])) # 1
print(minSubArraySum([1, 2, 3, 4, 5])) # 1
print(minSubArraySum([1])) # 1
print(minSubArraySum([])) # 0
print(minSubArraySum([-1])) # -1
print(minSubArraySum([-1, -2, -3, -4])) # -6
print(minSubArraySum([-1, 2, -3, 4, -5])) # -3
print(minSubArraySum([1, 2, 3, 4, 5, 6])) # 1
print(minSubArraySum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) # 1
print(minSubArraySum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -10])) # -10
print(minSubArraySum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -10, -11])) # -11
print(minSubArraySum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -10, -11, -12])) # -12
print(minSubArraySum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -10, -11, -12, -13])) # -13
print(minSubArraySum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -10, -11, -12