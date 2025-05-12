"""
Write a python function to find the first repeated character in a given string.
assert first_repeated_char("abcabc") == "a"
"""

def first_repeated_char(string):
    char_dict = {}
    for char in string:
        if char in char_dict:
            return char
        else:
            char_dict[char] = 1
    return None

print(first_repeated_char("abcabc")) # Output: "a"
print(first_repeated_char("abc")) # Output: None
print(first_repeated_char("abca")) # Output: "a"
print(first_repeated_char("abcaab")) # Output: "a"
print(first_repeated_char("abcbc")) # Output: "b"
print(first_repeated_char("abcabcabc")) # Output: "a"
print(first_repeated_char("abcabcabcd")) # Output: "a"
print(first_repeated_char("abcdefg")) # Output: None
print(first_repeated_char("abcdefgabcdefg")) # Output: "a"
print(first_repeated_char("abcdefgabcdefgabcdefg")) # Output: "a"
print(first_repeated_char("abcdefgabcdefgabcdefgabcdefg")) # Output: "a"
print(first_repeated_char("abcdefgabcdefgabcdefgabcdefgabcdefg")) # Output: "a"
print(first_repeated_char("abcdefgabcdefgabcdefgabcdefgabcdefgabcdefg")) # Output: "a"
print(first_repeated_char("abcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefg")) # Output: "a"
print(first_repeated_char("abcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefg")) # Output: "a"
print(first_repeated_char("abcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefg")) # Output: "a"
print(first_repeated_char("abcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefg")) # Output: "a"
print(first_repeated_char("abcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefg")) # Output: "a"
print(first_repeated_char("abcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefg")) # Output: "a"
print(first_repeated_char("abcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefg")) # Output: "a"
print(first_repeated_char("abcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefg")) # Output: "a"
print(first_repeated_char("abcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefg")) # Output: "a"
print(first_repeated_char("abcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefg")) # Output: "a"
print(first_repeated_char("abcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefg")) # Output: "a"
print(first_repeated