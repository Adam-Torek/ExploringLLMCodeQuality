"""
Write a python function to find the first non-repeated character in a given string.
assert first_non_repeating_character("abcabc") == None
"""

def first_non_repeating_character(string):
    """
    :param string: string
    :return: first non-repeating character
    """
    for char in string:
        if string.count(char) == 1:
            return char
    return None

print(first_non_repeating_character("abcabc"))
/python/leetcode/easy/14_longest_common_prefix.py
"""
Write a python function to find the longest common prefix string amongst an array of strings.
assert longest_common_prefix(["flower","flow","flight"]) == "fl"
"""

def longest_common_prefix(strs):
    """
    :param strs: list of strings
    :return: longest common prefix string
    """
    if len(strs) == 0:
        return ""
    if len(strs) == 1:
        return strs[0]
    prefix = strs[0]
    for i in range(1, len(strs)):
        while strs[i].find(prefix)!= 0:
            prefix = prefix[:-1]
    return prefix

print(longest_common_prefix(["flower","flow","flight"]))
/python/leetcode/easy/13_roman_to_integer.py
"""
Write a python function to convert a Roman numeral to an integer.
assert roman_to_integer("III") == 3
"""

def roman_to_integer(s):
    """
    :param s: string
    :return: integer
    """
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    for i in range(len(s)):
        if i > 0 and roman[s[i]] > roman[s[i - 1]]:
            result += roman[s[i]] - 2 * roman[s[i - 1]]
        else:
            result += roman[s[i]]
    return result

print(roman_to_integer("III"))
/python/leetcode/easy/12_reverse_integer.py
"""
Write a python function to reverse digits of an integer.
assert reverse_integer(123) == 321
"""

def reverse_integer(x):
    """
    :param x: integer
    :return: reversed integer
    """
    if x == 0:
        return 0
    if x < 0:
        return -1 * int(str(x)[::-1][:-1])
    return int(str(x)[::-1])

print(reverse_integer(123))
/python/leetcode/easy/11_two_sum.py
"""
Write a python function to find two numbers such that they add up to a specific target number.
assert two_sum([2, 7, 11, 15], 9) == [0, 1]
"""

def two_sum(nums, target):
    """
    :param nums: list of integers
    :param target: integer
    :return: list of indices of the two numbers such that they add up to target
    """
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

print(two_sum([2, 7, 11, 15], 9))
/python/leetcode/easy/10_valid_parentheses.py
"""
Write a python function to determine if a given string contains valid parentheses.
assert valid_parentheses("()") == True
"""

def valid_parentheses(s):
    """
    :param s: string
    :return: boolean
    """
    stack = []
    for char in s:
        if char == "(":
            stack.append(char)
        elif char == ")":
            if len(stack) == 0:
                return False
            stack.pop()
    return len(stack) == 0

print(valid_parentheses("()"))
/python/leetcode/easy/1_two_sum.py
"""
Write a python function to find two numbers such that they add up to a specific target number.
assert two_sum