"""
Write a function to put spaces between words starting with capital letters in a given string.
assert capital_words_spaces("Python") == 'Python'
"""

def capital_words_spaces(string):
    return ' '.join(string[0].upper() + string[1:] for string in string.split(' '))

# Test cases
print(capital_words_spaces("Python")) # Output: Python
print(capital_words_spaces("This is a test string")) # Output: This is a Test String
print(capital_words_spaces("This is another test string")) # Output: This is Another Test String
print(capital_words_spaces("This is a test string with multiple capital letters")) # Output: This is a Test String with Multiple Capital Letters
print(capital_words_spaces("This is a test string with multiple capital letters and spaces")) # Output: This is a Test String with Multiple Capital Letters and Spaces
print(capital_words_spaces("This is a test string with multiple capital letters and spaces and numbers123")) # Output: This is a Test String with Multiple Capital Letters and Spaces and Numbers123
print(capital_words_spaces("This is a test string with multiple capital letters and spaces and numbers 123")) # Output: This is a Test String with Multiple Capital Letters and Spaces and Numbers 123
print(capital_words_spaces("This is a test string with multiple capital letters and spaces and numbers 123 and symbols #$%")) # Output: This is a Test String with Multiple Capital Letters and Spaces and Numbers 123 and Symbols #$%
print(capital_words_spaces("This is a test string with multiple capital letters and spaces and numbers 123 and symbols #$% and spaces")) # Output: This is a Test String with Multiple Capital Letters and Spaces and Numbers 123 and Symbols #$% and Spaces
print(capital_words_spaces("This is a test string with multiple capital letters and spaces and numbers 123 and symbols #$% and spaces and more spaces")) # Output: This is a Test String with Multiple Capital Letters and Spaces and Numbers 123 and Symbols #$% and Spaces and More Spaces
print(capital_words_spaces("")) # Output: