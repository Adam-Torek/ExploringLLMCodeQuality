"""
Write a function to check whether the given string is starting with a vowel or not using regex.
assert check_str("annie")
"""

import re

def check_str(string):
    vowels = "aeiouAEIOU"
    if re.match("^[" + vowels + "]", string):
        return True
    else:
        return False

print(check_str("annie")) # True
print(check_str("apple")) # False
print(check_str("Eve")) # True
print(check_str("Orange")) # False
print(check_str("Alice")) # True
print(check_str("Zebra")) # False
print(check_str("123")) # False
print(check_str("")) # False
print(check_str(" ")) # False
print(check_str("a")) # True
print(check_str("A")) # True
print(check_str("e")) # True
print(check_str("E")) # True
print(check_str("i")) # True
print(check_str("o")) # True
print(check_str("u")) # True
print(check_str("U")) # True