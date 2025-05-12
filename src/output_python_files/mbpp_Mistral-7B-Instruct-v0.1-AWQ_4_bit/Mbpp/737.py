"""
Write a function to check whether the given string is starting with a vowel or not using regex.
assert check_str("annie")
"""

import re

def check_str(str):
    vowels = "aeiouAEIOU"
    if re.search(r"^[" + vowels + "]", str):
        return True
    else:
        return False

# Testing the function
assert check_str("annie")
assert check_str("hello")
assert check_str("world")