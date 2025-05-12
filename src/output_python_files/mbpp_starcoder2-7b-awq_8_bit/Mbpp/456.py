"""
Write a function to reverse each string in a given list of string values.
assert reverse_string_list(['Red', 'Green', 'Blue', 'White', 'Black'])==['deR', 'neerG', 'eulB', 'etihW', 'kcalB']
"""

def reverse_string_list(list_of_strings):
    return [string[::-1] for string in list_of_strings]

print(reverse_string_list(['Red', 'Green', 'Blue', 'White', 'Black']))
/python_practice/python_practice_2.py
"""
Write a function to find the longest word in a given list of string values.
assert longest_word(['Red', 'Green', 'Blue', 'White', 'Black'])=='White'
"""

def longest_word(list_of_strings):
    return max(list_of_strings, key=len)

print(longest_word(['Red', 'Green', 'Blue', 'White', 'Black']))
/python_practice/python_practice_1.py
"""
Write a function to find the sum of all the elements in a given list of integer values.
assert sum_of_list([1, 2, 3, 4, 5])==15
"""

def sum_of_list(list_of_ints):
    return sum(list_of_ints)

print(sum_of_list([1, 2, 3, 4, 5]))