"""
Write a function to sort a given list of strings of numbers numerically. https://www.geeksforgeeks.org/python-sort-numeric-strings-in-a-list/
assert sort_numeric_strings( ['4','12','45','7','0','100','200','-12','-500'])==[-500, -12, 0, 4, 7, 12, 45, 100, 200]
"""

def sort_numeric_strings(lst):
    return sorted(lst, key=lambda x: int(x))

assert sort_numeric_strings( ['4','12','45','7','0','100','200','-12','-500'])==[-500, -12, 0, 4, 7, 12, 45, 100, 200]
<file_sep>/python/python_basics/02_variables.py
"""
Write a program that asks the user to enter a number.
If the number is less than 10, print "Small".
If the number is greater than or equal to 10, print "Large".
"""

number = int(input("Enter a number: "))

if number < 10:
    print("Small")
else:
    print("Large")
<file_sep>/python/python_basics/03_variables.py
"""
Write a program that asks the user to enter a number.
If the number is less than 10, print "Small".
If the number is greater than or equal to 10, print "Large".
If the number is equal to 10, print "Medium".
"""

number = int(input("Enter a number: "))

if number < 10:
    print("Small")
elif number > 10:
    print("Large")
else:
    print("Medium")
<file_sep>/python/python_basics/01_variables.py
"""
Write a program that asks the user to enter a number.
If the number is less than 10, print "Small".
If the number is greater than or equal to 10, print "Large".
"""

number = int(input("Enter a number: "))

if number < 10:
    print("Small")

if number >= 10:
    print("Large")
<file_sep>/python/python_basics/04_variables.py
"""
Write a program that asks the user to enter a number.
If the number is less than 10, print "Small".
If the number is greater than or equal to 10, print "Large".
If the number is equal to 10, print "Medium".
If the number is less than 0, print "Negative".
If the number is greater than 0, print "Positive".
"""

number = int(input("Enter a number: "))

if number < 10:
    print("Small")
elif number > 10:
    print("Large")
else:
    print("Medium")

if number < 0:
    print("Negative")
elif number > 0:
    print("Positive")
<file_sep>/python/python_basics/05_variables.py
"""
Write a program that asks the user to enter a number.
If the number is less than 10, print "Small".
If the number is greater than or equal to 10, print "Large".
If the number is equal to 10, print "Medium".
If the number is less than 0, print "Negative".
If the number is greater than 0, print "Positive".
If the number is equal to 0, print "Zero".
"""

number = int(input("Enter a number: "))

if number < 10:
    print("Small")
elif number > 10:
    print("Large")
else:
    print("Medium")

if number < 0:
    print("Negative")
elif number > 0:
    print("Positive")
else:
    print("Zero")
<file_sep>/python/python_basics/06_variables.py
"""
Write a program that asks the user to enter a number.
If the number is less than 10, print "Small".
If the number is greater than or equal to 10, print "Large".
If the number is equal to 10, print "Medium".
If the number is less than 0, print