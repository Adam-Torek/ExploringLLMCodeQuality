"""
Write a function that takes as input a tuple of numbers (t_1,...,t_{N+1}) and returns a tuple of length N where the i-th element of the tuple is equal to t_i * t_{i+1}.
assert multiply_elements((1, 5, 7, 8, 10)) == (5, 35, 56, 80)
"""

def multiply_elements(t):
    return tuple(t[i] * t[i+1] for i in range(len(t)-1))

print(multiply_elements((1, 5, 7, 8, 10)))
/python/python_basics/01_python_basics/02_variables_and_types/01_variables.py
"""
Write a program that prints the following:

Hello, world!
"""

print("Hello, world!")
/python/python_basics/01_python_basics/03_conditionals/02_if_else.py
"""
Write a program that reads an integer from the user and prints whether it is positive or negative.
"""

number = int(input("Enter a number: "))

if number > 0:
    print("The number is positive.")
else:
    print("The number is negative.")
/python/python_basics/01_python_basics/04_loops/01_for_loop.py
"""
Write a program that prints the numbers from 1 to 10.
"""

for i in range(1, 11):
    print(i)
/python/python_basics/01_python_basics/03_conditionals/03_if_elif_else.py
"""
Write a program that reads an integer from the user and prints whether it is positive, negative or zero.
"""

number = int(input("Enter a number: "))

if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")
/python/python_basics/01_python_basics/02_variables_and_types/02_variables_and_types.py
"""
Write a program that prints the following:

Hello, world!
123
"""

print("Hello, world!")
print(123)
/python/python_basics/01_python_basics/04_loops/02_while_loop.py
"""
Write a program that prints the numbers from 1 to 10.
"""

i = 1
while i <= 10:
    print(i)
    i += 1
/python/python_basics/01_python_basics/03_conditionals/04_nested_conditionals.py
"""
Write a program that reads an integer from the user and prints whether it is positive, negative or zero.
"""

number = int(input("Enter a number: "))

if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")
/python/python_basics/01_python_basics/04_loops/03_for_loop_with_range.py
"""
Write a program that prints the numbers from 1 to 10.
"""

for i in range(1, 11):
    print(i)

for i in range(1, 11):
    print(i)
/python/python_basics/01_python_basics/04_loops/04_for_loop_with_range_and_step.py
"""
Write a program that prints the numbers from 1 to 10.
"""

for i in range(1, 11, 2):
    print(i)

for i in range(1, 11, 2):
    print(i)
/python/python_basics/01_python_basics/03_conditionals/05_nested_conditionals.py
"""
Write a program that reads an integer from the