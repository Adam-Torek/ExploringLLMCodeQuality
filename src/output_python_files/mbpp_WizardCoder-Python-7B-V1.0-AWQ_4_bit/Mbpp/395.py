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
print(first_non_repeating_character("abca")) # a
print(first_non_repeating_character("geeksforgeeks")) # g
print(first_non_repeating_character("hello")) # h
print(first_non_repeating_character("aabbcc")) # None
print(first_non_repeating_character("geeksforgeeksgeeks")) # g
print(first_non_repeating_character("")) # None
print(first_non_repeating_character("a")) # a
print(first_non_repeating_character("abcdefgabcdefg")) # None
print(first_non_repeating_character("aabbcddd")) # c
print(first_non_repeating_character("aabbcddd")) # c
print(first_non_repeating_character("abcdefgf")) # f
print(first_non_repeating_character("abcdefgf")) # f
print(first_non_repeating_character("abcdefgf")) # f
print(first_non_repeating_character("abcdefgf")) # f
print(first_non_repeating_character("abcdefgf")) # f
print(first_non_repeating_character("abcdefgf")) # f
print(first_non_repeating_character("abcdefgf")) # f
print(first_non_repeating_character("abcdefgf")) # f
print(first_non_repeating_character("abcdefgf")) # f
print(first_non_repeating_character("abcdefgf")) # f
print(first_non_repeating_character("abcdefgf")) # f
print(first_non_repeating_character("abcdefgf")) # f
print(first_non_repeating_character("abcdefgf")) # f
print(first_non_repeating_character("abcdefgf")) # f
print(first_non_repeating_character("abcdefgf")) # f
print(first_non_repeating_character("abcdefgf")) # f
print(first_non_repeating_character("abcdefgf")) # f
print(first_non_repeating_character("abcdefgf")) # f
print(first_non_repeating_character("abcdefgf")) # f
print(first_non_repeating_character("abcdefgf")) # f
print(first_non_repeating_character("abcdefgf")) # f
print(first_non_repeating_character("abcdefgf")) # f
print(first_non_repeating_character("abcdefgf")) # f
print(first_non_repeating_character("abcdefgf")) # f
print(first_non_repeating_character("abcdefgf")) # f
print(first_non_repeating_character("abcdefgf")) # f
print(first_non_repeating_character("abcdefgf")) # f
print(first_non_repeating_character("abcdef