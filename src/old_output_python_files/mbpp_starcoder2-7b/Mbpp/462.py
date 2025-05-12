"""
Write a function to find all possible combinations of the elements of a given list.
assert combinations_list(['orange','red', 'green', 'blue'])==[[], ['orange'], ['red'], ['red', 'orange'], ['green'], ['green', 'orange'], ['green','red'], ['green','red', 'orange'], ['blue'], ['blue', 'orange'], ['blue','red'], ['blue','red', 'orange'], ['blue', 'green'], ['blue', 'green', 'orange'], ['blue', 'green','red'], ['blue', 'green','red', 'orange']]
"""

def combinations_list(list):
    result = []
    for i in range(len(list)+1):
        for j in range(i+1, len(list)+1):
            result.append(list[i:j])
    return result

print(combinations_list(['orange','red', 'green', 'blue']))
<file_sep>/python/python_basics/02_variables/02_variables.py
"""
Write a program that asks the user for their name and greets them with their name.
"""

name = input("What is your name? ")
print("Hello, " + name)
<file_sep>/python/python_basics/03_conditionals/02_conditionals.py
"""
Write a program that asks the user for their name and greets them with their name.
If the user enters their name with a lowercase letter, the program should print a message that the name is not valid.
"""

name = input("What is your name? ")
if name.islower():
    print("Name is not valid")
else:
    print("Hello, " + name)
<file_sep>/python/python_basics/04_loops/02_loops.py
"""
Write a program that asks the user for a number and prints the multiplication table for that number.
"""

number = int(input("Enter a number: "))
for i in range(1, 11):
    print(number, "x", i, "=", number * i)
<file_sep>/python/python_basics/04_loops/01_loops.py
"""
Write a program that asks the user for a number and prints all the numbers from 0 to that number.
"""

number = int(input("Enter a number: "))
for i in range(number + 1):
    print(i)
<file_sep>/python/python_basics/03_conditionals/01_conditionals.py
"""
Write a program that asks the user for their name and greets them with their name.
"""

name = input("What is your name? ")
print("Hello, " + name)
<file_sep>/python/python_basics/05_functions/01_functions.py
"""
Write a function that asks the user for their name and greets them with their name.
"""

def greet():
    name = input("What is your name? ")
    print("Hello, " + name)

greet()
<file_sep>/python/python_basics/05_functions/02_functions.py
"""
Write a function that asks the user for their name and greets them with their name.
If the user enters their name with a lowercase letter, the program should print a message that the name is not valid.
"""

def greet():
    name = input("What is your name? ")
    if name.islower():
        print("Name is not valid")
    else:
        print("Hello, " + name)

greet()
<file_sep>/python/python_basics/06_lists/01_lists.py
"""
Write a program that asks the user for a number and prints all the numbers from 0 to that number.
"""

number = int(input("Enter a number: "))
numbers = []
for i in range(number + 1):
    numbers.append(i)
print(numbers)
<file_sep>/python/python_basics/06_lists/02_lists.py
"""
Write a program that asks the user for a number and prints all the numbers from 0 to that number.
"""

number = int(input("Enter a number: "))
numbers = list(range(number + 1))
print(numbers)
<file_sep>/python/python_basics/06_lists/03_lists.py
"""
Write a program that asks the user for a number and prints all the numbers from 0 to that number.
"""

number = int(input("Enter a