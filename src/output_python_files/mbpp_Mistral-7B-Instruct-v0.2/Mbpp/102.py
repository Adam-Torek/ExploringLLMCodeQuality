"""
Write a function to convert a snake case string to camel case string.
assert snake_to_camel('python_program')=='PythonProgram'
"""
def snake_to_camel(snake_string):
    words = snake_string.split('_')
    if len(words) == 1:
        return words[0]
    return words[0] + ''.join(word.capitalize() for word in words[1:])

assert snake_to_camel('python_program') == 'PythonProgram'
assert snake_to_camel('snake_case_string') == 'SnakeCaseString'
assert snake_to_camel('lower_case_with_one_word') == 'LowerCaseWithOneWord'
assert snake_to_camel('') == ''
assert snake_to_camel('single_word') == 'SingleWord'