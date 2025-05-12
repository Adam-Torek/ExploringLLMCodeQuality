def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # Initialize variables
    min_sum = float('inf')
    current_sum = 0
    start = 0
    end = 0

    # Iterate through the array
    while end < len(nums):
        # Add the current number to the sum
        current_sum += nums[end]

        # If the sum is greater than the minimum sum, update the start variable
        while current_sum > min_sum:
            current_sum -= nums[start]
            start += 1

        # Update the minimum sum if necessary
        min_sum = min(min_sum, current_sum)
        end += 1

    # Return the minimum sum
    return min_sum

# Test the function
print(minSubArraySum([2, 3, 4, 1, 2, 4])) # 1
print(minSubArraySum([-1, -2, -3])) # -6
print(minSubArraySum([1, 2, 3, 4, 5])) # 1
print(minSubArraySum([1, 1, 1, 1, 1])) # 1
print(minSubArraySum([1, 2, 3, 5, 6])) # 3
print(minSubArraySum([-1, -2, -3, -4, -5])) # -5
print(minSubArraySum([-1, -2, -3, -4, -5, -6])) # -11
print(minSubArraySum([-1, -2, -3, -4, -5, -6, -7])) # -12
print(minSubArraySum([-1, -2, -3, -4, -5, -6, -7, -8])) # -13
print(minSubArraySum([-1, -2, -3, -4, -5, -6, -7, -8, -9])) # -14
print(minSubArraySum([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10])) # -15
print(minSubArraySum([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11])) # -16
print(minSubArraySum([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12])) # -17
print(minSubArraySum([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13])) # -18
print(minSubArraySum([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14])) # -19
print(minSubArraySum([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15])) # -20
print(minSubArraySum([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16])) # -21
print(minSubArraySum([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17])) # -22
print(minSubArraySum([-1, -