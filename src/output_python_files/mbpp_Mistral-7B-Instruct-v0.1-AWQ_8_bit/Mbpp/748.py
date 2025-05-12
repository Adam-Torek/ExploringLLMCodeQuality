"""
Write a function to put spaces between words starting with capital letters in a given string.
assert capital_words_spaces("Python") == 'Python'
"""

def capital_words_spaces(string):
    """
    This function takes a string as an input and returns the string with spaces between words starting with capital letters.
    """
    words = string.split()
    capital_words = [word for word in words if word[0].isupper()]
    spaces = [word for word in words if not word[0].isupper()]
    capital_words_spaces = ' '.join(capital_words) + ' '.join(spaces)
    return capital_words_spaces


# Test the function
string = "Python"
assert capital_words_spaces(string) == string