"""
Write a function to check whether the given string starts and ends with the same character or not.
assert check_char("abba") == "Valid"
"""

def check_char(string):
    if string[0] == string[-1]:
        return "Valid"
    else:
        return "Invalid"

# Test the function
assert check_char("abba") == "Valid"
assert check_char("hello") == "Invalid"