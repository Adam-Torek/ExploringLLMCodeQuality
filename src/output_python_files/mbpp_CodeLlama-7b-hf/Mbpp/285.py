"""
Write a function that checks whether a string contains the 'a' character followed by two or three 'b' characters.
assert text_match_two_three("ac")==(False)
"""


def text_match_two_three(text):
    if text.count('a') == 0:
        return False
    else:
        if text.count('a') == 1:
            if text.count('b') == 2:
                return True
            else:
                return False
        else:
            if text.count('b') == 3:
                return True
            else:
                return False


print(text_match_two_three("ac"))
print(text_match_two_three("acb"))
print(text_match_two_three("acbb"))
print(text_match_two_three("acbbb"))
print(text_match_two_three("acbbbb"))
print(text_match_two_three("acbbbbb"))
print(text_match_two_three("acbbbbbb"))
print(text_match_two_three("acbbbbbbb"))
print(text_match_two_three("acbbbbbbbb"))
print(text_match_two_three("acbbbbbbbbb"))
print(text_match_two_three("acbbbbbbbbbb"))
print(text_match_two_three("acbbbbbbbbbbb"))
print(text_match_two_three("acbbbbbbbbbbbb"))
print(text_match_two_three("acbbbbbbbbbbbbb"))
print(text_match_two_three("acbbbbbbbbbbbbbb"))
print(text_match_two_three("acbbbbbbbbbbbbbbb"))
print(text_match_two_three("acbbbbbbbbbbbbbbbb"))
print(text_match_two_three("acbbbbbbbbbbbbbbbbb"))
print(text_match_two_three("acbbbbbbbbbbbbbbbbbb"))
print(text_match_two_three("acbbbbbbbbbbbbbbbbbbb"))
print(text_match_two_three("acbbbbbbbbbbbbbbbbbbbb"))
print(text_match_two_three("acbbbbbbbbbbbbbbbbbbbbb"))
print(text_match_two_three("acbbbbbbbbbbbbbbbbbbbbbb"))
print(text_match_two_three("acbbbbbbbbbbbbbbbbbbbbbbb"))
print(text_match_two_three("acbbbbbbbbbbbbbbbbbbbbbbbb"))
print(text_match_two_three("acbbbbbbbbbbbbbbbbbbbbbbbbb"))
print(text_match_two_three("acbbbbbbbbbbbbbbbbbbbbbbbbbb"))
print(text_match_two_three("acbbbbbbbbbbbbbbbbbbbbbbbbbbb"))
print(text_match_two_three("acbbbbbbbbbbbbbbbbbbbbbbbbbbbb"))
print(text_match_two_three("acbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"))
print(text_match_two_three("acbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"))
print(text_match_two_three("acbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"))
print(text_match_two_three("acbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"))
print(text_match_two_three("acbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"))
print(text_match_two_three("acbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"))
print(text_match_two_three("acbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"))
print(text_match_two_three("acbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"))
print(text_match_two_three("acbbbbbbbbbbbbbbbbbbbbbbbb