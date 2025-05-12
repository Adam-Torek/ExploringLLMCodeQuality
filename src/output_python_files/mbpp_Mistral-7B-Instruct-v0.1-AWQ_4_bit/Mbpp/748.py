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
    spaces_between_capital_words = ' '.join(capital_words)
    return words[0] + spaces_between_capital_words + ' '.join(words[1:])

# Test the function
assert capital_words_spaces("Python") == 'Python'
assert capital_words_spaces("Java") == 'Java'
assert capital_words_spaces("PythonJava") == 'Python Java'