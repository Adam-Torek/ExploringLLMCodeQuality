"""
Write a function to replace all spaces in the given string with '%20'.
assert replace_spaces("My Name is Dawood") == 'My%20Name%20is%20Dawood'
"""

def replace_spaces(string):
    return string.replace(" ", "%20")

print(replace_spaces("My Name is Dawood"))
/chapter_1/1_1_is_unique.py
"""
Implement an algorithm to determine if a string has all unique characters.
"""

def is_unique(string):
    """
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    return len(set(string)) == len(string)

print(is_unique("dawood"))
print(is_unique("dawoodd"))
/chapter_1/1_3_urlify.py
"""
Write a method to replace all spaces in a string with '%20'. You may assume that the string has sufficient space at the end to hold the additional characters, and that you are given the "true" length of the string.
"""

def urlify(string, length):
    return string[:length].replace(" ", "%20")

print(urlify("", 13))
/chapter_1/1_2_check_permutation.py
"""
Given two strings, write a method to decide if one is a permutation of the other.
"""

def check_permutation(string1, string2):
    """
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    return sorted(string1) == sorted(string2)

print(check_permutation("dawood", "dawood"))
print(check_permutation("dawood", "dawoodd"))
/chapter_1/1_5_one_away.py
"""
There are three types of edits that can be performed on strings: insert a character, remove a character, or replace a character. Given two strings, write a function to check if they are one edit (or zero edits) away.
"""

def one_away(string1, string2):
    """
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    if len(string1) == len(string2):
        return one_edit_replace(string1, string2)
    elif len(string1) + 1 == len(string2):
        return one_edit_insert(string1, string2)
    elif len(string1) - 1 == len(string2):
        return one_edit_insert(string2, string1)
    return False

def one_edit_replace(string1, string2):
    found_difference = False
    for i in range(len(string1)):
        if string1[i]!= string2[i]:
            if found_difference:
                return False
            found_difference = True
    return True

def one_edit_insert(string1, string2):
    index1 = 0
    index2 = 0
    while index1 < len(string1) and index2 < len(string2):
        if string1[index1]!= string2[index2]:
            if index1!= index2:
                return False
            index2 += 1
        else:
            index1 += 1
            index2 += 1
    return True

print(one_away("pale", "ple"))
print(one_away("pales", "pale"))
print(one_away("pale", "bale"))
print(one_away("pale", "bake"))
/chapter_1/1_4_palindrome_permutation.py
"""
Given a string, write a function to check if it is a permutation of a palindrome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.
"""

def palindrome_permutation(string):
    """
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    string = string.replace(" ", "")
    string = string.lower()
    char_count = {}
    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] =