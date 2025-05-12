"""
Write a function that checks if a strings contains 'z', except at the start and end of the word.
assert text_match_wordz_middle("pythonzabc.")==True
"""

def text_match_wordz_middle(text):
    if text.startswith("z") and text.endswith("z"):
        return True
    else:
        return False

assert text_match_wordz_middle("pythonzabc.")==True
assert text_match_wordz_middle("pythonzabc")==False
assert text_match_wordz_middle("pythonabcz")==False
assert text_match_wordz_middle("pythonabc")==False
assert text_match_wordz_middle("zpythonabc")==False
assert text_match_wordz_middle("zpythonabcz")==True
assert text_match_wordz_middle("zpythonabcz.")==True
assert text_match_wordz_middle("zpythonabcz.")==True
assert text_match_wordz_middle("zpythonabcz")==True
assert text_match_wordz_middle("zpythonabcz")==True
assert text_match_wordz_middle("zpythonabcz")==True
assert text_match_wordz_middle("zpythonabcz")==True
assert text_match_wordz_middle("zpythonabcz")==True
assert text_match_wordz_middle("zpythonabcz")==True
assert text_match_wordz_middle("zpythonabcz")==True
assert text_match_wordz_middle("zpythonabcz")==True
assert text_match_wordz_middle("zpythonabcz")==True
assert text_match_wordz_middle("zpythonabcz")==True
assert text_match_wordz_middle("zpythonabcz")==True
assert text_match_wordz_middle("zpythonabcz")==True
assert text_match_wordz_middle("zpythonabcz")==True
assert text_match_wordz_middle("zpythonabcz")==True
assert text_match_wordz_middle("zpythonabcz")==True
assert text_match_wordz_middle("zpythonabcz")==True
assert text_match_wordz_middle("zpythonabcz")==True
assert text_match_wordz_middle("zpythonabcz")==True
assert text_match_wordz_middle("zpythonabcz")==True
assert text_match_wordz_middle("zpythonabcz")==True
assert text_match_wordz_middle("zpythonabcz")==True
assert text_match_wordz_middle("zpythonabcz")==True
assert text_match_wordz_middle("zpythonabcz")==True
assert text_match_wordz_middle("zpythonabcz")==True
assert text_match_wordz_middle("zpythonabcz")==True
assert text_match_wordz_middle("zpythonabcz")==True
assert text_match_wordz_middle("zpythonabcz")==True
assert text_match_wordz_middle("zpythonabcz")==True
assert text_match_wordz_middle("zpythonabcz")==True
assert text_match_wordz_middle("zpythonabcz")==True
assert text_match_wordz_middle("zpythonabcz")==True
assert text_match_wordz_middle("zpythonabcz")==True
assert text_match_wordz_middle("zpythonabcz")==True
assert text_match_wordz_middle("zpythonabcz")==True
assert text_match_wordz_middle("zpythonabcz")==True
assert text_match_wordz_middle("zpythonabcz")==True
assert text_match_wordz_middle("zpythonabcz")==True
assert text_match_wordz_middle("zpythonabcz")==True
assert text_match_wordz_middle("zpythonabcz")==True
assert text_match_wordz_middle("zpythonabcz")==True
assert text_match_wordz_middle("zpythonabcz")==True
assert text_match_wordz_middle("zpythonabcz")==True
assert text_match_wordz_middle("zpythonabcz")==True
assert text_match_wordz_middle("zpythonabcz")==True
assert text_match_wordz_middle("z