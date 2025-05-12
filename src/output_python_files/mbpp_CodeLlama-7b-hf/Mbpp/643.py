"""
Write a function that checks if a strings contains 'z', except at the start and end of the word.
assert text_match_wordz_middle("pythonzabc.")==True
"""


def text_match_wordz_middle(text):
    if text[0] == "z" and text[-1] == "z":
        return False
    elif text[0] == "z":
        return text[1:] == text[1:].replace("z", "")
    elif text[-1] == "z":
        return text[:-1] == text[:-1].replace("z", "")
    else:
        return text == text.replace("z", "")


print(text_match_wordz_middle("pythonzabc."))
print(text_match_wordz_middle("pythonzabc"))
print(text_match_wordz_middle("pythonzabc.z"))
print(text_match_wordz_middle("pythonzabc.z."))
print(text_match_wordz_middle("pythonzabc.z.z"))
print(text_match_wordz_middle("pythonzabc.z.z."))
print(text_match_wordz_middle("pythonzabc.z.z.z"))
print(text_match_wordz_middle("pythonzabc.z.z.z."))
print(text_match_wordz_middle("pythonzabc.z.z.z.z"))
print(text_match_wordz_middle("pythonzabc.z.z.z.z."))
print(text_match_wordz_middle("pythonzabc.z.z.z.z.z"))
print(text_match_wordz_middle("pythonzabc.z.z.z.z.z."))
print(text_match_wordz_middle("pythonzabc.z.z.z.z.z.z"))
print(text_match_wordz_middle("pythonzabc.z.z.z.z.z.z."))
print(text_match_wordz_middle("pythonzabc.z.z.z.z.z.z.z"))
print(text_match_wordz_middle("pythonzabc.z.z.z.z.z.z.z."))
print(text_match_wordz_middle("pythonzabc.z.z.z.z.z.z.z.z"))
print(text_match_wordz_middle("pythonzabc.z.z.z.z.z.z.z.z."))
print(text_match_wordz_middle("pythonzabc.z.z.z.z.z.z.z.z.z"))
print(text_match_wordz_middle("pythonzabc.z.z.z.z.z.z.z.z.z."))
print(text_match_wordz_middle("pythonzabc.z.z.z.z.z.z.z.z.z.z"))
print(text_match_wordz_middle("pythonzabc.z.z.z.z.z.z.z.z.z.z."))
print(text_match_wordz_middle("pythonzabc.z.z.z.z.z.z.z.z.z.z.z"))
print(text_match_wordz_middle("pythonzabc.z.z.z.z.z.z.z.z.z.z.z."))
print(text_match_wordz_middle("pythonzabc.z.z.z.z.z.z.z.z.z.z.z.z"))
print(text_match_wordz_middle("pythonzabc.z.z.z.z.z.z.z.z.z.z.z.z."))
print(text_match_wordz_middle("pythonzabc.z.z.z.z.z.z.z.z