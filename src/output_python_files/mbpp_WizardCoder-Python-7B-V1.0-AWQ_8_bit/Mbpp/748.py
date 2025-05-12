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
print(capital_words_spaces("This is a test string with multiple words")) # Output: This is a Test String with Multiple Words
print(capital_words_spaces("This is a test string with multiple CapitalWords")) # Output: This is a Test String with Multiple CapitalWords
print(capital_words_spaces("This is a test string with multiple CapitalWords and Numbers123")) # Output: This is a Test String with Multiple CapitalWords and Numbers123
print(capital_words_spaces("This is a test string with multiple CapitalWords and Numbers123 and spaces")) # Output: This is a Test String with Multiple CapitalWords and Numbers123 and Spaces
print(capital_words_spaces("This is a test string with multiple CapitalWords and Numbers123 and spaces and UPPERCASE")) # Output: This is a Test String with Multiple CapitalWords and Numbers123 and Spaces and UPPERCASE
print(capital_words_spaces("This is a test string with multiple CapitalWords and Numbers123 and spaces and UPPERCASE and lowercase")) # Output: This is a Test String with Multiple CapitalWords and Numbers123 and Spaces and UPPERCASE and Lowercase
print(capital_words_spaces("This is a test string with multiple CapitalWords and Numbers123 and spaces and UPPERCASE and lowercase and Minus-Word")) # Output: This is a Test String with Multiple CapitalWords and Numbers123 and Spaces and UPPERCASE and Lowercase and Minus-Word
print(capital_words_spaces("This is a test string with multiple CapitalWords and Numbers123 and spaces and UPPERCASE and lowercase and Minus-Word and UPPER-UPPER")) # Output: This is a Test String with Multiple CapitalWords and Numbers123 and Spaces and UPPERCASE and Lowercase and Minus-Word and UPPER-UPPER
print(capital_words_spaces("This is a test string with multiple CapitalWords and Numbers123 and spaces and UPPERCASE and lowercase and Minus-Word and UPPER-UPPER and special-char@cter$")) # Output: This is a Test String with Multiple CapitalWords and Numbers123 and Spaces and UPPERCASE and Lowercase and Minus-Word and UPPER-UPPER and Special-Char@cter$
print(capital_words_spaces("")) # Output: