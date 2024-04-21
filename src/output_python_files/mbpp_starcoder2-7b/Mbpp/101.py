"""
Write a function to find the kth element in the given array using 1-based indexing.
assert kth_element([12,3,5,7,19], 2) == 3
"""

def kth_element(arr, k):
    return arr[k-1]

print(kth_element([12,3,5,7,19], 2))<file_sep>/python/leetcode/easy/1365.py
"""
Given an array of integers arr, write a function that returns true if and only if the number of occurrences of each value in the array is unique.

Example 1:

Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
Example 2:

Input: arr = [1,2]
Output: false
Example 3:

Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true
"""

def unique_occurrences(arr):
    return len(arr) == len(set(arr))

print(unique_occurrences([1,2,2,1,1,3]))
print(unique_occurrences([1,2]))
print(unique_occurrences([-3,0,1,-3,1,1,1,-3,10,0]))<file_sep>/python/leetcode/easy/1431.py
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
"""

def kids_with_candies(candies, extraCandies):
    max_candies = max(candies)
    return [True if candies[i] + extraCandies >= max_candies else False for i in range(len(candies))]

print(kids_with_candies([2,3,5,1,3], 3))
print(kids_with_candies([4,2,1,1,2], 1))
print(kids_with_candies([12,1,12], 10))<file_sep>/python/leetcode/easy/1360.py
"""
Given an array of integers arr, write a function that returns true if and only if the number of occurrences of each value in the array is unique.

Example 1:

Input: arr = [1,2,2,1,1,3]