"""
Write a function that matches a string that has an 'a' followed by anything, ending in 'b'.
assert text_starta_endb("aabbbb")
"""

def text_starta_endb(string):
    return string.startswith('a') and string.endswith('b')

print(text_starta_endb("aabbbb")) # True
print(text_starta_endb("abbbba")) # False
print(text_starta_endb("baaab")) # False
print(text_starta_endb("aaab")) # True
print(text_starta_endb("aab")) # False
print(text_starta_endb("ab")) # False
print(text_starta_endb("a")) # False
print(text_starta_endb("b")) # False
print(text_starta_endb("")) # False
print(text_starta_endb("a")) # False
print(text_starta_endb("ba")) # False
print(text_starta_endb("abb")) # False
print(text_starta_endb("baa")) # False
print(text_starta_endb("aabba")) # False
print(text_starta_endb("abba")) # False
print(text_starta_endb("baab")) # False
print(text_starta_endb("aabb")) # True
print(text_starta_endb("aab")) # True
print(text_starta_endb("a")) # False
print(text_starta_endb("b")) # False
print(text_starta_endb("")) # False
print(text_starta_endb("a")) # False
print(text_starta_endb("ba")) # False
print(text_starta_endb("abb")) # False
print(text_starta_endb("baa")) # False
print(text_starta_endb("aabb")) # True
print(text_starta_endb("aab")) # True