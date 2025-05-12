"""
Write a function that checks if a strings contains 'z', except at the start and end of the word.
assert text_match_wordz_middle("pythonzabc.")==True
"""

def text_match_wordz_middle(text):
    if text.startswith("z") or text.endswith("z"):
        return False
    else:
        return True

assert text_match_wordz_middle("pythonzabc.")==True
assert text_match_wordz_middle("pythonabc.")==False
assert text_match_wordz_middle("pythonabcz")==False
assert text_match_wordz_middle("pythonabcz.")==True
assert text_match_wordz_middle("pythonabcz.")==True
assert text_match_wordz_middle("pythonabcz")==False
assert text_match_wordz_middle("pythonabcz.")==True
assert text_match_wordz_middle("pythonabcz")==False
assert text_match_wordz_middle("pythonabcz.")==True
assert text_match_wordz_middle("pythonabcz")==False
assert text_match_wordz_middle("pythonabcz.")==True
assert text_match_wordz_middle("pythonabcz")==False
assert text_match_wordz_middle("pythonabcz.")==True
assert text_match_wordz_middle("pythonabcz")==False
assert text_match_wordz_middle("pythonabcz.")==True
assert text_match_wordz_middle("pythonabcz")==False
assert text_match_wordz_middle("pythonabcz.")==True
assert text_match_wordz_middle("pythonabcz")==False
assert text_match_wordz_middle("pythonabcz.")==True
assert text_match_wordz_middle("pythonabcz")==False
assert text_match_wordz_middle("pythonabcz.")==True
assert text_match_wordz_middle("pythonabcz")==False
assert text_match_wordz_middle("pythonabcz.")==True
assert text_match_wordz_middle("pythonabcz")==False
assert text_match_wordz_middle("pythonabcz.")==True
assert text_match_wordz_middle("pythonabcz")==False
assert text_match_wordz_middle("pythonabcz.")==True
assert text_match_wordz_middle("pythonabcz")==False
assert text_match_wordz_middle("pythonabcz.")==True
assert text_match_wordz_middle("pythonabcz")==False
assert text_match_wordz_middle("pythonabcz.")==True
assert text_match_wordz_middle("pythonabcz")==False
assert text_match_wordz_middle("pythonabcz.")==True
assert text_match_wordz_middle("pythonabcz")==False
assert text_match_wordz_middle("pythonabcz.")==True
assert text_match_wordz_middle("pythonabcz")==False
assert text_match_wordz_middle("pythonabcz.")==True
assert text_match_wordz_middle("pythonabcz")==False
assert text_match_wordz_middle("pythonabcz.")==True
assert text_match_wordz_middle("pythonabcz")==False
assert text_match_wordz_middle("pythonabcz.")==True
assert text_match_wordz_middle("pythonabcz")==False
assert text_match_wordz_middle("pythonabcz.")==True
assert text_match_wordz_middle("pythonabcz")==False
assert text_match_wordz_middle("pythonabcz.")==True
assert text_match_wordz_middle("pythonabcz")==False
assert text_match_wordz_middle("pythonabcz.")==True
assert text_match_wordz_middle("pythonabcz")==False
assert text_match_wordz_middle("pythonabcz.")==True
assert text_match_wordz_middle("pythonabcz")==False
assert text_match_wordz_middle("pythonabcz.")==True
assert text_match_wordz_middle("pythonabc