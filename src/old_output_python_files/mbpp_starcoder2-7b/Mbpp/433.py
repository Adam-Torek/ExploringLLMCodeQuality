"""
Write a function to check whether the entered number is greater than the elements of the given array.
assert check_greater([1, 2, 3, 4, 5], 4) == False
"""

def check_greater(arr, num):
    for i in arr:
        if i > num:
            return True
    return False

print(check_greater([1, 2, 3, 4, 5], 4))
<file_sep>/python/python_basics/01_variables/01_variables.py
"""
Write a program that asks the user to enter a number.
Print the number entered by the user.
"""

num = input("Enter a number: ")
print(num)
<file_sep>/python/python_basics/03_conditionals/01_if_else.py
"""
Write a program that asks the user to enter a number.
If the number is greater than 10, print "Greater than 10".
If the number is less than 10, print "Less than 10".
If the number is equal to 10, print "Equal to 10".
"""

num = int(input("Enter a number: "))

if num > 10:
    print("Greater than 10")
elif num < 10:
    print("Less than 10")
else:
    print("Equal to 10")
<file_sep>/python/python_basics/04_loops/01_for_loop.py
"""
Write a program that prints the numbers from 1 to 10.
"""

for i in range(1, 11):
    print(i)
<file_sep>/python/python_basics/04_loops/02_while_loop.py
"""
Write a program that prints the numbers from 1 to 10.
"""

i = 1
while i <= 10:
    print(i)
    i += 1
<file_sep>/python/python_basics/02_functions/01_functions.py
"""
Write a function that prints "Hello World".
"""

def hello_world():
    print("Hello World")

hello_world()
<file_sep>/python/python_basics/02_functions/02_functions_with_parameters.py
"""
Write a function that prints the name of the user.
"""

def print_name(name):
    print(name)

print_name("John")
<file_sep>/python/python_basics/03_conditionals/02_if_elif_else.py
"""
Write a program that asks the user to enter a number.
If the number is greater than 10, print "Greater than 10".
If the number is less than 10, print "Less than 10".
If the number is equal to 10, print "Equal to 10".
"""

num = int(input("Enter a number: "))

if num > 10:
    print("Greater than 10")
elif num < 10:
    print("Less than 10")
else:
    print("Equal to 10")
<file_sep>/python/python_basics/02_functions/03_functions_with_return.py
"""
Write a function that returns the name of the user.
"""

def get_name():
    return "John"

print(get_name())
<file_sep>/python/python_basics/04_loops/03_for_loop_with_range.py
"""
Write a program that prints the numbers from 1 to 10.
"""

for i in range(1, 11):
    print(i)

for i in range(1, 11):
    print(i, end=" ")
<file_sep>/python/python_basics/02_functions/04_functions_with_parameters_and_return.py
"""
Write a function that returns the name of the user.
"""

def get_name(name):
    return name

print(get_name("John"))
<file_sep>/python/python_basics/04_loops/04_for_loop_with_list.py
"""
Write a program that prints the elements of the given list.
"""

arr = [1, 2, 3, 4, 5]

for i in arr:
    print(i)
<file_sep>/python/python_basics/04_loops/05_for