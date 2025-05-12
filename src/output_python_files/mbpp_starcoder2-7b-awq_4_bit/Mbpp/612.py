"""
Write a python function which takes a list of lists, where each sublist has two elements, and returns a list of two lists where the first list has the first element of each sublist and the second one has the second.
assert merge([['x', 'y'], ['a', 'b'], ['m', 'n']]) == [['x', 'a','m'], ['y', 'b', 'n']]
"""

def merge(list_of_lists):
    return [list(x) for x in zip(*list_of_lists)]

print(merge([['x', 'y'], ['a', 'b'], ['m', 'n']]))
/python/python_basics/01_variables/01_variables.py
"""
Write a python program which prints the following:

Hello World!
"""

print("Hello World!")
/python/python_basics/02_data_types/01_data_types.py
"""
Write a python program which prints the following:

Hello World!
123
"""

print("Hello World!")
print(123)
/python/python_basics/03_operators/01_operators.py
"""
Write a python program which prints the following:

Hello World!
123
123
"""

print("Hello World!")
print(123)
print(123)
/python/python_basics/04_functions/01_functions.py
"""
Write a python program which prints the following:

Hello World!
123
123
"""

def print_hello_world():
    print("Hello World!")

def print_number(number):
    print(number)

print_hello_world()
print_number(123)
print_number(123)
/python/python_basics/05_conditionals/01_conditionals.py
"""
Write a python program which prints the following:

Hello World!
123
123
"""

def print_hello_world():
    print("Hello World!")

def print_number(number):
    print(number)

def print_hello_world_if_true(condition):
    if condition:
        print_hello_world()

print_hello_world()
print_number(123)
print_number(123)
print_hello_world_if_true(True)
/python/python_basics/06_loops/01_loops.py
"""
Write a python program which prints the following:

Hello World!
123
123
Hello World!
"""

def print_hello_world():
    print("Hello World!")

def print_number(number):
    print(number)

def print_hello_world_if_true(condition):
    if condition:
        print_hello_world()

print_hello_world()
print_number(123)
print_number(123)
print_hello_world_if_true(True)

def print_hello_world_if_true_loop(condition):
    for i in range(10):
        if condition:
            print_hello_world()

print_hello_world_if_true_loop(True)
/python/python_basics/07_lists/01_lists.py
"""
Write a python program which prints the following:

Hello World!
123
123
Hello World!
Hello World!
Hello World!
Hello World!
Hello World!
Hello World!
Hello World!
"""

def print_hello_world():
    print("Hello World!")

def print_number(number):
    print(number)

def print_hello_world_if_true(condition):
    if condition:
        print_hello_world()

print_hello_world()
print_number(123)
print_number(123)
print_hello_world_if_true(True)

def print_hello_world_if_true_loop(condition):
    for i in range(10):
        if condition:
            print_hello_world()

print_hello_world_if_true_loop(True)

def print_hello_world_if_true_