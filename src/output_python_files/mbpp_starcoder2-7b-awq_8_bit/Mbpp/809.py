"""
Write a function to check if each element of second tuple is smaller than its corresponding element in the first tuple.
assert check_smaller((1, 2, 3), (2, 3, 4)) == False
"""

def check_smaller(tuple1, tuple2):
    return all(x < y for x, y in zip(tuple1, tuple2))

print(check_smaller((1, 2, 3), (2, 3, 4)))
/python_basics/00_python_basics/00_python_basics.py
"""
Write a function that takes a list of numbers and returns the sum of the numbers.
assert sum_numbers([1, 2, 3]) == 6
"""

def sum_numbers(numbers):
    return sum(numbers)

print(sum_numbers([1, 2, 3]))
/python_basics/02_lists/02_lists.py
"""
Write a function that takes a list of numbers and returns the largest number.
assert largest_number([1, 2, 3]) == 3
"""

def largest_number(numbers):
    return max(numbers)

print(largest_number([1, 2, 3]))
/python_basics/03_strings/03_strings.py
"""
Write a function that takes a string and returns the number of words in the string.
assert count_words("Hello world") == 2
"""

def count_words(string):
    return len(string.split())

print(count_words("Hello world"))
/python_basics/01_tuples/01_tuples.py
"""
Write a function that takes a tuple of numbers and returns the smallest number.
assert smallest_number((1, 2, 3)) == 1
"""

def smallest_number(numbers):
    return min(numbers)

print(smallest_number((1, 2, 3)))
/python_basics/04_dictionaries/04_dictionaries.py
"""
Write a function that takes a dictionary and returns the sum of the values.
assert sum_values({"a": 1, "b": 2, "c": 3}) == 6
"""

def sum_values(dictionary):
    return sum(dictionary.values())

print(sum_values({"a": 1, "b": 2, "c": 3}))
/python_basics/05_sets/05_sets.py
"""
Write a function that takes a set and returns the number of elements in the set.
assert count_elements({1, 2, 3}) == 3
"""

def count_elements(set):
    return len(set)

print(count_elements({1, 2, 3}))
/python_basics/06_functions/06_functions.py
"""
Write a function that takes a list of numbers and returns the largest number.
assert largest_number([1, 2, 3]) == 3
"""

def largest_number(numbers):
    return max(numbers)

print(largest_number([1, 2, 3]))
/python_basics/07_classes/07_classes.py
"""
Write a class that represents a rectangle.
The class should have two attributes: width and height.
The class should have a method that returns the area of the rectangle.
assert Rectangle(1, 2).area() == 2
"""

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

print(Rectangle(1, 2).area())
/python_basics/08_inheritance/08_inheritance.py
"""
Write a class that represents a rectangle.
The class should have two attributes: width and height.
The class should have a method that returns the area of the rectangle.
Write a class that inherits from the previous class.
The class should have a method that returns the perimeter of the rectangle.
assert Rectangle(1, 2).area() == 2
assert Rectangle(1, 2).perimeter() == 6
"""

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class