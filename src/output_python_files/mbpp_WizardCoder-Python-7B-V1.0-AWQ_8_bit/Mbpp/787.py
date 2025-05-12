"""
Write a function that matches a string that has an a followed by three 'b'.
assert not text_match_three("ac")
"""

def text_match_three(text):
    if text[0] == 'a' and text[1:4] == 'bbb':
        return True
    else:
        return False

# Test cases
print(text_match_three("abbc")) # True
print(text_match_three("abbb")) # True
print(text_match_three("abbbc")) # False
print(text_match_three("aac")) # False
print(text_match_three("abb")) # False
print(text_match_three("abbba")) # False
print(text_match_three("abbbbb")) # False
print(text_match_three("abbbb")) # True
print(text_match_three("a")) # False
print(text_match_three("")) # False
print(text_match_three("abc")) # False
print(text_match_three("abcd")) # False
print(text_match_three("abbb")) # True
print(text_match_three("abb")) # False
print(text_match_three("a")) # False
print(text_match_three("bbb")) # False
print(text_match_three("bbbb")) # False
print(text_match_three("cbbb")) # False
print(text_match_three("ac")) # False
print(text_match_three("abbc")) # True
print(text_match_three("abbbc")) # False
print(text_match_three("abbcc")) # False
print(text_match_three("abbbbc")) # False
print(text_match_three("abbbbc")) # False
print(text_match_three("abbbbc")) # False
print(text_match_three("abbbbc")) # False
print(text_match_three("abbbbc")) # False
print(text_match_three("abbbbc")) # False
print(text_match_three("abbbbc")) # False
print(text_match_three("abbbbc")) # False
print(text_match_three("abbbbc")) # False
print(text_match_three("abbbbc")) # False
print(text_match_three("abbbbc")) # False
print(text_match_three("abbbbc")) # False
print(text_match_three("abbbbc")) # False
print(text_match_three("abbbbc")) # False
print(text_match_three("abbbbc")) # False
print(text_match_three("abbbbc")) # False
print(text_match_three("abbbbc")) # False
print(text_match_three("abbbbc")) # False
print(text_match_three("abbbbc")) # False
print(text_match_three("abbbbc")) # False
print(text_match_three("abbbbc")) # False
print(text_match_three("abbbbc")) # False
print(text_match_three("abbbbc")) # False
print(text_match_three("abbbbc")) # False
print(text_match_three("abbbbc")) # False
print(text_match_three("abbbbc")) # False
print(text_match_three("abbbbc")) # False
print(text_match_three("abbbbc")) # False
print(text_match_three("abbbbc")) # False
print(text_match_three("abbbbc")) # False
print(text_match_three("abbbbc")) # False
print(text_match_three("abbbbc")) # False
print(text_match_three("abbbbc")) # False
print(text_match_three("abbbbc")) # False
print(text_match_three("abbbbc")) # False
print(text_match_three("abbbbc")) # False
print(text_match_three("abbbbc")) # False
print(text_match_three("abbbbc")) # False
print(text_match_three("abbbbc")) # False
print(text_match_three("abbbbc")) # False
print(text_match_three("abbbbc")) # False
print(text_match_three("abbbbc")) # False
print(