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
print(first_repeated_char("abca")) # Output: "a"
print(first_repeated_char("abc")) # Output: None
print(first_repeated_char("abcaab")) # Output: "a"
print(first_repeated_char("abba")) # Output: "a"
print(first_repeated_char("abcbc")) # Output: "b"
print(first_repeated_char("abcabcabc")) # Output: "a"
print(first_repeated_char("abcabcabcd")) # Output: "a"
print(first_repeated_char("abcabcabcabcd")) # Output: "a"
print(first_repeated_char("abcabcabcabcde")) # Output: "a"
print(first_repeated_char("abcdefg")) # Output: None
print(first_repeated_char("")) # Output: None
print(first_repeated_char("a")) # Output: "a"
print(first_repeated_char("aa")) # Output: "a"
print(first_repeated_char("aaa")) # Output: "a"
print(first_repeated_char("aaaa")) # Output: "a"
print(first_repeated_char("abbaa")) # Output: "a"
print(first_repeated_char("abbaaab")) # Output: "a"
print(first_repeated_char("abbaaabc")) # Output: "a"
print(first_repeated_char("abbaaabcd")) # Output: "a"
print(first_repeated_char("abbaaabcdc")) # Output: "a"
print(first_repeated_char("abbaaabcdcde")) # Output: "a"
print(first_repeated_char("abbaaabcdcdea")) # Output: "a"
print(first_repeated_char("abbaaabcdcdef")) # Output: "a"
print(first_repeated_char("abbaaabcdcdefg")) # Output: "a"
print(first_repeated_char("abbaaabcdcdefgh")) # Output: "a"
print(first_repeated_char("abbaaabcdcdefghi")) # Output: "a"
print(first_repeated_char("abbaaabcdcdefghij")) # Output: "a"
print(first_repeated_char("abbaaabcdcdefghijk")) # Output: "a"
print(first_repeated_char("abbaaabcdcdefghijkl")) # Output: "a"
print(first_repeated_char("abbaaabcdcdefghijklm")) # Output: "a"
print(first_repeated_char("abbaaabcdcdefghijklmn")) # Output: "a"
print(first_repeated_char("abbaaabcdcdefghijklmno")) # Output: "a"
print(first_repeated_char("abbaaabcdcdefghijklmnop")) # Output: "a"
print(first_repeated_char("abbaaabcdcdefghijklmnopq")) # Output: "a"
print(first_repeated_char("abbaaabcdcdefghijklmnopqr")) # Output: "a"
print(first_repeated_char("abbaaabcdcdefghijklmnopqrs")) # Output: "a"
print(first_repeated_char("abbaaabcdcdefghijklmnopqrst")) # Output: "a"
print(first_repeated_char("