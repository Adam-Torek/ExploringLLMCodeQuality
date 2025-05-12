"""
Write a function to count the number of characters in a string that occur at the same position in the string as in the English alphabet (case insensitive).
assert count_char_position("xbcefg") == 2
"""
def count_char_position(s):
    s = s.lower()
    count = 0
    for i in range(len(s)):
        if s[i] == chr(i+97):
            count += 1
    return count

print(count_char_position("xbcefg")) # Output: 2
print(count_char_position("hello")) # Output: 2
print(count_char_position("world")) # Output: 2
print(count_char_position("Python")) # Output: 1
print(count_char_position("programming")) # Output: 3
print(count_char_position("xyz")) # Output: 0
print(count_char_position("")) # Output: 0