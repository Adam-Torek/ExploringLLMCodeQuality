"""
Write a python function takes in an integer and check whether the frequency of each digit in the integer is less than or equal to the digit itself.
assert validate(1234) == True
"""

def validate(num):
    num = str(num)
    for i in num:
        if num.count(i) > int(i):
            return False
    return True

print(validate(1234))
<file_sep>/python/python_practice/practice_1.py
"""
Write a python function takes in a list of numbers and returns the sum of all the numbers in the list.
assert sum_list([1,2,3,4,5]) == 15
"""

def sum_list(list):
    sum = 0
    for i in list:
        sum += i
    return sum

print(sum_list([1,2,3,4,5]))
<file_sep>/python/python_practice/practice_2.py
"""
Write a python function takes in a list of numbers and returns the average of all the numbers in the list.
assert average([1,2,3,4,5]) == 3
"""

def average(list):
    sum = 0
    for i in list:
        sum += i
    return sum/len(list)

print(average([1,2,3,4,5]))
<file_sep>/python/python_practice/practice_3.py
"""
Write a python function takes in a list of numbers and returns the largest number in the list.
assert largest([1,2,3,4,5]) == 5
"""

def largest(list):
    largest = list[0]
    for i in list:
        if i > largest:
            largest = i
    return largest

print(largest([1,2,3,4,5]))
<file_sep>/python/python_practice/practice_4.py
"""
Write a python function takes in a list of numbers and returns the smallest number in the list.
assert smallest([1,2,3,4,5]) == 1
"""

def smallest(list):
    smallest = list[0]
    for i in list:
        if i < smallest:
            smallest = i
    return smallest

print(smallest([1,2,3,4,5]))
<|endoftext|>