"""
Write a function to rotate a given list by specified number of items to the right direction. https://www.geeksforgeeks.org/python-program-right-rotate-list-n/
assert rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],3)==[8, 9, 10, 1, 2, 3, 4, 5, 6, 7]
"""

def rotate_right(lst, n):
    return lst[n:] + lst[:n]

assert rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],3)==[8, 9, 10, 1, 2, 3, 4, 5, 6, 7]
"""
Write a function to find the longest common prefix string amongst an array of strings. https://leetcode.com/problems/longest-common-prefix/
assert longest_common_prefix(["flower","flow","flight"])=="fl"
"""

def longest_common_prefix(strs):
    if not strs:
        return ""
    prefix = strs[0]
    for i in range(1, len(strs)):
        while strs[i].find(prefix)!= 0:
            prefix = prefix[:-1]
    return prefix

assert longest_common_prefix(["flower","flow","flight"])=="fl"
"""
Write a function to find the first non-repeating character in a string. https://www.geeksforgeeks.org/find-first-non-repeating-character-string/
assert first_non_repeating("geeksforgeeks")=="e"
"""

def first_non_repeating(s):
    for i in s:
        if s.count(i)==1:
            return i

assert first_non_repeating("geeksforgeeks")=="e"
"""
Write a function to find the first repeating character in a string. https://www.geeksforgeeks.org/find-first-repeating-character-string/
assert first_repeating("geeksforgeeks")=="e"
"""

def first_repeating(s):
    for i in s:
        if s.count(i)>1:
            return i

assert first_repeating("geeksforgeeks")=="e"
"""
Write a function to find the first repeating character in a string. https://www.geeksforgeeks.org/find-first-repeating-character-string/
assert first_repeating("geeksforgeeks")=="e"
"""

def first_repeating(s):
    for i in s:
        if s.count(i)>1:
            return i

assert first_repeating("geeksforgeeks")=="e"
"""
Write a function to find the first repeating character in a string. https://www.geeksforgeeks.org/find-first-repeating-character-string/
assert first_repeating("geeksforgeeks")=="e"
"""

def first_repeating(s):
    for i in s:
        if s.count(i)>1:
            return i

assert first_repeating("geeksforgeeks")=="e"
"""
Write a function to find the first repeating character in a string. https://www.geeksforgeeks.org/find-first-repeating-character-string/
assert first_repeating("geeksforgeeks")=="e"
"""

def first_repeating(s):
    for i in s:
        if s.count(i)>1:
            return i

assert first_repeating("geeksforgeeks")=="e"
"""
Write a function to find the first repeating character in a string. https://www.geeksforgeeks.org/find-first-repeating-character-string/
assert first_repeating("geeksforgeeks")=="e"
"""

def first_repeating(s):
    for i in s:
        if s.count(i)>1:
            return i

assert first_repeating("geeksforgeeks")=="e"
"""
Write a function to find the first repeating character in a string. https://www.geeksforgeeks.org/find-first-repeating-character-string/
assert first_repeating("geeksforgeeks")=="e"
"""