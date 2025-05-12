"""
Write a function to count lists within a list. The function should return a dictionary where every list is converted to a tuple and the value of such tuple is the number of its occurencies in the original list.
assert unique_sublists([[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]] )=={(1, 3): 2, (5, 7): 2, (13, 15, 17): 1, (9, 11): 1}
"""

def unique_sublists(lst):
    d = {}
    for i in lst:
        d[tuple(i)] = lst.count(i)
    return d

print(unique_sublists([[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]]))
<file_sep>/Python/Python_Basics/01_Python_Basics/02_Python_Basics_Exercises/02_01_Python_Basics_Exercises.py
"""
Write a program that asks the user for their name and greets them with their name.
"""

name = input("What is your name? ")
print("Hello, " + name + "!")
<file_sep>/Python/Python_Basics/01_Python_Basics/02_Python_Basics_Exercises/02_04_Python_Basics_Exercises.py
"""
Write a program that asks the user for their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.
"""

name = input("What is your name? ")
age = int(input("How old are you? "))
year = 2019
print(name + ", you will be 100 years old in the year " + str(year + (100 - age)))
<file_sep>/Python/Python_Basics/01_Python_Basics/02_Python_Basics_Exercises/02_05_Python_Basics_Exercises.py
"""
Write a program that asks the user for a number and prints out a list of all the divisors of that number. (If you don’t know what a divisor is, it is a number that divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)
"""

number = int(input("Enter a number: "))
divisors = []
for i in range(1, number + 1):
    if number % i == 0:
        divisors.append(i)
print(divisors)
<file_sep>/Python/Python_Basics/01_Python_Basics/02_Python_Basics_Exercises/02_03_Python_Basics_Exercises.py
"""
Write a program that asks the user for a number and then prints out a list of all the divisors of that number. (If you don’t know what a divisor is, it is a number that divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)
"""

number = int(input("Enter a number: "))
divisors = []
for i in range(1, number + 1):
    if number % i == 0:
        divisors.append(i)
print(divisors)
<file_sep>/Python/Python_Basics/01_Python_Basics/02_Python_Basics_Exercises/02_02_Python_Basics_Exercises.py
"""
Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?
"""

number = int(input("Enter a number: "))
if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")
<file_sep>/Python/Python_Basics/01_Python_Basics/02_Python_Basics_Exercises/02_06_Python_Basics_Exercises.py
"""
Write a program that asks the user for a string and prints out whether this string is a palindrome or not. (A palindrome is a string that reads the