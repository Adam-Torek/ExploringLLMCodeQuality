"""
Write a function to convert a snake case string to camel case string.
assert snake_to_camel('python_program')=='PythonProgram'
"""

def snake_to_camel(s):
    # split the string by underscore
    words = s.split('_')
    # capitalize the first word
    first_word = words[0].capitalize()
    # join the rest of the words with uppercase
    rest_of_words = '_'.join(words[1:]).upper()
    # join the first word and rest of the words
    return first_word + rest_of_words

# test the function
assert snake_to_camel('python_program')=='PythonProgram'