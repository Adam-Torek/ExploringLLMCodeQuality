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
print(text_match_three("abbb")) # False
print(text_match_three("abbbc")) # False
print(text_match_three("abbbbc")) # True
print(text_match_three("aabbbbc")) # False
print(text_match_three("aabbbbcc")) # False
print(text_match_three("abbbb")) # True
print(text_match_three("a")) # False
print(text_match_three("ab")) # False
print(text_match_three("abc")) # False
print(text_match_three("abbb")) # True
print(text_match_three("abbc")) # False
print(text_match_three("abbbbcc")) # False
print(text_match_three("abbbb")) # True
print(text_match_three("aabbc")) # False
print(text_match_three("abbbbc")) # True
print(text_match_three("aabbbbcc")) # False
print(text_match_three("abbbbc")) # True
print(text_match_three("aabb")) # False
print(text_match_three("abbc")) # False
print(text_match_three("abc")) # False
print(text_match_three("abbb")) # True
print(text_match_three("a")) # False
print(text_match_three("ab")) # False
print(text_match_three("")) # False
print(text_match_three("a")) # False
print(text_match_three("b")) # False
print(text_match_three("bbb")) # False
print(text_match_three("bbbb")) # False
print(text_match_three("bbbbc")) # False
print(text_match_three("bbbb")) # False
print(text_match_three("bbb")) # True
print(text_match_three("bbbc")) # False
print(text_match_three("bbbcc")) # False
print(text_match_three("bbb")) # True
print(text_match_three("bbbc")) # False
print(text_match_three("bbbcc")) # False
print(text_match_three("b")) # False
print(text_match_three("c")) # False
print(text_match_three("cc")) # False
print(text_match_three("cbbb")) # False
print(text_match_three("cbbbc")) # False
print(text_match_three("cbbb")) # False
print(text_match_three("cbbbc")) # False
print(text_match_three("cbbbcc")) # False
print(text_match_three("cbbb")) # False
print(text_match_three("cbbbc")) # False
print(text_match_three("cbbbcc")) # False
print(text_match_three("c")) # False
print(text_match_three("cc")) # False
print(text_match_three("ccbbb")) # False
print(text_match_three("ccbbbc")) # False
print(text_match_three("ccbbb")) # False
print(text_match_three("ccbbbc")) # False
print(text_match_three("ccbbbcc")) # False
print(text_match_three("ccbbb")) # False
print(text_match_three("ccbbbc")) # False
print(text_match_three("ccbbbcc")) # False
print(text_match_three("ccb")) # False
print(text_match_three("ccbb")) # False
print(text_match_three("ccbbc")) # False
print(text_match_three("ccbb")) # False
print(text_match_three("ccbbc")) # False
print(text_match_three("ccbbcc")) # False
print(text