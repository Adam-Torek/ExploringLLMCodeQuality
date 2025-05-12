"""
Write a function to check if a string represents an integer or not.
assert check_integer("python")==False
"""
def check_integer(string):
    """
    :param string: string to check if it represents an integer
    :return: True if the string represents an integer, False otherwise
    """
    try:
        int(string)
        return True
    except ValueError:
        return False

assert check_integer("python")==False
assert check_integer("123")==True
assert check_integer("1234567890")==True
assert check_integer("12345678901234567890")==True
assert check_integer("123e45")==False
assert check_integer("123.45")==False
assert check_integer("123.0")==False
assert check_integer("123.")==False
assert check_integer("123e+45")==False
assert check_integer("123e-45")==False
assert check_integer("123.0e+45")==False
assert check_integer("123.0e-45")==False
assert check_integer("123.0e+0")==False
assert check_integer("123.0e-0")==False
assert check_integer("123.0e+45.0")==False
assert check_integer("123.0e-45.0")==False
assert check_integer("123.0e+45.0123")==False
assert check_integer("123.0e-45.0123")==False
assert check_integer("123.0e+45.0123e+45")==False
assert check_integer("123.0e-45.0123e-45")==False
assert check_integer("123.0e+45.0123e+45.0")==False
assert check_integer("123.0e-45.0123e-45.0")==False
assert check_integer("123.0e+45.0123e+45.0123")==False
assert check_integer("123.0e-45.0123e-45.0123")==False
assert check_integer("123.0e+45.0123e+45.0123e+45")==False
assert check_integer("123.0e-45.0123e-45.0123e-45")==False
assert check_integer("123.0e+45.0123e+45.0123e+45.0")==False
assert check_integer("123.0e-45.0123e-45.0123e-45.0")==False
assert check_integer("123.0e+45.0123e+45.0123e+45.0123")==False
assert check_integer("123.0e-45.0123e-45.0123e-45.0123")==False
assert check_integer("123.0e+45.0123e+45.0123e+45.0123e+45")==False
assert check_integer("123.0e-45.0123e-45.0123e-45.0123e-45")==False
assert check_integer("123.0e+45.0123e+45.0123e+45.0123e+45.0")==False
assert check_integer("123.0e-45.0123e-45.0123e-45.0123e-45.0")==False
assert check_integer("123.0e+45.0123e+45