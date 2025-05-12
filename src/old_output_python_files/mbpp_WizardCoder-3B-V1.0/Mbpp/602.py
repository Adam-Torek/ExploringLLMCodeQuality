"""
Write a python function to find the first repeated character in a given string.
assert first_repeated_char("abcabc") == "a"
"""

def first_repeated_char(string):
    char_count = {}
    for char in string:
        if char in char_count:
            return char
        char_count[char] = True
    return None

# Test cases
assert first_repeated_char("abcabc") == "a"
assert first_repeated_char("hello") == None
assert first_repeated_char("abbccc") == "b"<|endoftext|>