"""
Write a function to put spaces between words starting with capital letters in a given string.
assert capital_words_spaces("Python") == 'Python'
"""

def capital_words_spaces(s):
    words = s.split()
    capitalized_words = []
    for word in words:
        if word[0].isupper():
            capitalized_words.append(word)
        else:
            capitalized_words.append(''+ word)
    return ''.join(capitalized_words)

# Test cases
assert capital_words_spaces("Python") == 'Python'
assert capital_words_spaces("Java Script") == 'Java Script'
assert capital_words_spaces("Python is awesome") == 'Python is awesome'
assert capital_words_spaces("Python is not awesome") == 'Python is not awesome'<|endoftext|>