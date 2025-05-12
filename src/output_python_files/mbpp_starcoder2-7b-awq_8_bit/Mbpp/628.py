"""
Write a function to replace all spaces in the given string with '%20'.
assert replace_spaces("My Name is Dawood") == 'My%20Name%20is%20Dawood'
"""

def replace_spaces(string):
    return string.replace(" ", "%20")

print(replace_spaces("My Name is Dawood"))
/Chapter 1/1.3.py
"""
Write a function to check if two strings are anagrams of each other.
assert is_anagram("abc", "cba") == True
assert is_anagram("abc", "def") == False
"""

def is_anagram(string1, string2):
    return sorted(string1) == sorted(string2)

print(is_anagram("abc", "cba"))
print(is_anagram("abc", "def"))
/Chapter 1/1.1.py
"""
Write a function to check if a string has all unique characters.
assert has_unique_characters("abc") == True
assert has_unique_characters("abca") == False
"""

def has_unique_characters(string):
    return len(set(string)) == len(string)

print(has_unique_characters("abc"))
print(has_unique_characters("abca"))
/Chapter 1/1.2.py
"""
Write a function to check if two strings are permutations of each other.
assert is_permutation("abc", "cba") == True
assert is_permutation("abc", "def") == False
"""

def is_permutation(string1, string2):
    return sorted(string1) == sorted(string2)

print(is_permutation("abc", "cba"))
print(is_permutation("abc", "def"))
/Chapter 1/1.4.py
"""
Write a function to replace all spaces in the given string with '%20'.
assert replace_spaces("My Name is Dawood") == 'My%20Name%20is%20Dawood'
"""

def replace_spaces(string):
    return string.replace(" ", "%20")

print(replace_spaces("My Name is Dawood"))
/Chapter 1/1.5.py
"""
Write a function to check if a string is a palindrome.
assert is_palindrome("abc") == False
assert is_palindrome("aba") == True
"""

def is_palindrome(string):
    return string == string[::-1]

print(is_palindrome("abc"))
print(is_palindrome("aba"))
/Chapter 1/1.6.py
"""
Write a function to compress a string by replacing repeated characters with the count of the repeated characters.
assert compress("aabcccccaaa") == "a2b1c5a3"
"""

def compress(string):
    compressed_string = ""
    count = 1
    for i in range(len(string)):
        if i == len(string) - 1 or string[i]!= string[i+1]:
            compressed_string += string[i] + str(count)
            count = 1
        else:
            count += 1
    return compressed_string

print(compress("aabcccccaaa"))
/Chapter 1/1.7.py
"""
Write a function to check if a matrix is a rotation of another matrix.
assert is_rotation([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[7, 4, 1], [8, 5, 2], [9, 6, 3]]) == True
assert is_rotation([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == False
"""

def is_rotation(matrix1, matrix2):
    return matrix1 == matrix2[::-1]

print(is_rotation([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[7, 4, 1], [8, 5, 2], [9, 6, 3]]))
print(is_rotation([[1, 2, 3], [4, 5, 6], [7, 8, 9