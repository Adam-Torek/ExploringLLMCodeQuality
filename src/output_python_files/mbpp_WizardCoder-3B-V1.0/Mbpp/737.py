"""
Write a function to check whether the given string is starting with a vowel or not using regex.
assert check_str("annie")
"""
import re

def check_str(s):
    pattern = r'^[aeiouAEIOU]'
    return bool(re.match(pattern, s))

# Test cases
print(check_str("annie")) # True
print(check_str("hello")) # False
print(check_str("123")) # False<|endoftext|>