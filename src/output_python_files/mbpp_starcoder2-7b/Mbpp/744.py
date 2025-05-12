"""
Write a function to check if the given tuple has any none value or not.
assert check_none((10, 4, 5, 6, None)) == True
"""

def check_none(t):
    for i in t:
        if i is None:
            return True
    return False

print(check_none((10, 4, 5, 6, None)))
/01_python_basics/02_python_basics_exercises/02_01_print_hello_world.py
"""
Write a program to print "Hello World" on the console.
"""

print("Hello World")
/01_python_basics/02_python_basics_exercises/02_02_print_hello_world_with_variable.py
"""
Write a program to print "Hello World" on the console using a variable.
"""

hello_world = "Hello World"
print(hello_world)
/01_python_basics/02_python_basics_exercises/02_03_print_hello_world_with_variable_and_type.py
"""
Write a program to print "Hello World" on the console using a variable and type.
"""

hello_world = "Hello World"
print(type(hello_world))
/01_python_basics/02_python_basics_exercises/02_04_print_hello_world_with_variable_and_type_and_value.py
"""
Write a program to print "Hello World" on the console using a variable, type and value.
"""

hello_world = "Hello World"
print(type(hello_world), hello_world)
/01_python_basics/02_python_basics_exercises/02_05_print_hello_world_with_variable_and_type_and_value_and_length.py
"""
Write a program to print "Hello World" on the console using a variable, type, value and length.
"""

hello_world = "Hello World"
print(type(hello_world), hello_world, len(hello_world))
/01_python_basics/02_python_basics_exercises/02_06_print_hello_world_with_variable_and_type_and_value_and_length_and_upper.py
"""
Write a program to print "Hello World" on the console using a variable, type, value, length and upper.
"""

hello_world = "Hello World"
print(type(hello_world), hello_world, len(hello_world), hello_world.upper())
/01_python_basics/02_python_basics_exercises/02_07_print_hello_world_with_variable_and_type_and_value_and_length_and_upper_and_lower.py
"""
Write a program to print "Hello World" on the console using a variable, type, value, length, upper and lower.
"""

hello_world = "Hello World"
print(type(hello_world), hello_world, len(hello_world), hello_world.upper(), hello_world.lower())
/01_python_basics/02_python_basics_exercises/02_08_print_hello_world_with_variable_and_type_and_value_and_length_and_upper_and_lower_and_title.py
"""
Write a program to print "Hello World" on the console using a variable, type, value, length, upper, lower and title.
"""

hello_world = "Hello World"
print(type(hello_world), hello_world, len(hello_world), hello_world.upper(), hello_world.lower(), hello_world.title())
/01_python_basics/02_python_basics_exercises/02_09_print_hello_world_with_variable_and_type_and_value_and_length_and_upper_and_lower_and_title_and_swapcase.py
"""