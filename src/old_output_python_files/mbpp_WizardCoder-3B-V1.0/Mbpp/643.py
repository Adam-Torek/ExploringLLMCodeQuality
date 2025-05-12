"""
Write a function that checks if a strings contains 'z', except at the start and end of the word.
assert text_match_wordz_middle("pythonzabc.")==True
"""
def text_match_wordz_middle(text):
    words = text.split()
    for word in words:
        if word[0] == 'z' and word[-1] == 'z':
            return True
    return False

# Test cases
assert text_match_wordz_middle("pythonzabc.")==True
assert text_match_wordz_middle("pythonabcz.")==True
assert text_match_wordz_middle("pythonabc.")==False<|endoftext|>