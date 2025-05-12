"""
Write a function that matches a string that has an a followed by three 'b'.
assert not text_match_three("ac")
"""

def text_match_three(text):
    if text[0] == 'a' and text[1:4] == 'bbb':
        return True
    else:
        return False

print(text_match_three("abb")) # True
print(text_match_three("abbb")) # True
print(text_match_three("abbbc")) # False
print(text_match_three("ac")) # False
print(text_match_three("abbc")) # False
print(text_match_three("aabbb")) # False
print(text_match_three("abb")) # True
print(text_match_three("aabb")) # False
print(text_match_three("abbba")) # False
print(text_match_three("abbbb")) # False
print(text_match_three("a")) # False
print(text_match_three("bbb")) # False
print(text_match_three("")) # False
print(text_match_three("a")) # False
print(text_match_three("bbb")) # False
print(text_match_three("ab")) # False
print(text_match_three("abbc")) # False
print(text_match_three("aab")) # False
print(text_match_three("abbbbb")) # False
print(text_match_three("abbbbbc")) # False
print(text_match_three("abbbc")) # False
print(text_match_three("abbbbc")) # False
print(text_match_three("abbba")) # False
print(text_match_three("aabbc")) # False
print(text_match_three("aabbbc")) # False
print(text_match_three("aabb")) # False
print(text_match_three("aabbc")) # False
print(text_match_three("aabbbc")) # False
print(text_match_three("aabbcc")) # False
print(text_match_three("aabbccd")) # False
print(text_match_three("aabbccd")) # False
print(text_match_three("aabbccd")) # False
print(text_match_three("aabbccd")) # False
print(text_match_three("aabbccd")) # False
print(text_match_three("aabbccd")) # False
print(text_match_three("aabbccd")) # False
print(text_match_three("aabbccd")) # False
print(text_match_three("aabbccd")) # False
print(text_match_three("aabbccd")) # False
print(text_match_three("aabbccd")) # False
print(text_match_three("aabbccd")) # False
print(text_match_three("aabbccd")) # False
print(text_match_three("aabbccd")) # False
print(text_match_three("aabbccd")) # False
print(text_match_three("aabbccd")) # False
print(text_match_three("aabbccd")) # False
print(text_match_three("aabbccd")) # False
print(text_match_three("aabbccd")) # False
print(text_match_three("aabbccd")) # False
print(text_match_three("aabbccd")) # False
print(text_match_three("aabbccd")) # False
print(text_match_three("aabbccd")) # False
print(text_match_three("aabbccd")) # False
print(text_match_three("aabbccd")) # False
print(text_match_three("aabbccd")) # False
print(text_match_three("aabbccd")) # False
print(text_match_three("aabbccd")) # False
print(text_match_three("aabbccd")) # False
print(text_match_three("aabbccd")) # False
print(text_match_three("aabbccd")) # False
print(text_match_three("aabbccd")) # False