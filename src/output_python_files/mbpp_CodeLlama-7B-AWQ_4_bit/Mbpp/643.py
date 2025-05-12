"""
Write a function that checks if a strings contains 'z', except at the start and end of the word.
assert text_match_wordz_middle("pythonzabc.")==True
"""


def text_match_wordz_middle(text):
    return text.startswith("z") and text.endswith("z") and "z" in text[1:-1]


print(text_match_wordz_middle("pythonzabc."))
print(text_match_wordz_middle("zpythonzabc."))
print(text_match_wordz_middle("pythonzabc.z"))
print(text_match_wordz_middle("pythonzabc.zpythonzabc."))
print(text_match_wordz_middle("pythonzabc.zpythonzabc.z"))
print(text_match_wordz_middle("pythonzabc.zpythonzabc.zpythonzabc."))
print(text_match_wordz_middle("pythonzabc.zpythonzabc.zpythonzabc.z"))
print(text_match_wordz_middle("pythonzabc.zpythonzabc.zpythonzabc.zpythonzabc."))
print(text_match_wordz_middle("pythonzabc.zpythonzabc.zpythonzabc.zpythonzabc.z"))
print(text_match_wordz_middle("pythonzabc.zpythonzabc.zpythonzabc.zpythonzabc.zpythonzabc."))
print(text_match_wordz_middle("pythonzabc.zpythonzabc.zpythonzabc.zpythonzabc.zpythonzabc.z"))
print(text_match_wordz_middle("pythonzabc.zpythonzabc.zpythonzabc.zpythonzabc.zpythonzabc.zpythonzabc."))
print(text_match_wordz_middle("pythonzabc.zpythonzabc.zpythonzabc.zpythonzabc.zpythonzabc.zpythonzabc.z"))
print(text_match_wordz_middle("pythonzabc.zpythonzabc.zpythonzabc.zpythonzabc.zpythonzabc.zpythonzabc.zpythonzabc."))
print(text_match_wordz_middle("pythonzabc.zpythonzabc.zpythonzabc.zpythonzabc.zpythonzabc.zpythonzabc.zpythonzabc.z"))
print(text_match_wordz_middle("pythonzabc.zpythonzabc.zpythonzabc.zpythonzabc.zpythonzabc.zpythonzabc.zpythonzabc.zpythonzabc."))
print(text_match_wordz_middle("pythonzabc.zpythonzabc.zpythonzabc.zpythonzabc.zpythonzabc.zpythonzabc.zpythonzabc.zpythonzabc.z"))
print(text_match_wordz_middle("pythonzabc.zpythonzabc.zpythonzabc.zpythonzabc.zpythonzabc.zpythonzabc.zpythonzabc.zpythonzabc.zpythonzabc."))
print(text_match_wordz_middle("pythonzabc.zpythonzabc.zpythonzabc.zpythonzabc.zpythonzabc.zpythonzabc.zpythonzabc.zpythonzabc.zpythonzabc.z"))
print(text_match_wordz_middle("pythonzabc.zpythonzabc.zpythonzabc.zpythonzabc.zpythonzabc.zpythonzabc.zpythonzabc.zpythonzabc.zpythonzabc.zpythonzabc."))
print(text_match_wordz_middle("pythonzabc.zpythonzabc.zpythonzabc.zpythonzabc.zpythonzabc.zpythonzabc.zpythonzabc.zpythonzabc.zpythonzabc.zpythonzabc.z"))
print(text_match_wordz_middle("pythonzabc.zpythonzabc.zpythonz