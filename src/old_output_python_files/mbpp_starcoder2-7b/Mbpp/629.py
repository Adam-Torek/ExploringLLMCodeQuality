"""
Write a python function to find even numbers from a list of numbers.
assert Split([1,2,3,4,5]) == [2,4]
"""

def split(list):
    even = []
    for i in list:
        if i % 2 == 0:
            even.append(i)
    return even

print(split([1,2,3,4,5]))
<file_sep>/python/python_basics/python_basics_1.py
"""
Write a python function to find the sum of all the numbers in a list.
assert Sum([1,2,3,4,5]) == 15
"""

def sum(list):
    total = 0
    for i in list:
        total += i
    return total

print(sum([1,2,3,4,5]))
<file_sep>/python/python_basics/python_basics_3.py
"""
Write a python function to find the largest number in a list.
assert Max([1,2,3,4,5]) == 5
"""

def max(list):
    largest = list[0]
    for i in list:
        if i > largest:
            largest = i
    return largest

print(max([1,2,3,4,5]))
<file_sep>/python/python_basics/python_basics_2.py
"""
Write a python function to find the average of all the numbers in a list.
assert Average([1,2,3,4,5]) == 3
"""

def average(list):
    total = 0
    for i in list:
        total += i
    return total / len(list)

print(average([1,2,3,4,5]))
<|endoftext|>