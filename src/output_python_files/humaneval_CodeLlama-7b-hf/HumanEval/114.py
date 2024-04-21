def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # Write your code here
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return min(nums[0], nums[1])
    if len(nums) == 3:
        return min(nums[0], nums[1], nums[2])
    if len(nums) == 4:
        return min(nums[0], nums[1], nums[2], nums[3])
    if len(nums) == 5:
        return min(nums[0], nums[1], nums[2], nums[3], nums[4])
    if len(nums) == 6:
        return min(nums[0], nums[1], nums[2], nums[3], nums[4], nums[5])
    if len(nums) == 7:
        return min(nums[0], nums[1], nums[2], nums[3], nums[4], nums[5], nums[6])
    if len(nums) == 8:
        return min(nums[0], nums[1], nums[2], nums[3], nums[4], nums[5], nums[6], nums[7])
    if len(nums) == 9:
        return min(nums[0], nums[1], nums[2], nums[3], nums[4], nums[5], nums[6], nums[7], nums[8])
    if len(nums) == 10:
        return min(nums[0], nums[1], nums[2], nums[3], nums[4], nums[5], nums[6], nums[7], nums[8], nums[9])
    if len(nums) == 11:
        return min(nums[0], nums[1], nums[2], nums[3], nums[4], nums[5], nums[6], nums[7], nums[8], nums[9], nums[10])
    if len(nums) == 12:
        return min(nums[0], nums[1], nums[2], nums[3], nums[4], nums[5], nums[6], nums[7], nums[8], nums[9], nums[10], nums[11])
    if len(nums) == 13:
        return min(nums[0], nums[1], nums[2], nums[3], nums[4], nums[5], nums[6], nums[7], nums[8], nums[9], nums[10], nums[11], nums[12])
    if len(nums) == 14:
        return min(nums[0], nums[1], nums[2], nums[3], nums[4], nums[5], nums[6], nums[7], nums[8], nums[9], nums[10], nums[11], nums[12], nums[13])
    if len(nums) == 15:
        return min(nums[0], nums[1], nums[2], nums[3], nums[4], nums[5], nums[6], nums[7], nums[8], nums[9], nums[10], nums[11], nums[12], nums[13], nums[14])
    if len(nums) == 16:
        return min(nums[0], nums[1], nums[2], nums[