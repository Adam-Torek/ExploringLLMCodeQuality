"""
Write a python function to find a pair with highest product from a given array of integers.
assert max_Product([1,2,3,4,7,0,8,4]) == (7,8)
"""

def max_Product(arr):
    max_product = 0
    max_product_pair = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] * arr[j] > max_product:
                max_product = arr[i] * arr[j]
                max_product_pair = [arr[i], arr[j]]
    return max_product_pair

print(max_Product([1,2,3,4,7,0,8,4]))
/python/leetcode/easy/14_longest_common_prefix.py
"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
"""

def longestCommonPrefix(strs):
    if not strs:
        return ""
    prefix = strs[0]
    for i in range(1, len(strs)):
        while strs[i].find(prefix)!= 0:
            prefix = prefix[:-1]
    return prefix

print(longestCommonPrefix(["flower","flow","flight"]))
/python/leetcode/easy/13_roman_to_integer.py
"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.

Example 1:

Input: "III"
Output: 3
Example 2:

Input: "IV"
Output: 4
Example 3:

Input: "IX"
Output: 9
Example 4:

Input: "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 5:

Input: "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
"""

def romanToInt(s):
    roman_dict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    total = 0
    for i in range(len(s)):
        if i < len(s) - 1 and roman