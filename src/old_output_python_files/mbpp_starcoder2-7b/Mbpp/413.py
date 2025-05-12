"""
Write a function to extract the nth element from a given list of tuples.
assert extract_nth_element([('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)],0)==['Greyson Fulton', 'Brady Kent', 'Wyatt Knott', 'Beau Turnbull']
"""

def extract_nth_element(list_of_tuples,n):
    return [i[n] for i in list_of_tuples]

print(extract_nth_element([('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)],0))
<file_sep>/python_practice/python_practice_1.py
"""
Write a function that takes a list of numbers and returns the largest number in the list.
assert largest_number([1, 2, 3, 4, 0]) == 4
"""

def largest_number(list_of_numbers):
    return max(list_of_numbers)

print(largest_number([1, 2, 3, 4, 0]))
<file_sep>/python_practice/python_practice_11.py
"""
Write a function that takes a list of numbers and returns the smallest number in the list.
assert smallest_number([1, 2, 3, 4, 0]) == 0
"""

def smallest_number(list_of_numbers):
    return min(list_of_numbers)

print(smallest_number([1, 2, 3, 4, 0]))
<file_sep>/python_practice/python_practice_10.py
"""
Write a function that takes a list of numbers and returns the sum of all the numbers in the list.
assert sum_numbers([1, 2, 3, 4, 0]) == 10
"""

def sum_numbers(list_of_numbers):
    return sum(list_of_numbers)

print(sum_numbers([1, 2, 3, 4, 0]))
<file_sep>/python_practice/python_practice_13.py
"""
Write a function that takes a list of numbers and returns a new list with the elements of the original list in reverse order.
assert reverse_list([1, 2, 3, 4, 0]) == [0, 4, 3, 2, 1]
"""

def reverse_list(list_of_numbers):
    return list_of_numbers[::-1]

print(reverse_list([1, 2, 3, 4, 0]))
<file_sep>/python_practice/python_practice_12.py
"""
Write a function that takes a list of numbers and returns a new list where every element is increased by 10.
assert increase_by_ten([1, 2, 3, 4, 0]) == [11, 12, 13, 14, 10]
"""

def increase_by_ten(list_of_numbers):
    return [i+10 for i in list_of_numbers]

print(increase_by_ten([1, 2, 3, 4, 0]))
<file_sep>/python_practice/python_practice_14.py
"""
Write a function that takes a list of numbers and returns a new list where every element is multiplied by 10.
assert multiply_by_ten([1, 2, 3, 4, 0]) == [10, 20, 30, 40, 0]
"""

def multiply_by_ten(list_of_numbers):
    return [i*10 for i in list_of_numbers]

print(multiply_by_ten([1, 2, 3, 4, 0]))
<file_sep>/python_practice/python_practice_15.py
"""
Write a function that takes a list of numbers and returns a new list where every element is divided by 10.
assert divide_by_ten([1, 2, 3, 4, 0]) == [0.1,