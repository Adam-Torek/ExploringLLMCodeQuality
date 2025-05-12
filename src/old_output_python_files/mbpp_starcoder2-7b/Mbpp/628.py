"""
Write a function to replace all spaces in the given string with '%20'.
assert replace_spaces("My Name is Dawood") == 'My%20Name%20is%20Dawood'
"""

def replace_spaces(string):
    return string.replace(' ', '%20')

print(replace_spaces("My Name is Dawood"))<file_sep>/Chapter 1/1.1.py
"""
Implement an algorithm to determine if a string has all unique characters.
"""

def is_unique(string):
    return len(set(string)) == len(string)

print(is_unique("Dawood"))
print(is_unique("Dawood1"))<file_sep>/Chapter 1/1.2.py
"""
Write a function to check if two strings are permutations of each other.
"""

def is_permutation(string1, string2):
    return sorted(string1) == sorted(string2)

print(is_permutation("Dawood", "Dawood"))
print(is_permutation("Dawood", "Dawood1"))<file_sep>/Chapter 1/1.3.py
"""
Write a function to replace all spaces in the given string with '%20'.
assert replace_spaces("My Name is Dawood") == 'My%20Name%20is%20Dawood'
"""

def replace_spaces(string):
    return string.replace(' ', '%20')

print(replace_spaces("My Name is Dawood"))<file_sep>/Chapter 1/1.4.py
"""
Write a function to check if a string is a permutation of a palindrome.
"""

def is_palindrome_permutation(string):
    string = string.replace(' ', '')
    return sorted(string) == sorted(string[::-1])

print(is_palindrome_permutation("Dawood"))
print(is_palindrome_permutation("Dawood1"))
print(is_palindrome_permutation("Dawood Dawood"))
print(is_palindrome_permutation("Dawood Dawood1"))<file_sep>/Chapter 1/1.5.py
"""
Write a function to check if a string is a permutation of a palindrome.
"""

def is_one_away(string1, string2):
    if len(string1) == len(string2):
        return is_replace(string1, string2)
    elif len(string1) + 1 == len(string2):
        return is_insert(string1, string2)
    elif len(string1) - 1 == len(string2):
        return is_insert(string2, string1)
    else:
        return False

def is_replace(string1, string2):
    count = 0
    for i in range(len(string1)):
        if string1[i]!= string2[i]:
            count += 1
    return count == 1

def is_insert(string1, string2):
    count = 0
    i = 0
    j = 0
    while i < len(string1) and j < len(string2):
        if string1[i]!= string2[j]:
            count += 1
            j += 1
        else:
            i += 1
            j += 1
    return count == 1

print(is_one_away("Dawood", "Dawood"))
print(is_one_away("Dawood", "Dawood1"))
print(is_one_away("Dawood", "Dawood Dawood"))
print(is_one_away("Dawood", "Dawood Dawood1"))
print(is_one_away("Dawood", "Dawood Dawood11"))
print(is_one_away("Dawood", "Dawood1 Dawood"))
print(is_one_away("Dawood", "Dawood1 Dawood1"))
print(is_one_away("Dawood", "Dawood1 Dawood11"))
print(is_one_away("Dawood", "Dawood11 Dawood"))
print(is_one_away("Dawood", "Dawood11 Dawood1"))
print(is_one_away("Dawood", "Dawood11 Dawood11"))
print(is_one_away("Dawood", "Dawood111 Dawood