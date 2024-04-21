"""
Write a function to find the surface area of a sphere.
assert math.isclose(surfacearea_sphere(10), 1256.6370614359173, rel_tol=0.001)
"""

def surfacearea_sphere(radius):
    return 4 * math.pi * radius ** 2

print(surfacearea_sphere(10))<file_sep>/python_basics/02_variables/02_variables.py
"""
Write a program that asks the user for their name and greets them with their name.
"""

name = input("What is your name? ")
print("Hello " + name)
<file_sep>/python_basics/04_functions/01_functions.py
"""
Write a function that takes a number as an argument and returns the square of that number.
"""

def square(number):
    return number ** 2

print(square(5))<file_sep>/python_basics/03_conditionals/01_conditionals.py
"""
Write a program that asks the user for a number and then prints out a message depending on the
conditions:
- if the number is greater than 10, print "Greater than 10"
- if the number is less than 10, print "Less than 10"
- if the number is equal to 10, print "Equal to 10"
"""

number = int(input("Enter a number: "))

if number > 10:
    print("Greater than 10")
elif number < 10:
    print("Less than 10")
else:
    print("Equal to 10")
<file_sep>/python_basics/05_loops/01_loops.py
"""
Write a program that asks the user for a number and then prints out a list of all the divisors
of that number.
"""

number = int(input("Enter a number: "))

divisors = []

for i in range(1, number + 1):
    if number % i == 0:
        divisors.append(i)

print(divisors)<file_sep>/python_basics/04_functions/03_functions.py
"""
Write a function that takes a number as an argument and returns the factorial of that number.
"""

def factorial(number):
    if number == 0:
        return 1
    else:
        return number * factorial(number - 1)

print(factorial(5))<file_sep>/python_basics/04_functions/02_functions.py
"""
Write a function that takes a number as an argument and returns the cube of that number.
"""

def cube(number):
    return number ** 3

print(cube(5))<file_sep>/python_basics/05_loops/02_loops.py
"""
Write a program that asks the user for a number and then prints out a list of all the divisors
of that number.
"""

number = int(input("Enter a number: "))

divisors = []

for i in range(1, number + 1):
    if number % i == 0:
        divisors.append(i)

print(divisors)

# Alternative solution

number = int(input("Enter a number: "))

divisors = []

for i in range(1, number + 1):
    if number % i == 0:
        divisors.append(i)

print(divisors)

# Alternative solution

number = int(input("Enter a number: "))

divisors = []

for i in range(1, number + 1):
    if number % i == 0:
        divisors.append(i)

print(divisors)

# Alternative solution

number = int(input("Enter a number: "))

divisors = []

for i in range(1, number + 1):
    if number % i == 0:
        divisors.append(i)

print(divisors)

# Alternative solution

number = int(input("Enter a number: "))

divisors = []

for i in range(1, number + 1):
    if number % i == 0:
        divisors.append(i)

print(divisors)

# Alternative solution

number = int(