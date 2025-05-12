"""
Write a function to divide two lists element wise.
assert div_list([4,5,6],[1, 2, 3])==[4.0,2.5,2.0]
"""

def div_list(list1,list2):
    return [float(list1[i])/list2[i] for i in range(len(list1))]

print(div_list([4,5,6],[1, 2, 3]))
/python_practice/python_practice_1/python_practice_1_1.py
"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

assert longestCommonPrefix(["flower","flow","flight"])=="fl"
assert longestCommonPrefix(["dog","racecar","car"])==""
"""

def longestCommonPrefix(strs):
    if len(strs) == 0:
        return ""
    if len(strs) == 1:
        return strs[0]
    prefix = strs[0]
    for i in range(1,len(strs)):
        while strs[i].find(prefix)!= 0:
            prefix = prefix[:-1]
            if len(prefix) == 0:
                return ""
    return prefix

print(longestCommonPrefix(["flower","flow","flight"]))
print(longestCommonPrefix(["dog","racecar","car"]))
/python_practice/python_practice_1/python_practice_1_2.py
"""
Given a string, find the length of the longest substring without repeating characters.

assert lengthOfLongestSubstring("abcabcbb") == 3
assert lengthOfLongestSubstring("bbbbb") == 1
assert lengthOfLongestSubstring("pwwkew") == 3
assert lengthOfLongestSubstring("aab") == 2
assert lengthOfLongestSubstring("dvdf") == 3
"""

def lengthOfLongestSubstring(s):
    if len(s) == 0:
        return 0
    if len(s) == 1:
        return 1
    max_length = 1
    for i in range(len(s)):
        for j in range(i+1,len(s)):
            if s[j] not in s[i:j]:
                max_length = max(max_length,j-i)
            else:
                break
    return max_length

print(lengthOfLongestSubstring("abcabcbb"))
print(lengthOfLongestSubstring("bbbbb"))
print(lengthOfLongestSubstring("pwwkew"))
print(lengthOfLongestSubstring("aab"))
print(lengthOfLongestSubstring("dvdf"))
/python_practice/python_practice_1/python_practice_1_3.py
"""
Given a string, find the length of the longest substring without repeating characters.

assert lengthOfLongestSubstring("abcabcbb") == 3
assert lengthOfLongestSubstring("bbbbb") == 1
assert lengthOfLongestSubstring("pwwkew") == 3
assert lengthOfLongestSubstring("aab") == 2
assert lengthOfLongestSubstring("dvdf") == 3
"""

def lengthOfLongestSubstring(s):
    if len(s) == 0:
        return 0
    if len(s) == 1:
        return 1
    max_length = 1
    for i in range(len(s)):
        for j in range(i+1,len(s)):
            if s[j] not in s[i:j]:
                max_length = max(max_length,j-i)
            else:
                break
    return max_length

print(lengthOfLongestSubstring("abcabcbb"))
print(lengthOfLongestSubstring("bbbbb"))
print(lengthOfLongestSubstring("pwwkew"))
print(lengthOfLongestSubstring("aab"))
print(lengthOfLongestSubstring("dvdf"))
/python_practice/python_practice_1/python_practice_1_4.py
"""
Given a string, find the length of the longest substring without repeating characters.

assert lengthOfLongestSubstring("abcabcbb") == 3
assert lengthOfLongestSubstring("bbbbb") == 1
assert lengthOfLongestSubstring("pwwkew") == 3
assert lengthOfLongestSubstring("aab") == 2
assert lengthOfLongestSubstring("dvdf") == 3
"""

def lengthOfLongestSubstring(s