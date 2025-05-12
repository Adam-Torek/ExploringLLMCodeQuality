"""
Write a function to find the number of elements that occurs before the tuple element in the given tuple.
assert count_first_elements((1, 5, 7, (4, 6), 10) ) == 3
"""

def count_first_elements(tup):
    count = 0
    for i in tup:
        if type(i) == tuple:
            count += 1
        else:
            break
    return count

print(count_first_elements((1, 5, 7, (4, 6), 10)))
<file_sep>/python_basics/01_python_basics/03_variables_and_data_types/03_03_variables_and_data_types.py
"""
Write a program that asks the user to enter a number.
Print the number multiplied by 10.
"""

number = int(input("Enter a number: "))
print(number * 10)
<file_sep>/python_basics/01_python_basics/04_conditional_statements/04_01_conditional_statements.py
"""
Write a program that asks the user to enter a number.
If the number is positive, print "positive".
If the number is negative, print "negative".
If the number is zero, print "zero".
"""

number = int(input("Enter a number: "))
if number > 0:
    print("positive")
elif number < 0:
    print("negative")
else:
    print("zero")
<file_sep>/python_basics/01_python_basics/03_variables_and_data_types/03_02_variables_and_data_types.py
"""
Write a program that asks the user to enter a number.
Print the number divided by 2.
"""

number = int(input("Enter a number: "))
print(number / 2)
<file_sep>/python_basics/01_python_basics/04_conditional_statements/04_02_conditional_statements.py
"""
Write a program that asks the user to enter a number.
If the number is positive, print "positive".
If the number is negative, print "negative".
If the number is zero, print "zero".
"""

number = int(input("Enter a number: "))
if number > 0:
    print("positive")
elif number < 0:
    print("negative")
else:
    print("zero")
<file_sep>/python_basics/01_python_basics/03_variables_and_data_types/03_01_variables_and_data_types.py
"""
Write a program that asks the user to enter a number.
Print the number.
"""

number = int(input("Enter a number: "))
print(number)
<file_sep>/python_basics/01_python_basics/04_conditional_statements/04_03_conditional_statements.py
"""
Write a program that asks the user to enter a number.
If the number is positive, print "positive".
If the number is negative, print "negative".
If the number is zero, print "zero".
"""

number = int(input("Enter a number: "))
if number > 0:
    print("positive")
elif number < 0:
    print("negative")
else:
    print("zero")
<file_sep>/python_basics/01_python_basics/02_functions/02_01_functions.py
"""
Write a function that prints "Hello World!"
"""

def hello_world():
    print("Hello World!")

hello_world()
<file_sep>/python_basics/01_python_basics/02_functions/02_02_functions.py
"""
Write a function that prints "Hello World!"
"""

def hello_world():
    print("Hello World!")

hello_world()
hello_world()
hello_world()
<file_sep>/python_basics/01_python_basics/02_functions/02_03_functions.py
"""
Write a function that prints "Hello World!"
"""

def hello_world():
    print("Hello World!")

hello_world()
hello_world()
hello_world()
hello_world()
hello_world()
hello_world()
hello_world()
hello_world()
hello_world()
hello_world()
<file_sep>/python_basics/01_python_basics/02_functions/02_