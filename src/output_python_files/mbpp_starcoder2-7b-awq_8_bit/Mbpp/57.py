"""
Write a python function to find the largest number that can be formed with the given list of digits.
assert find_Max_Num([1,2,3]) == 321
"""

def find_Max_Num(digits):
    return int(''.join(sorted(digits, reverse=True)))

print(find_Max_Num([1,2,3]))
/python/leetcode/easy/136_single_number.py
"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4
"""

def single_number(nums):
    return 2 * sum(set(nums)) - sum(nums)

print(single_number([2,2,1]))
print(single_number([4,1,2,1,2]))
/python/leetcode/easy/1089_duplicate_zeros.py
"""
Given a fixed length array arr of integers, duplicate each occurrence of zero, shifting the remaining elements to the right.

Note that elements beyond the length of the original array are not written.

Do the above modifications to the input array in place, do not return anything from your function.

Example 1:

Input: [1,0,2,3,0,4,5,0]
Output: null
Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]
Example 2:

Input: [1,2,3,0,4,5,0,0]
Output: null
Explanation: After calling your function, the input array is modified to: [1,2,3,0,0,4,5,0]
Example 3:

Input: [1,2,3,0,4,5,0,0,0]
Output: null
Explanation: After calling your function, the input array is modified to: [1,2,3,0,0,0,4,5,0]
Example 4:

Input: [0,0,0]
Output: null
Explanation: After calling your function, the input array is modified to: [0,0,0]
Example 5:

Input: [0]
Output: null
Explanation: After calling your function, the input array is modified to: [0]

Note:

1 <= arr.length <= 10000
0 <= arr[i] <= 9
"""

def duplicate_zeros(arr):
    for i in range(len(arr)):
        if arr[i] == 0:
            arr.insert(i, 0)
            arr.pop()

print(duplicate_zeros([1,0,2,3,0,4,5,0]))
print(duplicate_zeros([1,2,3,0,4,5,0,0]))
print(duplicate_zeros([1,2,3,0,4,5,0,0,0]))
print(duplicate_zeros([0,0,0]))
print(duplicate_zeros([0]))
/python/leetcode/easy/1221_split_a_string_in_balanced_strings.py
"""
Balanced strings are those who have equal quantity of 'L' and 'R' characters.

Given a balanced string s split it in the maximum amount of balanced strings.

Return the maximum amount of splitted balanced strings.

Example 1:

Input: s = "RLRRLLRLRL"
Output: 4
Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.
Example 2:

Input: s = "RLLLLRRRLR"
Output: 3
Explanation: s can be split into "RL", "LLLRRR", "LR", each substring contains same number of 'L' and 'R'.
Example 3:

Input: s = "LLLLRRRR"
Output: 1
Explanation: s can be split into "LLLLRRRR".
Example 4:

Input: s = "RLRRRLL