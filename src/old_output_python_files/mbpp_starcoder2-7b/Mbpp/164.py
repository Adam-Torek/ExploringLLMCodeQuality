"""
Write a function to determine if the sum of the divisors of two integers are the same.
assert are_equivalent(36, 57) == False
"""

def are_equivalent(a, b):
    sum_a = 0
    sum_b = 0
    for i in range(1, a):
        if a % i == 0:
            sum_a += i
    for i in range(1, b):
        if b % i == 0:
            sum_b += i
    return sum_a == sum_b

print(are_equivalent(36, 57))
<file_sep>/python/leetcode/easy/1365.py
"""
Given an array of integers arr, return the number of unique integers
where their difference is at most 6.

Example 1:
Input: arr = [1,2,3]
Output: 2
Explanation: 1 and 2 are counted cause difference between them is 1.

Example 2:
Input: arr = [1,2,3,4]
Output: 3
Explanation: 1, 2 and 3 are counted cause difference between them is at most 6.

Example 3:
Input: arr = [1,5,9]
Output: 1
Explanation: 5 is counted cause difference between 1 and 5 is 4.

Example 4:
Input: arr = [1,2,3,4,5]
Output: 2

Example 5:
Input: arr = [1,3,2,2,3,4]
Output: 3

Constraints:
1 <= arr.length <= 10^4
0 <= arr[i] <= 10^6
"""

def count_different_numbers(arr):
    count = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if abs(arr[i] - arr[j]) <= 6:
                count += 1
    return count

print(count_different_numbers([1,2,3,4,5]))
<file_sep>/python/leetcode/easy/1431.py
"""
Given a binary array nums, return the number of subarrays with an even sum.

A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:
Input: nums = [1,4,5,2]
Output: 1
Explanation: The only subarray with an even sum is [2].

Example 2:
Input: nums = [2,4,6]
Output: 0
Explanation: There are no subarrays of size 2 with an even sum.

Example 3:
Input: nums = [2,2,2]
Output: 9

Constraints:
1 <= nums.length <= 10^5
nums[i] is either 0 or 1.
"""

def num_subarrays_with_even_sum(nums):
    count = 0
    for i in range(len(nums)):
        if nums[i] == 0:
            continue
        count += 1
        for j in range(i+1, len(nums)):
            if nums[j] == 0:
                continue
            count += 1
    return count

print(num_subarrays_with_even_sum([1,4,5,2]))
<file_sep>/python/leetcode/easy/1480.py
"""
Given an array of integers nums.
A pair (i,j) is called good if nums[i] == nums[j] and i < j.
Return the number of good pairs.

Example 1:
Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.

Example 2:
Input: nums = [1,1,1,1]
Output: 6
Explanation: Each pair in the array are good.

Example 3:
Input: nums = [1,2,3]
Output: 0

Constraints:
1 <= nums.length <= 100
1 <= nums[i] <= 100
"""

def num_of_good_pairs(nums):
    count = 0
    for i in range(len(nums)):
        for j in range(i+1