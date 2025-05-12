"""
Write a function to convert a snake case string to camel case string.
assert snake_to_camel('python_program')=='PythonProgram'
"""
def snake_to_camel(snake_string):
    words = snake_string.split('_')
    if len(words) > 1:
        return words[0] + ''.join(map(lambda x: x.capitalize(), words[1:]))
    else:
        return snake_string

assert snake_to_camel('python_program') == 'PythonProgram'
assert snake_to_camel('snake_case') == 'SnakeCase'
assert snake_to_camel('') == ''
assert snake_to_camel('single_word') == 'SingleWord'