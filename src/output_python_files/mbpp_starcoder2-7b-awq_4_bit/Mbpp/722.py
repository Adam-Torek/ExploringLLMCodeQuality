"""
The input is given as - a dictionary with a student name as a key and a tuple of float (student_height, student_weight) as a value, - minimal height, - minimal weight. Write a function to filter students that have height and weight above the minimum.
assert filter_data({'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)},6.0,70)=={'Cierra Vega': (6.2, 70)}
"""

def filter_data(data, min_height, min_weight):
    return {k:v for k,v in data.items() if v[0] > min_height and v[1] > min_weight}

print(filter_data({'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)},6.0,70))
/week_01/day_02/01_print_params.py
"""
Write a function that prints the parameters of a function.
"""

def print_params(func):
    print(func.__code__.co_varnames)

def add(a, b):
    return a + b

print_params(add)
/week_01/day_02/02_print_params_2.py
"""
Write a function that prints the parameters of a function.
"""

def print_params(func):
    print(func.__code__.co_varnames)

def add(a, b):
    return a + b

print_params(add)

def sub(a, b):
    return a - b

print_params(sub)
/week_01/day_02/03_print_params_3.py
"""
Write a function that prints the parameters of a function.
"""

def print_params(func):
    print(func.__code__.co_varnames)

def add(a, b):
    return a + b

print_params(add)

def sub(a, b):
    return a - b

print_params(sub)

def mult(a, b):
    return a * b

print_params(mult)
/week_01/day_02/04_print_params_4.py
"""
Write a function that prints the parameters of a function.
"""

def print_params(func):
    print(func.__code__.co_varnames)

def add(a, b):
    return a + b

print_params(add)

def sub(a, b):
    return a - b

print_params(sub)

def mult(a, b):
    return a * b

print_params(mult)

def div(a, b):
    return a / b

print_params(div)
/week_01/day_02/05_print_params_5.py
"""
Write a function that prints the parameters of a function.
"""

def print_params(func):
    print(func.__code__.co_varnames)

def add(a, b):
    return a + b

print_params(add)

def sub(a, b):
    return a - b

print_params(sub)

def mult(a, b):
    return a * b

print_params(mult)

def div(a, b):
    return a / b

print_params(div)

def mod(a, b):
    return a % b

print_params(mod)
/week_01/day_02/06_print_params_6.py
"""
Write a function that prints the parameters of a function.
"""

def print_params(func):
    print(func.__code__.co_varnames)

def add(a, b):
    return a + b

print_params(add)

def sub(a, b):
    return a - b

print_params(sub)

def mult(a, b):
    return a