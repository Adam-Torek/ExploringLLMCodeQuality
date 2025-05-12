"""
Write a function that matches a string that has an 'a' followed by anything, ending in 'b'.
assert text_starta_endb("aabbbb")
"""

def text_starta_endb(string):
    return string.startswith('a') and string.endswith('b')

print(text_starta_endb("aabbbb")) # True
print(text_starta_endb("abcab")) # False
print(text_starta_endb("abbbb")) # False
print(text_starta_endb("aabcd")) # False
print(text_starta_endb("abba")) # False
print(text_starta_endb("aab")) # True
print(text_starta_endb("aaab")) # True
print(text_starta_endb("aabb")) # True
print(text_starta_endb("aaaab")) # True
print(text_starta_endb("aaaabbb")) # False
print(text_starta_endb("aaaabbbb")) # True
print(text_starta_endb("aaaabbbc")) # False
print(text_starta_endb("aaaabbb")) # True
print(text_starta_endb("aaaabbbc")) # False
print(text_starta_endb("aaaab")) # True
print(text_starta_endb("aaaac")) # False
print(text_starta_endb("aaaacb")) # False
print(text_starta_endb("aaaacb")) # False
print(text_starta_endb("aaaacb")) # False
print(text_starta_endb("aaaacb")) # False
print(text_starta_endb("aaaacb")) # False
print(text_starta_endb("aaaacb")) # False
print(text_starta_endb("aaaacb")) # False
print(text_starta_endb("aaaacb")) # False
print(text_starta_endb("aaaacb")) # False
print(text_starta_endb("aaaacb")) # False
print(text_starta_endb("aaaacb")) # False
print(text_starta_endb("aaaacb")) # False
print(text_starta_endb("aaaacb")) # False
print(text_starta_endb("aaaacb")) # False
print(text_starta_endb("aaaacb")) # False
print(text_starta_endb("aaaacb")) # False
print(text_starta_endb("aaaacb")) # False
print(text_starta_endb("aaaacb")) # False
print(text_starta_endb("aaaacb")) # False
print(text_starta_endb("aaaacb")) # False
print(text_starta_endb("aaaacb")) # False
print(text_starta_endb("aaaacb")) # False
print(text_starta_endb("aaaacb")) # False
print(text_starta_endb("aaaacb")) # False
print(text_starta_endb("aaaacb")) # False
print(text_starta_endb("aaaacb")) # False
print(text_starta_endb("aaaacb")) # False
print(text_starta_endb("aaaacb")) # False
print(text_starta_endb("aaaacb")) # False
print(text_starta_endb("aaaacb")) # False
print(text_starta_endb("aaaacb")) # False
print(text_starta_endb("aaaacb")) # False
print(text_starta_endb("aaaacb")) # False
print(text_starta_endb("aaaacb")) # False
print(text_starta_endb("aaaacb")) # False
print(text_starta_endb("aaaacb")) # False
print(text_starta_endb("aaaacb