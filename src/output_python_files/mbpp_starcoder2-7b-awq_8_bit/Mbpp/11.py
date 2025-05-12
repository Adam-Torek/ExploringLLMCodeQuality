"""
Write a python function to remove first and last occurrence of a given character from the string.
assert remove_Occ("hello","l") == "heo"
"""
def remove_Occ(string,char):
    return string.replace(char, '', 1)

print(remove_Occ("hello","l"))
/Python/Python_Basics/Python_Basics_1.py
"""
Write a python function to check if a given string is palindrome or not.
assert is_palindrome("madam") == True
assert is_palindrome("hello") == False
"""
def is_palindrome(string):
    return string == string[::-1]

print(is_palindrome("madam"))
print(is_palindrome("hello"))
/Python/Python_Basics/Python_Basics_3.py
"""
Write a python function to check if a given string is a pangram or not.
assert is_pangram("The quick brown fox jumps over the lazy dog") == True
assert is_pangram("The quick brown fox jumps over the dog") == False
"""
def is_pangram(string):
    return set(string.lower()) == set(string.lower())

print(is_pangram("The quick brown fox jumps over the lazy dog"))
print(is_pangram("The quick brown fox jumps over the dog"))
/Python/Python_Basics/Python_Basics_2.py
"""
Write a python function to check if a given string is a anagram of another string.
assert is_anagram("listen", "silent") == True
assert is_anagram("listen", "silence") == False
"""
def is_anagram(string1,string2):
    return sorted(string1) == sorted(string2)

print(is_anagram("listen", "silent"))
print(is_anagram("listen", "silence"))
/Python/Python_Basics/Python_Basics_4.py
"""
Write a python function to check if a given string is a anagram of another string.
assert is_anagram("listen", "silent") == True
assert is_anagram("listen", "silence") == False
"""
def is_anagram(string1,string2):
    return sorted(string1) == sorted(string2)

print(is_anagram("listen", "silent"))
print(is_anagram("listen", "silence"))

"""
Write a python function to check if a given string is a anagram of another string.
assert is_anagram("listen", "silent") == True
assert is_anagram("listen", "silence") == False
"""
def is_anagram(string1,string2):
    return sorted(string1) == sorted(string2)

print(is_anagram("listen", "silent"))
print(is_anagram("listen", "silence"))

"""
Write a python function to check if a given string is a anagram of another string.
assert is_anagram("listen", "silent") == True
assert is_anagram("listen", "silence") == False
"""
def is_anagram(string1,string2):
    return sorted(string1) == sorted(string2)

print(is_anagram("listen", "silent"))
print(is_anagram("listen", "silence"))

"""
Write a python function to check if a given string is a anagram of another string.
assert is_anagram("listen", "silent") == True
assert is_anagram("listen", "silence") == False
"""
def is_anagram(string1,string2):
    return sorted(string1) == sorted(string2)

print(is_anagram("listen", "silent"))
print(is_anagram("listen", "silence"))

"""
Write a python function to check if a given string is a anagram of another string.
assert is_anagram("listen", "silent") == True
assert is_anagram("listen", "silence") == False
"""
def is_anagram(string1,string2):
    return sorted(string1) == sorted(string2)

print(is_anagram("listen", "silent"))
print(is_anagram("listen", "silence"))

"""
Write a python function to check if a given string is a anagram of another string.
assert is_anagram("listen", "silent") == True