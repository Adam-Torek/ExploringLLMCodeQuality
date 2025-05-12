"""
Write a function that checks if a strings contains 'z', except at the start and end of the word.
assert text_match_wordz_middle("pythonzabc.")==True
"""

def text_match_wordz_middle(text):
    if text[0] == 'z' or text[-1] == 'z':
        return False
    for i in range(1, len(text)-1):
        if text[i] == 'z':
            return False
    return True

print(text_match_wordz_middle("pythonzabc.")) # True
print(text_match_wordz_middle("zabc.")) # False
print(text_match_wordz_middle("abc.")) # False
print(text_match_wordz_middle("pythonz")) # False
print(text_match_wordz_middle("zabc")) # False
print(text_match_wordz_middle("abc")) # True
print(text_match_wordz_middle("zabcxyz")) # False
print(text_match_wordz_middle("abcxyz")) # True
print(text_match_wordz_middle("zabcxyz.")) # False
print(text_match_wordz_middle("abcxyz.")) # True
print(text_match_wordz_middle("zabcxyzabc")) # False
print(text_match_wordz_middle("abcxyzabc")) # True
print(text_match_wordz_middle("zabcxyzabc.")) # False
print(text_match_wordz_middle("abcxyzabc.")) # True