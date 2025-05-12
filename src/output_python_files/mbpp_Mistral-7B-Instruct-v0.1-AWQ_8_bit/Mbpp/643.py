"""
Write a function that checks if a strings contains 'z', except at the start and end of the word.
assert text_match_wordz_middle("pythonzabc.")==True
"""

def text_match_wordz_middle(text):
    """
    Check if a string contains 'z' except at the start and end of the word.
    """
    # Split the string into a list of words
    words = text.split()

    # Iterate over each word in the list
    for word in words:
        # Check if the word contains 'z' except at the start and end of the word
        if 'z' in word and word[0] != 'z' and word[-1] != 'z':
            return True

    # If no 'z' is found in any of the words, return False
    return False