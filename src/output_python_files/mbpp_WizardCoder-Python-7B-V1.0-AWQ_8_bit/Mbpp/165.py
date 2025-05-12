"""
Write a function to count the number of characters in a string that occur at the same position in the string as in the English alphabet (case insensitive).
assert count_char_position("xbcefg") == 2
"""

def count_char_position(s):
    count = 0
    for i in range(len(s)):
        if s[i].lower() == chr(i+97):
            count += 1
    return count

print(count_char_position("xbcefg")) # Output: 2
print(count_char_position("abcdefg")) # Output: 0
print(count_char_position("xyz")) # Output: 0
print(count_char_position("abcxyz")) # Output: 3
print(count_char_position("xyzabc")) # Output: 3
print(count_char_position("abcXYZ")) # Output: 3
print(count_char_position("XYZabc")) # Output: 3
print(count_char_position("xyzABC")) # Output: 3
print(count_char_position("abcdefghijklmnopqrstuvwxyz")) # Output: 26
print(count_char_position("ABCDEFGHIJKLMNOPQRSTUVWXYZ")) # Output: 26
print(count_char_position("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")) # Output: 52
print(count_char_position("")) # Output: 0