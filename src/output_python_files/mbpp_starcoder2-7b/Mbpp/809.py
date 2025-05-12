"""
Write a function to check if each element of second tuple is smaller than its corresponding element in the first tuple.
assert check_smaller((1, 2, 3), (2, 3, 4)) == False
"""

def check_smaller(tuple1, tuple2):
    if len(tuple1)!= len(tuple2):
        return False
    for i in range(len(tuple1)):
        if tuple1[i] >= tuple2[i]:
            return False
    return True

print(check_smaller((1, 2, 3), (2, 3, 4)))
/python/python_basics/02_variables/02_variables.py
"""
Write a program that asks the user for their name and greets them with their name.
"""

name = input("What is your name? ")
print("Hello " + name)
/python/python_basics/04_lists/04_lists.py
"""
Write a program that asks the user for a number and prints the square of that number.
"""

number = int(input("Enter a number: "))
print(number ** 2)
/python/python_basics/03_strings/03_strings.py
"""
Write a program that asks the user for their name and greets them with their name.
"""

name = input("What is your name? ")
print("Hello " + name)
/python/python_basics/05_tuples/05_tuples.py
"""
Write a function that takes a tuple of numbers and returns the largest number.
assert largest_number((1, 2, 3)) == 3
"""

def largest_number(tuple):
    return max(tuple)

print(largest_number((1, 2, 3)))
/python/python_basics/06_dictionaries/06_dictionaries.py
"""
Write a function that takes a dictionary and returns the largest value.
assert largest_value({'a': 1, 'b': 2, 'c': 3}) == 3
"""

def largest_value(dictionary):
    return max(dictionary.values())

print(largest_value({'a': 1, 'b': 2, 'c': 3}))
/python/python_basics/07_sets/07_sets.py
"""
Write a function that takes a set and returns the largest value.
assert largest_value({1, 2, 3}) == 3
"""

def largest_value(set):
    return max(set)

print(largest_value({1, 2, 3}))
/python/python_basics/08_functions/08_functions.py
"""
Write a function that takes a list of numbers and returns the largest number.
assert largest_number([1, 2, 3]) == 3
"""

def largest_number(list):
    return max(list)

print(largest_number([1, 2, 3]))
/python/python_basics/09_conditionals/09_conditionals.py
"""
Write a function that takes a number and returns whether it is even or odd.
assert even_or_odd(2) == "even"
assert even_or_odd(3) == "odd"
"""

def even_or_odd(number):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"

print(even_or_odd(2))
print(even_or_odd(3))
/python/python_basics/01_hello_world/01_hello_world.py
"""
Write a program that prints "Hello World!" to the screen.
"""

print("Hello World!")
/python/python_basics/04_lists/04_lists_2.py
"""
Write a program that asks the user for a number and prints the square of that number.
"""

number = int(input("Enter a number: "))
print(number ** 2)

# or

numbers = [1, 2, 3]
print(numbers[0] ** 2)
print(numbers[1] ** 2)
print(numbers[2] ** 2)
/python/python_basics/05_tuples/05_tuples_2.py
"""
Write a function that takes a tuple of numbers and returns