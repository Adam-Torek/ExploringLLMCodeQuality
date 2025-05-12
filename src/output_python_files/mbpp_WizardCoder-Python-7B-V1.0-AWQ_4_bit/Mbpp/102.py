"""
Write a function to convert a snake case string to camel case string.
assert snake_to_camel('python_program')=='PythonProgram'
"""

def snake_to_camel(snake_str):
    words = snake_str.split('_')
    return words[0].lower() + ''.join(word.title() for word in words[1:])

print(snake_to_camel('python_program')) # Output: PythonProgram
print(snake_to_camel('snake_case_string_to_camel_case_string')) # Output: SnakeCaseStringToCamelCaseString
print(snake_to_camel('snake_case_string_to_camel_case_string_function')) # Output: SnakeCaseStringToCamelCaseStringFunction