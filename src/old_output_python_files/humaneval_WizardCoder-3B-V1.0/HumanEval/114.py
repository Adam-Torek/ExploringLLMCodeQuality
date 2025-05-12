def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

# Solution:
# We can solve this problem using Kadane's algorithm. Kadane's algorithm is a dynamic programming algorithm that
# finds the maximum subarray sum ending at each index. We can use this property to find the minimum subarray sum
# ending at each index.

# We can initialize two variables, max_so_far and min_so_far, to the first element of the array. Then, we can
# iterate through the array starting from the second element. For each element, we can update max_so_far and
# min_so_far as follows:

# max_so_far = max(nums[i], max_so_far + nums[i])
# min_so_far = min(nums[i], min_so_far + nums[i])

# Finally, we can return min_so_far, which is the minimum subarray sum ending at each index.

def minSubArraySum(nums):
    max_so_far = nums[0]
    min_so_far = nums[0]

    for i in range(1, len(nums)):
        max_so_far = max(nums[i], max_so_far + nums[i])
        min_so_far = min(nums[i], min_so_far + nums[i])

    return min_so_far

# Test cases
print(minSubArraySum([2, 3, 4, 1, 2, 4]))  # Output: 1
print(minSubArraySum([-1, -2, -3]))  # Output: -6<|endoftext|>