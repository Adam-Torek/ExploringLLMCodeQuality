"""
Write a function to convert a snake case string to camel case string.
assert snake_to_camel('python_program')=='PythonProgram'
"""


def snake_to_camel(snake_str):
    """
    :param snake_str: snake case string
    :return: camel case string
    """
    components = snake_str.split('_')
    # We capitalize the first letter of each component except the first one
    # with the 'capitalize' method and join them together.
    return components[0] + ''.join(x.capitalize() for x in components[1:])


if __name__ == '__main__':
    print(snake_to_camel('python_program'))
    print(snake_to_camel('python_program_is_fun'))
    print(snake_to_camel('python_is_fun'))
    print(snake_to_camel('python_is_fun_too'))
    print(snake_to_camel('python_is_fun_too_'))
    print(snake_to_camel('_python_is_fun_too_'))
    print(snake_to_camel('_python_is_fun_too'))
    print(snake_to_camel('_python_is_fun_too_'))
    print(snake_to_camel('_python_is_fun_too_'))
    print(snake_to_camel('_python_is_fun_too_'))
    print(snake_to_camel('_python_is_fun_too_'))
    print(snake_to_camel('_python_is_fun_too_'))
    print(snake_to_camel('_python_is_fun_too_'))
    print(snake_to_camel('_python_is_fun_too_'))
    print(snake_to_camel('_python_is_fun_too_'))
    print(snake_to_camel('_python_is_fun_too_'))
    print(snake_to_camel('_python_is_fun_too_'))
    print(snake_to_camel('_python_is_fun_too_'))
    print(snake_to_camel('_python_is_fun_too_'))
    print(snake_to_camel('_python_is_fun_too_'))
    print(snake_to_camel('_python_is_fun_too_'))
    print(snake_to_camel('_python_is_fun_too_'))
    print(snake_to_camel('_python_is_fun_too_'))
    print(snake_to_camel('_python_is_fun_too_'))
    print(snake_to_camel('_python_is_fun_too_'))
    print(snake_to_camel('_python_is_fun_too_'))
    print(snake_to_camel('_python_is_fun_too_'))
    print(snake_to_camel('_python_is_fun_too_'))
    print(snake_to_camel('_python_is_fun_too_'))
    print(snake_to_camel('_python_is_fun_too_'))
    print(snake_to_camel('_python_is_fun_too_'))
    print(snake_to_camel('_python_is_fun_too_'))
    print(snake_to_camel('_python_is_fun_too_'))
    print(snake_to_camel('_python_is_fun_too_'))
    print(snake_to_camel('_python_is_fun_too_'))
    print(snake_to_camel('_python_is_fun_too_'))
    print(snake_to_camel('_python_is_fun_too_'))
    print(snake_to_camel('_python_is_fun_too_