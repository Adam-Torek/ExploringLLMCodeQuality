"""
Write a python function to find the first non-repeated character in a given string.
assert first_non_repeating_character("abcabc") == None
"""

def first_non_repeating_character(string):
    char_count = {}
    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    for char in string:
        if char_count[char] == 1:
            return char
    return None

# Test cases
print(first_non_repeating_character("abcabc")) # None
print(first_non_repeating_character("aabbcdaadd")) # c
print(first_non_repeating_character("geeksforgeeks")) # e
print(first_non_repeating_character("aabbccddeeff")) # f
print(first_non_repeating_character("aabbccddeeffg")) # g
print(first_non_repeating_character("aabbccddeeffg")) # g
print(first_non_repeating_character("aabbccddeeffgg")) # None