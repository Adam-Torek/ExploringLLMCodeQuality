"""
Write a function to reverse each string in a given list of string values.
assert reverse_string_list(['Red', 'Green', 'Blue', 'White', 'Black'])==['deR', 'neerG', 'eulB', 'etihW', 'kcalB']
"""

def reverse_string_list(list_of_strings):
    return [string[::-1] for string in list_of_strings]

print(reverse_string_list(['Red', 'Green', 'Blue', 'White', 'Black']))
/python_fundamentals/fundamentals/fundamentals_1.py
"""
Write a function that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.
assert remove_duplicates([1, 1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 9])==[1, 2, 3, 4, 5, 6, 7, 8, 9]
"""

def remove_duplicates(list_of_numbers):
    return list(set(list_of_numbers))

print(remove_duplicates([1, 1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 9]))
/python_fundamentals/fundamentals/fundamentals_2.py
"""
Write a function that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.
assert remove_duplicates([1, 1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 9])==[1, 2, 3, 4, 5, 6, 7, 8, 9]
"""

def remove_duplicates(list_of_numbers):
    return list(set(list_of_numbers))

print(remove_duplicates([1, 1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 9]))

"""
Write a function that takes a list of numbers and returns the sum of all the numbers in the list.
assert sum_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])==55
"""

def sum_list(list_of_numbers):
    return sum(list_of_numbers)

print(sum_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

"""
Write a function that takes a list of numbers and returns a new list where all the elements are greater than 10.
assert greater_than_10([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])==[11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
"""

def greater_than_10(list_of_numbers):
    return [number for number in list_of_numbers if number > 10]

print(greater_than_10([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

"""
Write a function that takes a list of numbers and returns a new list where all the elements are greater than 10.
assert greater_than_10([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])==[11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
"""

def greater_than_10(list_of_numbers):
    return [number for number in list_of_numbers if number > 10]

print(greater_than_10([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

"""
Write a function that takes a list of numbers and returns a new list where all the elements are greater than 10.
assert greater