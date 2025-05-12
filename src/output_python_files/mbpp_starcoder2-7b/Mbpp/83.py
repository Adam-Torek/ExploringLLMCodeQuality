"""
Write a python function to find the character made by adding the ASCII value of all the characters of the given string modulo 26.
assert get_Char("abc") == "f"
"""

def get_Char(string):
    sum = 0
    for i in string:
        sum += ord(i)
    return chr(sum % 26 + 97)

print(get_Char("abc"))
/Python/Python_Basics/02_Variables/02_Variables.py
"""
Write a python program to print the sum of two numbers.
"""

a = 10
b = 20

print(a + b)
/Python/Python_Basics/05_Operators/05_Operators.py
"""
Write a python program to print the result of the following operations.
"""

a = 10
b = 20

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a // b)
print(a ** b)
/Python/Python_Basics/03_Data_Types/03_Data_Types.py
"""
Write a python program to print the data type of the following variables.
"""

a = 10
b = 10.5
c = "Hello"
d = True
e = 1 + 2j

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
/Python/Python_Basics/04_Input_Output/04_Input_Output.py
"""
Write a python program to print the sum of two numbers entered by the user.
"""

a = int(input("Enter a number: "))
b = int(input("Enter another number: "))

print(a + b)
/Python/Python_Basics/06_Conditional_Statements/06_Conditional_Statements.py
"""
Write a python program to print the result of the following operations.
"""

a = 10
b = 20

if a > b:
    print("a is greater than b")
elif a < b:
    print("a is less than b")
else:
    print("a is equal to b")
/Python/Python_Basics/07_Loops/07_Loops.py
"""
Write a python program to print the sum of the first 10 natural numbers.
"""

sum = 0
for i in range(1, 11):
    sum += i

print(sum)
/Python/Python_Basics/08_Functions/08_Functions.py
"""
Write a python function to print the sum of the first 10 natural numbers.
"""

def sum_of_first_10_natural_numbers():
    sum = 0
    for i in range(1, 11):
        sum += i
    return sum

print(sum_of_first_10_natural_numbers())
/Python/Python_Basics/09_Lists/09_Lists.py
"""
Write a python program to print the sum of the first 10 natural numbers.
"""

def sum_of_first_10_natural_numbers():
    sum = 0
    for i in range(1, 11):
        sum += i
    return sum

print(sum_of_first_10_natural_numbers())

"""
Write a python program to print the sum of the first 10 natural numbers.
"""

def sum_of_first_10_natural_numbers():
    sum = 0
    for i in range(1, 11):
        sum += i
    return sum

print(sum_of_first_10_natural_numbers())

"""
Write a python program to print the sum of the first 10 natural numbers.
"""

def sum_of_first_10_natural_numbers():
    sum = 0
    for i in range(1, 11):
        sum += i
    return sum

print(sum_of_first_10_natural_numbers())

"""
Write a python program to print the sum of the first 10 natural numbers.
"""

def sum_of_first_10