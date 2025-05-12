"""
Write a function to apply a given format string to all of the elements in a list.
assert add_string([1,2,3,4],'temp{0}')==['temp1', 'temp2', 'temp3', 'temp4']
"""

def add_string(lst,format):
    return [format.format(i) for i in lst]

print(add_string([1,2,3,4],'temp{0}'))
/python_practice/python_practice_1.py
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
    for i in range(1,len(strs)):
        while strs[i].find(prefix)!= 0:
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix

print(longestCommonPrefix(["flower","flow","flight"]))
print(longestCommonPrefix(["dog","racecar","car"]))
/python_practice/python_practice_2.py
"""
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

def lengthOfLongestSubstring(s):
    if not s:
        return 0
    max_len = 1
    cur_len = 1
    for i in range(1,len(s)):
        if s[i] not in s[i-cur_len:i]:
            cur_len += 1
        else:
            if cur_len > max_len:
                max_len = cur_len
            cur_len = i - s[i-cur_len:i].index(s[i])
    if cur_len > max_len:
        max_len = cur_len
    return max_len

print(lengthOfLongestSubstring("abcabcbb"))
print(lengthOfLongestSubstring("bbbbb"))
print(lengthOfLongestSubstring("pwwkew"))
/python_practice/python_practice_3.py
"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
"""

def longestPalindrome(s):
    if not s:
        return ""
    max_len = 1
    max_str = s[0]
    for i in range(len(s)):
        for j in range(i+1,len(s)):
            if s[i:j+1] == s[i:j+1][::-1]:
                if j-i+1 > max_len:
                    max_len = j-i+1
                    max_str = s[i:j+1]
    return max_str

print(longestPalindrome("babad"))
print(longestPalindrome("cbbd"))
/python_practice/python_practice_4.py
"""
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3: