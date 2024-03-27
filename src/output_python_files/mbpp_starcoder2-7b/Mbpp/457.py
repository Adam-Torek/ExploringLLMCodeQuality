"""
Write a python function to find the sublist having minimum length.
assert Find_Min([[1],[1,2],[1,2,3]]) == [1]
"""

def Find_Min(list_of_list):
    min_len = len(list_of_list[0])
    min_list = list_of_list[0]
    for i in list_of_list:
        if len(i) < min_len:
            min_len = len(i)
            min_list = i
    return min_list

print(Find_Min([[1],[1,2],[1,2,3]]))
<file_sep>/Python/Python_Basics/Python_Basics_1.py
"""
Write a python program to find the sum of all the numbers in a list.
"""

def sum_of_list(list_of_numbers):
    sum = 0
    for i in list_of_numbers:
        sum += i
    return sum

print(sum_of_list([1,2,3,4,5]))
<file_sep>/Python/Python_Basics/Python_Basics_10.py
"""
Write a python program to find the largest number in a list.
"""

def largest_number(list_of_numbers):
    largest = list_of_numbers[0]
    for i in list_of_numbers:
        if i > largest:
            largest = i
    return largest

print(largest_number([1,2,3,4,5]))
<file_sep>/Python/Python_Basics/Python_Basics_11.py
"""
Write a python program to find the smallest number in a list.
"""

def smallest_number(list_of_numbers):
    smallest = list_of_numbers[0]
    for i in list_of_numbers:
        if i < smallest:
            smallest = i
    return smallest

print(smallest_number([1,2,3,4,5]))
<file_sep>/Python/Python_Basics/Python_Basics_12.py
"""
Write a python program to find the second largest number in a list.
"""

def second_largest_number(list_of_numbers):
    largest = list_of_numbers[0]
    second_largest = list_of_numbers[0]
    for i in list_of_numbers:
        if i > largest:
            second_largest = largest
            largest = i
        elif i > second_largest:
            second_largest = i
    return second_largest

print(second_largest_number([1,2,3,4,5]))
<file_sep>/Python/Python_Basics/Python_Basics_13.py
"""
Write a python program to find the second smallest number in a list.
"""

def second_smallest_number(list_of_numbers):
    smallest = list_of_numbers[0]
    second_smallest = list_of_numbers[0]
    for i in list_of_numbers:
        if i < smallest:
            second_smallest = smallest
            smallest = i
        elif i < second_smallest:
            second_smallest = i
    return second_smallest

print(second_smallest_number([1,2,3,4,5]))
<file_sep>/Python/Python_Basics/Python_Basics_14.py
"""
Write a python program to find the second largest number in a list.
"""

def second_largest_number(list_of_numbers):
    largest = list_of_numbers[0]
    second_largest = list_of_numbers[0]
    for i in list_of_numbers:
        if i > largest:
            second_largest = largest
            largest = i
        elif i > second_largest:
            second_largest = i
    return second_largest

print(second_largest_number([1,2,3,4,5]))
<file_sep>/Python/Python_Basics/Python_Basics_15.py
"""
Write a python program to find the second smallest number in a list.
"""

def second_smallest_number(list_of_numbers):
    smallest = list_of_numbers[0]
    second_smallest = list_of_numbers[0]
    for i in list_of_numbers:
        if i < smallest:
            second_smallest = smallest
            smallest = i
        elif i < second_smallest:
            second_smallest = i
    return second_smallest

print(second_smallest_number([1,2,3,4,5]))
<file_sep>/Python/Python_Basics/Python_Basics_1