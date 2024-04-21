"""
Write a function to remove the parenthesis and what is inbetween them from a string.
assert remove_parenthesis(["python (chrome)"])==("python")
"""

def remove_parenthesis(string):
    return string[0:string.index("(")]

print(remove_parenthesis(["python (chrome)"]))
<file_sep>/python/python_basics/001_hello_world.py
"""
Write a function that prints "Hello World"
"""

def hello_world():
    print("Hello World")

hello_world()
<file_sep>/python/python_basics/003_sum_of_numbers.py
"""
Write a function that takes a list of numbers and returns the sum of the numbers.
assert sum_of_numbers([1,2,3,4,5])==15
"""

def sum_of_numbers(numbers):
    return sum(numbers)

print(sum_of_numbers([1,2,3,4,5]))
<file_sep>/python/python_basics/004_reverse_string.py
"""
Write a function that takes a string and returns the reverse of the string.
assert reverse_string("hello")=="olleh"
"""

def reverse_string(string):
    return string[::-1]

print(reverse_string("hello"))
<file_sep>/python/python_basics/002_sum_of_numbers_in_list.py
"""
Write a function that takes a list of numbers and returns the sum of the numbers.
assert sum_of_numbers_in_list([1,2,3,4,5])==15
"""

def sum_of_numbers_in_list(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

print(sum_of_numbers_in_list([1,2,3,4,5]))
<file_sep>/python/python_basics/005_sum_of_numbers_in_range.py
"""
Write a function that takes a start and end number and returns the sum of all numbers between the start and end.
assert sum_of_numbers_in_range(1,5)==15
"""

def sum_of_numbers_in_range(start, end):
    total = 0
    for number in range(start, end+1):
        total += number
    return total

print(sum_of_numbers_in_range(1,5))
<file_sep>/python/python_basics/006_sum_of_numbers_in_range_step.py
"""
Write a function that takes a start, end and step number and returns the sum of all numbers between the start and end.
assert sum_of_numbers_in_range_step(1,5,2)==9
"""

def sum_of_numbers_in_range_step(start, end, step):
    total = 0
    for number in range(start, end+1, step):
        total += number
    return total

print(sum_of_numbers_in_range_step(1,5,2))
<file_sep>/python/python_basics/007_sum_of_numbers_in_range_step_negative.py
"""
Write a function that takes a start, end and step number and returns the sum of all numbers between the start and end.
assert sum_of_numbers_in_range_step_negative(5,1,-2)==9
"""

def sum_of_numbers_in_range_step_negative(start, end, step):
    total = 0
    for number in range(start, end+1, step):
        total += number
    return total

print(sum_of_numbers_in_range_step_negative(5,1,-2))
<file_sep>/python/python_basics/008_sum_of_numbers_in_range_step_negative_reverse.py
"""
Write a function that takes a start, end and step number and returns the sum of all numbers between the start and end.
assert sum_of_numbers_in_range_step_negative_reverse(5,1,-2)==9
"""

def sum_of_numbers_in_range_step_negative_reverse(start, end, step):
    total = 0
    for number in range(start, end-1, step):
        total += number
    return total

print(sum_of_numbers_in_range_step_negative_reverse(5,1,-2))
<file_sep>/