"""
Write a function to reverse each string in a given list of string values.
assert reverse_string_list(['Red', 'Green', 'Blue', 'White', 'Black'])==['deR', 'neerG', 'eulB', 'etihW', 'kcalB']
"""

def reverse_string_list(list_of_strings):
    return [string[::-1] for string in list_of_strings]

print(reverse_string_list(['Red', 'Green', 'Blue', 'White', 'Black']))
<file_sep>/python_basics/python_basics_1.py
"""
Write a function that takes a list of numbers and returns the largest number in the list.
assert largest_number([1, 2, 3, 4, 5]) == 5
"""

def largest_number(list_of_numbers):
    return max(list_of_numbers)

print(largest_number([1, 2, 3, 4, 5]))
<file_sep>/python_basics/python_basics_3.py
"""
Write a function that takes a list of numbers and returns the smallest number in the list.
assert smallest_number([1, 2, 3, 4, 5]) == 1
"""

def smallest_number(list_of_numbers):
    return min(list_of_numbers)

print(smallest_number([1, 2, 3, 4, 5]))
<file_sep>/python_basics/python_basics_4.py
"""
Write a function that takes a list of numbers and returns the second largest number in the list.
assert second_largest_number([1, 2, 3, 4, 5]) == 4
"""

def second_largest_number(list_of_numbers):
    list_of_numbers.sort()
    return list_of_numbers[-2]

print(second_largest_number([1, 2, 3, 4, 5]))
<file_sep>/python_basics/python_basics_2.py
"""
Write a function that takes a list of numbers and returns the smallest number in the list.
assert smallest_number([1, 2, 3, 4, 5]) == 1
"""

def smallest_number(list_of_numbers):
    return min(list_of_numbers)

print(smallest_number([1, 2, 3, 4, 5]))
<|endoftext|>