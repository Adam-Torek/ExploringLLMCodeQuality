"""
Write a function to convert a snake case string to camel case string.
assert snake_to_camel('python_program')=='PythonProgram'
"""

def snake_to_camel(s):
    # split the string by underscore
    words = s.split('_')
    # capitalize the first word
    first_word = words[0].capitalize()
    # join the words with camel case
    return first_word + ''.join(words[1:]).replace('_', '')

# test the function
assert snake_to_camel('python_program')=='PythonProgram'