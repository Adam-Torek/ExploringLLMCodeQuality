"""
Write a function that matches a string that has an 'a' followed by anything, ending in 'b'.
assert text_starta_endb("aabbbb")
"""

def text_starta_endb(string):
    return string.startswith("a") and string.endswith("b")

print(text_starta_endb("aabbbb")) # True
print(text_starta_endb("abcab")) # False
print(text_starta_endb("abcd")) # False
print(text_starta_endb("ab")) # False
print(text_starta_endb("a")) # False
print(text_starta_endb("ba")) # False
print(text_starta_endb("abb")) # False
print(text_starta_endb("abcdab")) # True
print(text_starta_endb("abcdabcd")) # False
print(text_starta_endb("ab")) # False
print(text_starta_endb("a")) # False
print(text_starta_endb("ba")) # False
print(text_starta_endb("abb")) # False
print(text_starta_endb("aab")) # False
print(text_starta_endb("aabb")) # True
print(text_starta_endb("aabbc")) # False
print(text_starta_endb("aabbb")) # True
print(text_starta_endb("aabbbc")) # False
print(text_starta_endb("a")) # False
print(text_starta_endb("b")) # False
print(text_starta_endb("")) # False
print(text_starta_endb("cab")) # False
print(text_starta_endb("acb")) # False
print(text_starta_endb("cabab")) # False
print(text_starta_endb("acbab")) # False
print(text_starta_endb("cababab")) # False
print(text_starta_endb("acbab")) # False
print(text_starta_endb("acbabab")) # False
print(text_starta_endb("acbababab")) # False
print(text_starta_endb("acbabababab")) # False
print(text_starta_endb("acbababababab")) # False
print(text_starta_endb("acbabababababab")) # False
print(text_starta_endb("acbababababababab")) # False
print(text_starta_endb("acbabababababababab")) # False
print(text_starta_endb("acbababababababababab")) # False
print(text_starta_endb("acbabababababababababab")) # False
print(text_starta_endb("acbababababababababababab")) # False
print(text_starta_endb("acbabababababababababababab")) # False
print(text_starta_endb("acbababababababababababababab")) # False
print(text_starta_endb("acbabababababababababababababab")) # False
print(text_starta_endb("acbababababababababababababababab")) # False
print(text_starta_endb("acbabababababababababababababababab")) # False
print(text_starta_endb("acbababababababababababababababababab")) # False
print(text_starta_endb("acbabababababababababababababababababab")) # False
print(text_starta_endb("acbababababababababababababababababababab")) # False
print(text_starta_endb("acbabababababababababababababababababababab")) # False
print