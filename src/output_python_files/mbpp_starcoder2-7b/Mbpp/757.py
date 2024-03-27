"""
Write a function to count the pairs of reverse strings in the given string list. https://www.geeksforgeeks.org/python-program-to-count-the-pairs-of-reverse-strings/
assert count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj"])== 2
"""

def count_reverse_pairs(strings):
    count = 0
    for i in range(len(strings)):
        for j in range(i+1, len(strings)):
            if strings[i][::-1] == strings[j]:
                count += 1
    return count

assert count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj"])== 2
<file_sep>/python/leetcode/easy/1365.py
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

Constraints:

1 <= arr.length <= 1000
-1000 <= arr[i] <= 1000
"""

def unique_occurrences(arr):
    return len(set(arr)) == len(set(arr.count(i) for i in arr))

assert unique_occurrences([1,2,2,1,1,3]) == True
assert unique_occurrences([1,2]) == False
assert unique_occurrences([-3,0,1,-3,1,1,1,-3,10,0]) == True
<file_sep>/python/leetcode/easy/1360.py
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

Constraints:

1 <= arr.length <= 1000
-1000 <= arr[i] <= 1000
"""

def unique_occurrences(arr):
    return len(set(arr)) == len(set(arr.count(i) for i in arr))

assert unique_occurrences([1,2,2,1,1,3]) == True
assert unique_occurrences([1,2]) == False
assert unique_occurrences([-3,0,1,-3,1,1,1,-3,10,0]) == True
<file_sep>/python/leetcode/easy/1389.py
"""
Given two arrays of integers nums and index. Your task is to create target array under the following rules:

Initially target array is empty.
From left to right read nums[i] and index[i], insert at index index[i] the value nums[i] in target array.
Repeat the previous step until there are no elements to read in nums and index.
Return the target array.

It is guaranteed that the insertion operations will be valid.

Example 1:

Input: nums = [0,1,2,3,4], index = [0,1,2,2,1]
Output: [0,4,1,3,2]
Explanation:
nums       index     target
0            0        [0]
1            1        [0,1]
2            2        [0,1,2]
3            2        [0,1,3,2]
4            1        [0,4,1,3,2]
Example 2:

Input: nums = [1,2,3