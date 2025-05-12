"""
Write a function to sort a dictionary by value.
assert sort_counter({'Math':81, 'Physics':83, 'Chemistry':87})==[('Chemistry', 87), ('Physics', 83), ('Math', 81)]
"""

def sort_counter(counter):
    return sorted(counter.items(), key=lambda x: x[1])

print(sort_counter({'Math':81, 'Physics':83, 'Chemistry':87}))
/python/python_basics/01_basics/01_02_variables.py
"""
Write a program that asks the user to enter their name and stores it in a variable.
Then print the following:
Hello, [name]! You just delved into python.
"""

name = input("Enter your name: ")
print("Hello, " + name + "! You just delved into python.")
/python/python_basics/02_functions/02_01_functions.py
"""
Write a function that takes a number as an input and returns the square of that number.
"""

def square(number):
    return number ** 2

print(square(2))
/python/python_basics/01_basics/01_03_operators.py
"""
Write a program that asks the user to enter a number and stores it in a variable.
Then print the following:
The square of the number is [square]
The cube of the number is [cube]
"""

number = int(input("Enter a number: "))
print("The square of the number is " + str(number ** 2))
print("The cube of the number is " + str(number ** 3))
/python/python_basics/01_basics/01_01_hello_world.py
"""
Write a program that prints the following:
Hello, World!
"""

print("Hello, World!")
/python/python_basics/02_functions/02_03_functions.py
"""
Write a function that takes a number as an input and returns the square of that number.
"""

def square(number):
    return number ** 2

print(square(2))

"""
Write a function that takes a number as an input and returns the cube of that number.
"""

def cube(number):
    return number ** 3

print(cube(2))

"""
Write a function that takes two numbers as inputs and returns the sum of those two numbers.
"""

def sum(number1, number2):
    return number1 + number2

print(sum(2, 3))

"""
Write a function that takes two numbers as inputs and returns the difference of those two numbers.
"""

def difference(number1, number2):
    return number1 - number2

print(difference(2, 3))

"""
Write a function that takes two numbers as inputs and returns the product of those two numbers.
"""

def product(number1, number2):
    return number1 * number2

print(product(2, 3))

"""
Write a function that takes two numbers as inputs and returns the quotient of those two numbers.
"""

def quotient(number1, number2):
    return number1 / number2

print(quotient(2, 3))

"""
Write a function that takes two numbers as inputs and returns the remainder of those two numbers.
"""

def remainder(number1, number2):
    return number1 % number2

print(remainder(2, 3))
/python/python_basics/02_functions/02_02_functions.py
"""
Write a function that takes a number as an input and returns the square of that number.
"""

def square(number):
    return number ** 2

print(square(2))

"""
Write a function that takes a number as an input and returns the cube of that number.
"""

def cube(number):
    return number ** 3

print(cube(2))

"""
Write a function that takes two numbers as inputs and returns the sum of those two numbers.
"""

def sum(number1, number2):
    return number1 + number2

print(sum(2, 3))

"""
Write a function that takes two numbers as inputs and returns the difference of those two numbers.
"""

def difference(number1,