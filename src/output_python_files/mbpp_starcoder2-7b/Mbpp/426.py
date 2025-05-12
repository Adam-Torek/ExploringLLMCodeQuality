"""
Write a function to filter odd numbers.
assert filter_oddnumbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])==[1,3,5,7,9]
"""

def filter_oddnumbers(numbers):
    return [x for x in numbers if x % 2 == 1]

print(filter_oddnumbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
/python/python_basics/01_variables/02_variables.py
"""
Write a program that asks the user for their name and greets them with their name.
"""

name = input("What is your name? ")
print("Hello " + name)
/python/python_basics/02_conditionals/02_conditionals.py
"""
Write a program that asks the user for their name and greets them with their name.
If the user enters their name as "Bob", print "Hello Bob".
If their name is "Alice", print "Hello Alice".
If their name is "Eve", print "Hello Eve".
If their name is something else, print "Hello unknown".
"""

name = input("What is your name? ")

if name == "Bob":
    print("Hello Bob")
elif name == "Alice":
    print("Hello Alice")
elif name == "Eve":
    print("Hello Eve")
else:
    print("Hello unknown")
/python/python_basics/02_conditionals/01_conditionals.py
"""
Write a program that asks the user for their name and greets them with their name.
If the user enters their name as "Bob", print "Hello Bob".
If their name is "Alice", print "Hello Alice".
If their name is "Eve", print "Hello Eve".
If their name is something else, print "Hello unknown".
"""

name = input("What is your name? ")

if name == "Bob":
    print("Hello Bob")
elif name == "Alice":
    print("Hello Alice")
elif name == "Eve":
    print("Hello Eve")
else:
    print("Hello unknown")
/python/python_basics/03_loops/01_loops.py
"""
Write a program that asks the user for their name and greets them with their name.
If the user enters their name as "Bob", print "Hello Bob".
If their name is "Alice", print "Hello Alice".
If their name is "Eve", print "Hello Eve".
If their name is something else, print "Hello unknown".
"""

name = input("What is your name? ")

while name!= "Bob" and name!= "Alice" and name!= "Eve":
    name = input("What is your name? ")

if name == "Bob":
    print("Hello Bob")
elif name == "Alice":
    print("Hello Alice")
elif name == "Eve":
    print("Hello Eve")
else:
    print("Hello unknown")
/python/python_basics/04_functions/01_functions.py
"""
Write a function that takes a list of numbers and returns the largest number in the list.
assert largest([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])==10
"""

def largest(numbers):
    return max(numbers)

print(largest([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
/python/python_basics/04_functions/02_functions.py
"""
Write a function that takes a list of numbers and returns the smallest number in the list.
assert smallest([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])==1
"""

def smallest(numbers):
    return min(numbers)

print(smallest([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
/python/python_basics/04_functions/