"""
Write a python function to find the first non-repeated character in a given string.
assert first_non_repeating_character("abcabc") == None
"""

def first_non_repeating_character(s):
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    for char in s:
        if char_count[char] == 1:
            return char

    return None

# Test cases
assert first_non_repeating_character("abcabc") == None
assert first_non_repeating_character("abca") == "a"
assert first_non_repeating_character("aabbcc") == "b"
assert first_non_repeating_character("abcde") == "e"
assert first_non_repeating_character("abcabcabc") == "c"<|endoftext|>