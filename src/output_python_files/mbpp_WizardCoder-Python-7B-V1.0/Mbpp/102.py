"""
Write a function to convert a snake case string to camel case string.
assert snake_to_camel('python_program')=='PythonProgram'
"""
def snake_to_camel(snake_str):
    words = snake_str.split('_')
    camel_str = ''
    for word in words:
        camel_str += word.capitalize()
    return camel_str

print(snake_to_camel('python_program')) # Output: PythonProgram