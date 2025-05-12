"""
Write a function that returns the perimeter of a square given its side length as input.
assert square_perimeter(10)==40
"""

def square_perimeter(side):
    return side * 4

print(square_perimeter(10))
/python/001_python_basics/002_variables/001_variables.py
"""
Write a function that returns the area of a square given its side length as input.
assert square_area(10)==100
"""

def square_area(side):
    return side * side

print(square_area(10))
/python/001_python_basics/001_hello_world/001_hello_world.py
"""
Write a function that returns the string "Hello World!"
assert hello_world()=="Hello World!"
"""

def hello_world():
    return "Hello World!"

print(hello_world())
/python/001_python_basics/003_conditionals/001_conditionals.py
"""
Write a function that returns the string "Hello World!" if the input is "Hello World!"
assert hello_world("Hello World!")=="Hello World!"
"""

def hello_world(input):
    if input == "Hello World!":
        return "Hello World!"
    else:
        return "Not Hello World!"

print(hello_world("Hello World!"))
/python/001_python_basics/004_loops/001_loops.py
"""
Write a function that returns the sum of the first 100 positive integers.
assert sum_of_first_100_integers()==5050
"""

def sum_of_first_100_integers():
    sum = 0
    for i in range(1, 101):
        sum += i
    return sum

print(sum_of_first_100_integers())
/python/001_python_basics/005_lists/001_lists.py
"""
Write a function that returns the sum of the first 100 positive integers.
assert sum_of_first_100_integers()==5050
"""

def sum_of_first_100_integers():
    return sum(range(1, 101))

print(sum_of_first_100_integers())
/python/001_python_basics/006_dictionaries/001_dictionaries.py
"""
Write a function that returns the sum of the first 100 positive integers.
assert sum_of_first_100_integers()==5050
"""

def sum_of_first_100_integers():
    return sum(range(1, 101))

print(sum_of_first_100_integers())
/python/001_python_basics/007_classes/001_classes.py
"""
Write a function that returns the sum of the first 100 positive integers.
assert sum_of_first_100_integers()==5050
"""

class SumOfFirst100Integers:
    def __init__(self):
        self.sum = 0

    def add(self, number):
        self.sum += number

    def get_sum(self):
        return self.sum

def sum_of_first_100_integers():
    sum_of_first_100_integers = SumOfFirst100Integers()
    for i in range(1, 101):
        sum_of_first_100_integers.add(i)
    return sum_of_first_100_integers.get_sum()

print(sum_of_first_100_integers())
/python/001_python_basics/008_modules/001_modules.py
"""
Write a function that returns the sum of the first 100 positive integers.
assert sum_of_first_100_integers()==