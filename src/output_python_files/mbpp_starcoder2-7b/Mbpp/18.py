"""
Write a function to remove characters from the first string which are present in the second string.
assert remove_dirty_chars("probasscurve", "pros") == 'bacuve'
"""

def remove_dirty_chars(string1, string2):
    result = ""
    for char in string1:
        if char not in string2:
            result += char
    return result

print(remove_dirty_chars("probasscurve", "pros"))
/python/python_basics/03_functions/01_function_basics.py
"""
Functions are a way to group code together and reuse it.

Functions are defined using the def keyword.

def function_name(parameters):
    # code goes here

Functions can take parameters, which are variables that are passed into the function.

Functions can return values, which are the values that are returned from the function.

Functions can be called using the function name and parameters.

def function_name(parameters):
    # code goes here
    return value

function_name(parameters)

"""

def add(a, b):
    return a + b

print(add(1, 2))

def subtract(a, b):
    return a - b

print(subtract(1, 2))

def multiply(a, b):
    return a * b

print(multiply(1, 2))

def divide(a, b):
    return a / b

print(divide(1, 2))

def remainder(a, b):
    return a % b

print(remainder(1, 2))

def power(a, b):
    return a ** b

print(power(1, 2))

def square_root(a):
    return a ** 0.5

print(square_root(4))

def cube_root(a):
    return a ** (1/3)

print(cube_root(27))

def absolute_value(a):
    if a < 0:
        return -a
    else:
        return a

print(absolute_value(-1))

def max_of_two(a, b):
    if a > b:
        return a
    else:
        return b

print(max_of_two(1, 2))

def max_of_three(a, b, c):
    return max_of_two(a, max_of_two(b, c))

print(max_of_three(1, 2, 3))

def is_even(a):
    if a % 2 == 0:
        return True
    else:
        return False

print(is_even(1))

def is_odd(a):
    return not is_even(a)

print(is_odd(1))

def is_divisible_by(a, b):
    if a % b == 0:
        return True
    else:
        return False

print(is_divisible_by(1, 2))

def is_divisible_by_both(a, b, c):
    return is_divisible_by(a, b) and is_divisible_by(a, c)

print(is_divisible_by_both(1, 2, 3))

def is_divisible_by_either(a, b, c):
    return is_divisible_by(a, b) or is_divisible_by(a, c)

print(is_divisible_by_either(1, 2, 3))

def is_divisible_by_all(a, b, c):
    return is_divisible_by(a, b) and is_divisible_by(a, c) and is_divisible_by(b, c)

print(is_divisible_by_all(1, 2, 3))

def is_divisible_by_none(a, b, c):
    return not is_divisible_by_all(a, b, c)

print(is_divisible_by_none(1, 2, 3))

def is_divisible_by_any(a, b, c):
    return is_divisible_by(a, b) or is_divisible_by(a, c) or is_divisible_by(b, c)

print(is_divisible_by_any(1, 2