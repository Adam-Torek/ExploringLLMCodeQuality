"""
Write a function to replace all spaces in the given string with '%20'.
assert replace_spaces("My Name is Dawood") == 'My%20Name%20is%20Dawood'
"""

def replace_spaces(string):
    return string.replace(" ", "%20")

print(replace_spaces("My Name is Dawood"))/Chapter 1/1.3.py
"""
Write a method to determine if two strings are anagrams or not.
"""

def is_anagram(string1, string2):
    return sorted(string1) == sorted(string2)

print(is_anagram("dawood", "dawood"))/Chapter 1/1.1.py
"""
Write a method to determine if a string has all unique characters.
"""

def is_unique(string):
    return len(string) == len(set(string))

print(is_unique("dawood"))/Chapter 1/1.2.py
"""
Write a method to reverse a string.
"""

def reverse(string):
    return string[::-1]

print(reverse("dawood"))/Chapter 1/1.4.py
"""
Write a method to replace all spaces in the given string with '%20'.
"""

def replace_spaces(string):
    return string.replace(" ", "%20")

print(replace_spaces("My Name is Dawood"))/Chapter 1/1.5.py
"""
Write a method to determine if two strings are anagrams or not.
"""

def is_anagram(string1, string2):
    return sorted(string1) == sorted(string2)

print(is_anagram("dawood", "dawood"))/Chapter 1/1.6.py
"""
Write a method to compress a string by replacing repeated characters with the count of the repeated characters.
"""

def compress(string):
    compressed_string = ""
    count = 1
    for i in range(len(string)):
        if i == len(string) - 1:
            compressed_string += string[i] + str(count)
        elif string[i] == string[i + 1]:
            count += 1
        else:
            compressed_string += string[i] + str(count)
            count = 1
    return compressed_string

print(compress("aabcccccaaa"))/Chapter 1/1.7.py
"""
Write a method to determine if a string is a rotation of another string.
"""

def is_rotation(string1, string2):
    return string1 in string2 + string2

print(is_rotation("dawood", "dawood"))/Chapter 1/1.8.py
"""
Write a method to determine if a string is a rotation of another string.
"""

def is_rotation(string1, string2):
    return string1 in string2 + string2

print(is_rotation("dawood", "dawood"))/Chapter 1/1.9.py
"""
Write a method to determine if a string is a rotation of another string.
"""

def is_rotation(string1, string2):
    return string1 in string2 + string2

print(is_rotation("dawood", "dawood"))