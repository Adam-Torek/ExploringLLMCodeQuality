"""
Write a function to check if the given tuple has any none value or not.
assert check_none((10, 4, 5, 6, None)) == True
"""

def check_none(tup):
    for i in tup:
        if i is None:
            return True
    return False

print(check_none((10, 4, 5, 6, None)))
<file_sep>/python_basics/02_variables/02_variables.py
"""
Write a program to print the following output.

Name: <NAME>
Age: 20
"""

name = "<NAME>"
age = 20

print("Name: " + name)
print("Age: " + str(age))
<file_sep>/python_basics/03_operators/01_operators.py
"""
Write a program to print the following output.

Addition: 10 + 5 = 15
Subtraction: 10 - 5 = 5
Multiplication: 10 * 5 = 50
Division: 10 / 5 = 2
"""

print("Addition: 10 + 5 = " + str(10 + 5))
print("Subtraction: 10 - 5 = " + str(10 - 5))
print("Multiplication: 10 * 5 = " + str(10 * 5))
print("Division: 10 / 5 = " + str(10 / 5))
<file_sep>/python_basics/04_conditional_statements/01_conditional_statements.py
"""
Write a program to print the following output.

If the number is positive, print "Positive"
If the number is negative, print "Negative"
If the number is zero, print "Zero"
"""

number = 0

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")
<file_sep>/python_basics/05_loops/01_loops.py
"""
Write a program to print the following output.

Print 1 to 10
Print 10 to 1
"""

for i in range(1, 11):
    print(i)

for i in range(10, 0, -1):
    print(i)
<file_sep>/python_basics/06_functions/01_functions.py
"""
Write a function to print the following output.

Print "Hello World"
"""

def print_hello_world():
    print("Hello World")

print_hello_world()
<file_sep>/python_basics/07_lists/01_lists.py
"""
Write a program to print the following output.

Print the list [1, 2, 3, 4, 5]
Print the list ["Hello", "World"]
Print the list [1, "Hello", 2, "World"]
"""

list1 = [1, 2, 3, 4, 5]
list2 = ["Hello", "World"]
list3 = [1, "Hello", 2, "World"]

print(list1)
print(list2)
print(list3)
<file_sep>/python_basics/08_dictionaries/01_dictionaries.py
"""
Write a program to print the following output.

Print the dictionary {"name": "<NAME>", "age": 20}
Print the dictionary {"name": "<NAME>", "age": 20, "address": "Kathmandu"}
"""

dict1 = {"name": "<NAME>", "age": 20}
dict2 = {"name": "<NAME>", "age": 20, "address": "Kathmandu"}

print(dict1)
print(dict2)
<file_sep>/python_basics/09_tuples/01_tuples.py
"""
Write a program to print the following output.

Print the tuple (1, 2, 3, 4, 5)
Print the tuple ("Hello", "World")
Print the tuple (1, "Hello", 2, "World")
"""

tup1 = (1, 2, 3, 4, 5)
tup2 = ("Hello", "World")
tup3 = (1, "Hello", 2, "World")

print(tup1)
print(tup2)
print(tup3