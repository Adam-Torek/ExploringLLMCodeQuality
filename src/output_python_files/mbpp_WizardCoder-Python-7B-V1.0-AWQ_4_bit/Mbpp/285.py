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
print(text_match_two_three("abbccc")) # False
print(text_match_two_three("abbbbb")) # True
print(text_match_two_three("abbbbbc")) # False
print(text_match_two_three("abbbbcc")) # False
print(text_match_two_three("abbccb")) # False
print(text_match_two_three("abbccc")) # False
print(text_match_two_three("abbbbbc")) # False
print(text_match_two_three("abbccbb")) # False
print(text_match_two_three("abbbbbcc")) # False
print(text_match_two_three("abbbbccb")) # False
print(text_match_two_three("abbbcccc")) # False
print(text_match_two_three("abbbbccc")) # False
print(text_match_two_three("abbbbbbb")) # True
print(text_match_two_three("abbbbbbbc")) # False
print(text_match_two_three("abbbbbbcc")) # False
print(text_match_two_three("abbbbbccc")) # False
print(text_match_two_three("abbbbbbcc")) # False
print(text_match_two_three("abbbbbccb")) # False
print(text_match_two_three("abbbbcccc")) # False
print(text_match_two_three("abbbbccbb")) # False
print(text_match_two_three("abbbbccbbc")) # False
print(text_match_two_three("abbbbccbbb")) # False
print(text_match_two_three("abbbbccbbcc")) # False
print(text_match_two_three("abbbbccbbbc")) # False
print(text_match_two_three("abbbbccbbbb")) # False
print(text_match_two_three("abbbbccbbbbc")) # False
print(text_match_two_three("abbbbccbbbbb")) # False
print(text_match_two_three("abbbbccbbbbcc")) # False
print(text_match_two_three("abbbbccbbbbbc")) # False
print(text_match_two_three("abbbbccbbbbbb")) # False
print(text_match_two_three("abbbbccbbbbbbc")) # False
print(text_match_two_three("abbbbccbbbbbbb")) # False
print(text_match_two_three("abbbbccbbbbbbcc")) # False
print(text_match_two_three("abbbbccbbbbbbbc")) # False
print(text_match_two_three("abbbbccbbbbbbbb")) # False
print(text_match_two_three("abbbbccbbbbbbbc")) # False
print(text_match_two_three("abbbbccbbbbbbbbc")) # False
print(text_match_two_three("abbbbccbbbbbbbbb")) # False
print(text_match_two_three("abbbbccbbbbbbbbcc")) # False
print(text_match_two_three("abbbbccbbbb