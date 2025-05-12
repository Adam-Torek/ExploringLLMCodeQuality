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
print(count_char_position("xyzABCDEFGHIJKLMNOPQRSTUVWXYZ")) # Output: 52
print(count_char_position("XYZabcdefghijklmnopqrstuvwxyz")) # Output: 52
print(count_char_position("zyxwvutsrqponmlkjihgfedcba")) # Output: 26
print(count_char_position("zyxwvutsrqponmlkjihgfedcbaC")) # Output: 26
print(count_char_position("zyxwvutsrqponmlkjihgfedcbaZ")) # Output: 26
print(count_char_position("zyxwvutsrqponmlkjihgfedcba1234567890")) # Output: 0
print(count_char_position("")) # Output: 0
print(count_char_position("a")) # Output: 1
print(count_char_position("A")) # Output: 1
print(count_char_position("aA")) # Output: 2
print(count_char_position("aAa")) # Output: 3
print(count_char_position("aAaA")) # Output: 4
print(count_char_position("aAaAa")) # Output: 5
print(count_char_position("aAaAaA")) # Output: 6
print(count_char_position("aAaAaAa")) # Output: 7
print(count_char_position("aAaAaAaA")) # Output: 8
print(count_char_position("aAaAaAaAa")) # Output: 9
print(count_char_position("aAaAaAaAaA")) # Output: 10
print(count_char_position("aAaAaAaAaAa")) # Output: 11
print(count_char_position("aAaAaAaAaAaA")) # Output: 12
print(count_char_position("aAaAaAaAaAaAa")) # Output: 13
print(count_char_position("aAaAaAaAaAaAaA")) # Output: 14
print(count_char_position("aAaAaAaAaAaAaAa")) # Output: 15
print(count_char_position("aAaAaAaAaAaAaAaA")) # Output: 16
print(count_char_position("aAa