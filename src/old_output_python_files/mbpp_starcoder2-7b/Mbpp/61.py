"""
Write a python function to count the number of substrings with the sum of digits equal to their length.
assert count_Substrings('112112') == 6
"""

def count_Substrings(s):
    count = 0
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            if sum(map(int, s[i:j])) == len(s[i:j]):
                count += 1
    return count

print(count_Substrings('112112'))
<file_sep>/python/leetcode/easy/1365.py
"""
Given an array of integers nums, return an array answer such that answer[i] is equal to the number of
integers in nums that are less than or equal to i.

The range of the integer i is [0, nums.length - 1].

Example 1:

Input: nums = [8,1,2,2,3]
Output: [4,0,1,1,3]
Explanation:
For i=0, nums[i]=8 was inserted at most a total of 4 times
For i=1, nums[i]=1 was inserted at most a total of 0 times
For i=2, nums[i]=2 was inserted at most a total of 1 times
For i=3, nums[i]=2 was inserted at most a total of 1 times
For i=4, nums[i]=3 was inserted at most a total of 3 times

Example 2:

Input: nums = [6,5,4,8]
Output: [2,1,0,3]

Example 3:

Input: nums = [7,7,7,7]
Output: [4,4,4,4]

Constraints:

1 <= nums.length <= 500
0 <= nums[i] <= 100
"""

from collections import Counter

def smallerNumbersThanCurrent(nums):
    """
    Time complexity: O(n)
    Space complexity: O(n)
    """
    count = Counter(nums)
    return [sum(count[i]) for i in range(101)]

print(smallerNumbersThanCurrent([8,1,2,2,3]))
print(smallerNumbersThanCurrent([6,5,4,8]))
print(smallerNumbersThanCurrent([7,7,7,7]))
<file_sep>/python/leetcode/easy/1431.py
"""
Given the array candies and the integer extraCandies, where candies[i] represents the number of candies that the ith kid has.

For each kid check if there is a way to distribute extraCandies among the kids such that he or she can have the greatest number of candies among them. Notice that multiple kids can have the greatest number of candies.

Example 1:

Input: candies = [2,3,5,1,3], extraCandies = 3
Output: [true,true,true,false,true]
Explanation:
Kid 1 has 2 candies and if he or she receives all extra candies (3) will have 5 candies --- the greatest number of candies among the kids.
Kid 2 has 3 candies and if he or she receives at least 2 extra candies will have the greatest number of candies among the kids.
Kid 3 has 5 candies and this is already the greatest number of candies among the kids.
Kid 4 has 1 candy and even if he or she receives all extra candies will only have 4 candies.
Kid 5 has 3 candies and if he or she receives at least 2 extra candies will have the greatest number of candies among the kids.

Example 2:

Input: candies = [4,2,1,1,2], extraCandies = 1
Output: [true,false,false,false,false]
Explanation: There is only 1 extra candy, therefore only kid 1 will have the greatest number of candies among the kids regardless of who takes the extra candy.

Example 3:

Input: candies = [12,1,12], extraCandies = 10
Output: [true,false,true]

Constraints:

2