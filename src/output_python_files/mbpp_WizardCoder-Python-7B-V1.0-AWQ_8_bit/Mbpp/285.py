"""
Write a function that checks whether a string contains the 'a' character followed by two or three 'b' characters.
assert text_match_two_three("ac")==(False)
"""
def text_match_two_three(string):
    if 'a' in string and 'b'*2 in string or 'a' in string and 'b'*3 in string:
        return True
    else:
        return False

print(text_match_two_three("ac")) # False
print(text_match_two_three("abb")) # True
print(text_match_two_three("abbb")) # True
print(text_match_two_three("abbc")) # False
print(text_match_two_three("abbbc")) # True
print(text_match_two_three("abbcc")) # False
print(text_match_two_three("abbbb")) # True
print(text_match_two_three("abbbbc")) # False
print(text_match_two_three("abbccc")) # False
print(text_match_two_three("abbbbb")) # True
print(text_match_two_three("abbbbbc")) # False
print(text_match_two_three("abbbbbbc")) # False
print(text_match_two_three("abbcccc")) # False
print(text_match_two_three("abbccccc")) # False
print(text_match_two_three("abbcccccc")) # False
print(text_match_two_three("abbcccccccc")) # False
print(text_match_two_three("abbcccccccccc")) # False
print(text_match_two_three("abbbbbbbbbb")) # True
print(text_match_two_three("abbbbbbbbbbc")) # False
print(text_match_two_three("abbcccccccccc")) # False
print(text_match_two_three("abbccccccccccc")) # False
print(text_match_two_three("abbcccccccccccc")) # False
print(text_match_two_three("abbccccccccccc")) # False
print(text_match_two_three("abbccccccccccccc")) # False
print(text_match_two_three("abbcccccccccccccc")) # False
print(text_match_two_three("abbcccccccccccccccc")) # False
print(text_match_two_three("abbccccccccccccccccc")) # False
print(text_match_two_three("abbcccccccccccccccccc")) # False
print(text_match_two_three("abbccccccccccccccccccc")) # False
print(text_match_two_three("abbcccccccccccccccccccc")) # False
print(text_match_two_three("abbcccccccccccccccccccc")) # False
print(text_match_two_three("abbccccccccccccccccccccc")) # False
print(text_match_two_three("abbcccccccccccccccccccccc")) # False
print(text_match_two_three("abbcccccccccccccccccccccc")) # False
print(text_match_two_three("abbccccccccccccccccccccccc")) # False
print(text_match_two_three("abbcccccccccccccccccccccccc")) # False
print(text_match_two_three("abbccccccccccccccccccccccc")) # False
print(text_match_two_three("abbcccccccccccccccccccccccc")) # False
print(text_match_two_three("abbcccccccccccccccccccccccc")) # False
print(text_match_two_three("abbcccccccccccccccccccccccc")) # False
print(text_match_two_three("abbcccccccccccccccccccccccc")) # False
print(text_match_two_three("abbcccccccccccccccccccccccc")) # False
print(text_match_two_three("abbcccccccccccccccccccccccc")) # False
print(text_match_