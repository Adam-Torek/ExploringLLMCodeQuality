"""
Write a function that takes in two numbers and returns a tuple with the second number and then the first number.
assert swap_numbers(10,20)==(20,10)
"""

def swap_numbers(a,b):
    return (b,a)

print(swap_numbers(10,20))
/01_python_basics/02_variables/01_variables.py
"""
Write a program that prints the following:

Hello, my name is.
"""

name = ""
print("Hello, my name is " + name)
/01_python_basics/03_data_types/02_data_types.py
"""
Write a program that prints the following:

Hello, my name is.
I am 20 years old.
I am 6'2" tall.
"""

name = ""
age = 20
height = 6.2
print("Hello, my name is " + name + ".")
print("I am " + str(age) + " years old.")
print("I am " + str(height) + " tall.")
/01_python_basics/05_functions/01_functions.py
"""
Write a function that takes in a number and returns the square of that number.
assert square(2)==4
"""

def square(num):
    return num**2

print(square(2))
/01_python_basics/04_operators/01_operators.py
"""
Write a program that prints the following:

Hello, my name is.
I am 20 years old.
I am 6'2" tall.
"""

name = ""
age = 20
height = 6.2
print("Hello, my name is " + name + ".")
print("I am " + str(age) + " years old.")
print("I am " + str(height) + " tall.")

print("Hello, my name is " + name + ".")
print("I am " + str(age) + " years old.")
print("I am " + str(height) + " tall.")

print("Hello, my name is " + name + ".")
print("I am " + str(age) + " years old.")
print("I am " + str(height) + " tall.")
/01_python_basics/06_conditionals/01_conditionals.py
"""
Write a function that takes in a number and returns True if the number is greater than 10 and False otherwise.
assert greater_than_ten(11)==True
"""

def greater_than_ten(num):
    if num > 10:
        return True
    else:
        return False

print(greater_than_ten(11))
/01_python_basics/07_lists/01_lists.py
"""
Write a function that takes in a list of numbers and returns the sum of all the numbers.
assert sum_list([1,2,3])==6
"""

def sum_list(nums):
    total = 0
    for num in nums:
        total += num
    return total

print(sum_list([1,2,3]))
/01_python_basics/08_dictionaries/01_dictionaries.py
"""
Write a function that takes in a dictionary and returns the sum of all the values.
assert sum_dict({"a":1,"b":2,"c":3})==6
"""

def sum_dict(nums):
    total = 0
    for num in nums.values():
        total += num
    return total

print(sum_dict({"a":1,"b":2,"c":3}))
/01_python_basics/09_loops/01_loops.py
"""
Write a function that takes in a list of numbers and returns the sum of all the numbers.
assert sum_list([1,2,3])==6
"""

def sum_list(nums):
    total = 0
    for num in nums:
        total += num
    return total