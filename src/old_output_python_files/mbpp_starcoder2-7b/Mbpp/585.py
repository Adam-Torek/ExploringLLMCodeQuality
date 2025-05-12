"""
Write a function to find the n most expensive items in a given dataset.
assert expensive_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}],1)==[{'name': 'Item-2', 'price': 555.22}]
"""

def expensive_items(items, n):
    return sorted(items, key=lambda x: x['price'], reverse=True)[:n]

print(expensive_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}],1))
<file_sep>/python/python_basics/001_hello_world.py
"""
Write a function that prints "Hello World!"
"""

def hello_world():
    print("Hello World!")

hello_world()
<file_sep>/python/python_basics/003_sum_of_numbers.py
"""
Write a function that sums up all the numbers in a given list.
assert sum_of_numbers([1,2,3,4,5])==15
"""

def sum_of_numbers(numbers):
    return sum(numbers)

print(sum_of_numbers([1,2,3,4,5]))
<file_sep>/python/python_basics/004_sum_of_numbers_in_range.py
"""
Write a function that sums up all the numbers in a given range.
assert sum_of_numbers_in_range(1,5)==15
"""

def sum_of_numbers_in_range(start, end):
    return sum(range(start, end+1))

print(sum_of_numbers_in_range(1,5))
<file_sep>/python/python_basics/002_sum_of_numbers_in_range.py
"""
Write a function that sums up all the numbers in a given range.
assert sum_of_numbers_in_range(1,5)==15
"""

def sum_of_numbers_in_range(start, end):
    total = 0
    for i in range(start, end+1):
        total += i
    return total

print(sum_of_numbers_in_range(1,5))
<file_sep>/python/python_basics/005_sum_of_numbers_in_range_with_step.py
"""
Write a function that sums up all the numbers in a given range with a given step.
assert sum_of_numbers_in_range_with_step(1,5,2)==9
"""

def sum_of_numbers_in_range_with_step(start, end, step):
    total = 0
    for i in range(start, end+1, step):
        total += i
    return total

print(sum_of_numbers_in_range_with_step(1,5,2))
<file_sep>/python/python_basics/006_sum_of_numbers_in_range_with_step.py
"""
Write a function that sums up all the numbers in a given range with a given step.
assert sum_of_numbers_in_range_with_step(1,5,2)==9
"""

def sum_of_numbers_in_range_with_step(start, end, step):
    return sum(range(start, end+1, step))

print(sum_of_numbers_in_range_with_step(1,5,2))
<file_sep>/python/python_basics/007_sum_of_numbers_in_range_with_step.py
"""
Write a function that sums up all the numbers in a given range with a given step.
assert sum_of_numbers_in_range_with_step(1,5,2)==9
"""

def sum_of_numbers_in_range_with_step(start, end, step):
    return sum(range(start, end+1, step))

print(sum_of_numbers_in_range_with_step(1,5,2))
<file_sep>/python/python_basics/008_sum_of_numbers_in_range_with_step.py
"""
Write a function that sums up all the numbers in a given range with a given step.
assert sum_of_numbers_in_range_with_step(1