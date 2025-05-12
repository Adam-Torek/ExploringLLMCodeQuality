"""
Write a function to compute the sum of digits of each number of a given list.
assert sum_of_digits([10,2,56])==14
"""

def sum_of_digits(lst):
    sum = 0
    for i in lst:
        while i > 0:
            sum += i % 10
            i //= 10
    return sum

print(sum_of_digits([10,2,56]))/python_basics/python_basics_1/task_1_1.py
"""
Write a function that takes a list of numbers and returns the sum of the numbers.
assert sum_of_numbers([1,2,3])==6
"""

def sum_of_numbers(lst):
    sum = 0
    for i in lst:
        sum += i
    return sum

print(sum_of_numbers([1,2,3]))/python_basics/python_basics_1/task_1_3.py
"""
Write a function that takes a list of numbers and returns the largest number.
assert largest_number([1,2,3])==3
"""

def largest_number(lst):
    max = lst[0]
    for i in lst:
        if i > max:
            max = i
    return max

print(largest_number([1,2,3]))/python_basics/python_basics_1/task_1_2.py
"""
Write a function that takes a list of numbers and returns the smallest number.
assert smallest_number([1,2,3])==1
"""

def smallest_number(lst):
    min = lst[0]
    for i in lst:
        if i < min:
            min = i
    return min

print(smallest_number([1,2,3]))/python_basics/python_basics_1/task_1_4.py
"""
Write a function that takes a list of numbers and returns the smallest number.
assert smallest_number([1,2,3])==1
"""

def smallest_number(lst):
    min = lst[0]
    for i in lst:
        if i < min:
            min = i
    return min

print(smallest_number([1,2,3]))

def largest_number(lst):
    max = lst[0]
    for i in lst:
        if i > max:
            max = i
    return max

print(largest_number([1,2,3]))

def sum_of_numbers(lst):
    sum = 0
    for i in lst:
        sum += i
    return sum

print(sum_of_numbers([1,2,3]))

def sum_of_digits(lst):
    sum = 0
    for i in lst:
        while i > 0:
            sum += i % 10
            i //= 10
    return sum

print(sum_of_digits([10,2,56]))/python_basics/python_basics_1/task_1_5.py
"""
Write a function that takes a list of numbers and returns the smallest number.
assert smallest_number([1,2,3])==1
"""

def smallest_number(lst):
    min = lst[0]
    for i in lst:
        if i < min:
            min = i
    return min

print(smallest_number([1,2,3]))

def largest_number(lst):
    max = lst[0]
    for i in lst:
        if i > max:
            max = i
    return max

print(largest_number([1,2,3]))

def sum_of_numbers(lst):
    sum = 0
    for i in lst:
        sum += i
    return sum

print(sum_of_numbers([1,2,3]))

def sum_of_digits(lst):
    sum = 0
    for i in lst:
        while i > 0:
            sum += i % 10
            i //= 10
    return sum

print(sum_of_digits([10,2,56]))

def sum_of_digits(lst):
    sum = 0
    for i in lst:
        while i > 0:
            sum += i % 10
            i //= 10
    return sum

print(sum_of_digits([10,2,56]))

def sum_of_digits(lst):
    sum = 0
    for i in lst: