"""
Write a python function to find the first repeated character in a given string.
assert first_repeated_char("abcabc") == "a"
"""

def first_repeated_char(s):
    char_dict = {}
    for char in s:
        if char in char_dict:
            return char
        else:
            char_dict[char] = 1
    return None

# Test cases
print(first_repeated_char("abcabc")) # Output: "a"
print(first_repeated_char("abca")) # Output: None
print(first_repeated_char("hello world")) # Output: "l"
print(first_repeated_char("aabbcde")) # Output: "a"
print(first_repeated_char("aabbcdee")) # Output: "a"
print(first_repeated_char("aabbccdde")) # Output: "a"
print(first_repeated_char("aabbccddee")) # Output: "a"
print(first_repeated_char("aabbccddeef")) # Output: "a"
print(first_repeated_char("aabbccddeeff")) # Output: "a"
print(first_repeated_char("aabbccddeefff")) # Output: "a"
print(first_repeated_char("aabbccddeeffg")) # Output: "a"
print(first_repeated_char("aabbccddeeffgf")) # Output: "a"
print(first_repeated_char("aabbccddeeffgh")) # Output: "a"
print(first_repeated_char("aabbccddeeffghi")) # Output: "a"
print(first_repeated_char("aabbccddeeffghh")) # Output: "a"
print(first_repeated_char("aabbccddeeffghhf")) # Output: "a"
print(first_repeated_char("aabbccddeeffghhi")) # Output: "a"
print(first_repeated_char("aabbccddeeffghhfk")) # Output: "a"
print(first_repeated_char("aabbccddeeffghhih")) # Output: "a"
print(first_repeated_char("aabbccddeeffghhif")) # Output: "a"
print(first_repeated_char("aabbccddeeffghhiff")) # Output: "a"
print(first_repeated_char("aabbccddeeffghhiffk")) # Output: "a"
print(first_repeated_char("aabbccddeeffghhiffl")) # Output: "a"
print(first_repeated_char("aabbccddeeffghhifflk")) # Output: "a"
print(first_repeated_char("aabbccddeeffghhifflkj")) # Output: "a"
print(first_repeated_char("aabbccddeeffghhifflkjj")) # Output: "a"
print(first_repeated_char("aabbccddeeffghhifflkjjj")) # Output: "a"
print(first_repeated_char("aabbccddeeffghhifflkjjjj")) # Output: "a"
print(first_repeated_char("aabbccddeeffghhifflkjjjjj")) # Output: "a"
print(first_repeated_char("aabbccddeeffghhifflkjjjjjj")) # Output: "a"
print(first_repeated_char("aabbccddeeffghhifflkjjjjjjj")) # Output: "a"
print(first_repeated_char("aabbccddeeffghhifflkjjjjjjjj")) # Output: "a"
print(first_repeated_char("aabbccddeeffghhifflkjjjjjjjjj")) # Output: "a"
print(first_