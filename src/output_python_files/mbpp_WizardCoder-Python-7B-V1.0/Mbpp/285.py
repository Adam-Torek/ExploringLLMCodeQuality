"""
Write a function that checks whether a string contains the 'a' character followed by two or three 'b' characters.
assert text_match_two_three("ac")==(False)
"""
def text_match_two_three(text):
    if 'a' in text and 'b' in text:
        if text.count('a') == 1 and text.count('b') == 2:
            return True
        elif text.count('a') == 1 and text.count('b') == 3:
            return True
        else:
            return False
    else:
        return False

print(text_match_two_three("ac")) # False
print(text_match_two_three("abbb")) # False
print(text_match_two_three("abbbb")) # True
print(text_match_two_three("abb")) # False
print(text_match_two_three("abbc")) # True
print(text_match_two_three("abbbc")) # True
print(text_match_two_three("abbcc")) # False
print(text_match_two_three("abbbbc")) # True
print(text_match_two_three("abbccc")) # False
print(text_match_two_three("aabbbc")) # False
print(text_match_two_three("aabbcc")) # False
print(text_match_two_three("aabb")) # False
print(text_match_two_three("aabbb")) # True
print(text_match_two_three("aabbc")) # False
print(text_match_two_three("aabbcc")) # False
print(text_match_two_three("aabb")) # False
print(text_match_two_three("aabbc")) # False
print(text_match_two_three("aabbcc")) # False
print(text_match_two_three("aabb")) # False
print(text_match_two_three("aabbc")) # False
print(text_match_two_three("aabbcc")) # False
print(text_match_two_three("aabb")) # False
print(text_match_two_three("aabbc")) # False
print(text_match_two_three("aabbcc")) # False
print(text_match_two_three("aabb")) # False
print(text_match_two_three("aabbc")) # False
print(text_match_two_three("aabbcc")) # False
print(text_match_two_three("aabb")) # False
print(text_match_two_three("aabbc")) # False
print(text_match_two_three("aabbcc")) # False
print(text_match_two_three("aabb")) # False
print(text_match_two_three("aabbc")) # False
print(text_match_two_three("aabbcc")) # False
print(text_match_two_three("aabb")) # False
print(text_match_two_three("aabbc")) # False
print(text_match_two_three("aabbcc")) # False
print(text_match_two_three("aabb")) # False
print(text_match_two_three("aabbc")) # False
print(text_match_two_three("aabbcc")) # False
print(text_match_two_three("aabb")) # False
print(text_match_two_three("aabbc")) # False
print(text_match_two_three("aabbcc")) # False
print(text_match_two_three("aabb")) # False
print(text_match_two_three("aabbc")) # False
print(text_match_two_three("aabbcc")) # False
print(text_match_two_three("aabb")) # False
print(text_match_two_three("aabbc")) # False
print(text_match_two_three("aabbcc")) # False
print(text_match_two_three("aabb")) # False
print(text_match_two_three("aabbc")) # False
print(text_match_two_three("aabbcc")) # False
print(text_match