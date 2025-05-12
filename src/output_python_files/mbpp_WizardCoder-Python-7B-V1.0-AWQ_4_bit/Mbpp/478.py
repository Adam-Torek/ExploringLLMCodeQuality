"""
Write a function to remove lowercase substrings from a given string.
assert remove_lowercase("PYTHon")==('PYTH')
"""
def remove_lowercase(string):
    return ''.join(filter(str.isupper, string))

print(remove_lowercase("PYTHon")) # Output: PYTH

# Another way to solve this problem is to use regular expressions
import re
def remove_lowercase(string):
    return re.sub(r'[a-z]+', '', string)

print(remove_lowercase("PYTHon")) # Output: PYTH