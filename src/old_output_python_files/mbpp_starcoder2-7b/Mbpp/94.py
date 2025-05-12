"""
Given a list of tuples, write a function that returns the first value of the tuple with the smallest second value.
assert index_minimum([('Rash', 143), ('Manjeet', 200), ('Varsha', 100)]) == 'Varsha'
"""

def index_minimum(list_of_tuples):
    min_value = list_of_tuples[0][1]
    min_index = 0
    for i in range(len(list_of_tuples)):
        if list_of_tuples[i][1] < min_value:
            min_value = list_of_tuples[i][1]
            min_index = i
    return list_of_tuples[min_index][0]

print(index_minimum([('Rash', 143), ('Manjeet', 200), ('Varsha', 100)]))
<file_sep>/python_basics/python_basics_1/python_basics_1_1.py
"""
Write a function that takes a list of numbers and returns the largest number in the list.
assert largest([1, 2, 3, 4, 0]) == 4
"""

def largest(list_of_numbers):
    max_value = list_of_numbers[0]
    for i in range(len(list_of_numbers)):
        if list_of_numbers[i] > max_value:
            max_value = list_of_numbers[i]
    return max_value

print(largest([1, 2, 3, 4, 0]))
<file_sep>/python_basics/python_basics_1/python_basics_1_2.py
"""
Write a function that takes a list of numbers and returns the smallest number in the list.
assert smallest([1, 2, 3, 4, 0]) == 0
"""

def smallest(list_of_numbers):
    min_value = list_of_numbers[0]
    for i in range(len(list_of_numbers)):
        if list_of_numbers[i] < min_value:
            min_value = list_of_numbers[i]
    return min_value

print(smallest([1, 2, 3, 4, 0]))
<file_sep>/python_basics/python_basics_1/python_basics_1_3.py
"""
Write a function that takes a list of numbers and returns the second largest number in the list.
assert second_largest([1, 2, 3, 4, 0]) == 3
"""

def second_largest(list_of_numbers):
    max_value = list_of_numbers[0]
    second_max_value = list_of_numbers[0]
    for i in range(len(list_of_numbers)):
        if list_of_numbers[i] > max_value:
            second_max_value = max_value
            max_value = list_of_numbers[i]
        elif list_of_numbers[i] > second_max_value:
            second_max_value = list_of_numbers[i]
    return second_max_value

print(second_largest([1, 2, 3, 4, 0]))
<file_sep>/python_basics/python_basics_1/python_basics_1_4.py
"""
Write a function that takes a list of numbers and returns the second smallest number in the list.
assert second_smallest([1, 2, 3, 4, 0]) == 1
"""

def second_smallest(list_of_numbers):
    min_value = list_of_numbers[0]
    second_min_value = list_of_numbers[0]
    for i in range(len(list_of_numbers)):
        if list_of_numbers[i] < min_value:
            second_min_value = min_value
            min_value = list_of_numbers[i]
        elif list_of_numbers[i] < second_min_value:
            second_min_value = list_of_numbers[i]
    return second_min_value

print(second_smallest([1, 2, 3, 4, 0]))
<file_sep>/python_basics/python_basics_1/python_basics_1_5.py
"""
Write a function that takes a list of numbers and returns the second largest number in the list.
assert second_largest([1, 2, 3