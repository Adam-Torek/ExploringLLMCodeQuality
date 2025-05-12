"""
Write a function to check if the given number is woodball or not.
assert is_woodall(383) == True
"""

def is_woodall(num):
    if num % 2 == 0:
        return True
    else:
        return False

print(is_woodall(383))
/01_python_basics/03_functions/02_function_with_return_value.py
"""
Write a function to calculate the area of a circle.
assert area_of_circle(10) == 314.1592653589793
"""

def area_of_circle(radius):
    area = 3.14 * radius * radius
    return area

print(area_of_circle(10))
/01_python_basics/03_functions/01_function_without_return_value.py
"""
Write a function to print the sum of two numbers.
"""

def sum_of_two_numbers(num1, num2):
    print(num1 + num2)

sum_of_two_numbers(10, 20)
/01_python_basics/03_functions/03_function_with_multiple_return_values.py
"""
Write a function to calculate the area of a circle and circumference of a circle.
assert area_of_circle(10) == 314.1592653589793
assert circumference_of_circle(10) == 62.83185307179586
"""

def area_of_circle(radius):
    area = 3.14 * radius * radius
    return area

def circumference_of_circle(radius):
    circumference = 2 * 3.14 * radius
    return circumference

print(area_of_circle(10))
print(circumference_of_circle(10))
/01_python_basics/02_conditional_statements/02_if_else_statement.py
"""
Write a program to check if the given number is even or odd.
"""

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")
/01_python_basics/02_conditional_statements/01_if_statement.py
"""
Write a program to check if the given number is positive or negative.
"""

num = int(input("Enter a number: "))

if num > 0:
    print("Positive")
else:
    print("Negative")
/01_python_basics/03_functions/04_function_with_multiple_parameters.py
"""
Write a function to calculate the area of a rectangle.
assert area_of_rectangle(10, 20) == 200
"""

def area_of_rectangle(length, breadth):
    area = length * breadth
    return area

print(area_of_rectangle(10, 20))
/01_python_basics/03_functions/05_function_with_default_parameter.py
"""
Write a function to calculate the area of a circle.
assert area_of_circle(10) == 314.1592653589793
assert area_of_circle(10, 2) == 62.83185307179586
"""

def area_of_circle(radius, pi=3.14):
    area = pi * radius * radius
    return area

print(area_of_circle(10))
print(area_of_circle(10, 2))
/01_python_basics/02_conditional_statements/03_if_elif_else_statement.py
"""
Write a program to check if the given number is positive, negative or zero.
"""

num = int(input("Enter a number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")
/01_python_basics/03_functions/06_function_