"""
Write a function that matches a word containing 'z'.
assert text_match_wordz("pythonz.")==True
"""

def text_match_wordz(text):
    """
    Check if the text contains a word with 'z' in it.
    """
    # Split the text into a list of words
    words = text.split()

    # Iterate over each word in the list
    for word in words:
        # Check if the word contains 'z'
        if 'z' in word:
            # Return True if a word with 'z' is found
            return True

    # Return False if no word with 'z' is found
    return False