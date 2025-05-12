"""
Write a function to convert a snake case string to camel case string.
assert snake_to_camel('python_program')=='PythonProgram'
"""
def snake_to_camel(snake_str):
    camel_str = ''
    for i in range(len(snake_str)):
        if i == 0:
            camel_str += snake_str[i].lower()
        else:
            if snake_str[i].isupper():
                camel_str += '_' + snake_str[i].lower()
            else:
                camel_str += snake_str[i]
    return camel_str

# Test cases
assert snake_to_camel('python_program')=='PythonProgram'
assert snake_to_camel('snake_case')=='SnakeCase'
assert snake_to_camel('UPPER_CASE')=='UpperCase'
assert snake_to_camel('mixed_case')=='MixedCase'<|endoftext|>