"""
Write a function to find the circumference of a circle.
assert math.isclose(circle_circumference(10), 62.830000000000005, rel_tol=0.001)
"""

import math

def circle_circumference(radius):
    return 2 * math.pi * radius

assert math.isclose(circle_circumference(10), 62.830000000000005, rel_tol=0.001)
<file_sep>/02_data_types/01_numbers/01_numbers.py
"""
Write a function to add two numbers.
assert add(1, 2) == 3
"""

def add(a, b):
    return a + b

assert add(1, 2) == 3
<file_sep>/02_data_types/03_strings/01_strings.py
"""
Write a function to reverse a string.
assert reverse("hello") == "olleh"
"""

def reverse(string):
    return string[::-1]

assert reverse("hello") == "olleh"
<file_sep>/02_data_types/02_lists/01_lists.py
"""
Write a function to find the sum of all the numbers in a list.
assert sum_list([1, 2, 3]) == 6
"""

def sum_list(list):
    return sum(list)

assert sum_list([1, 2, 3]) == 6
<file_sep>/02_data_types/03_strings/02_strings.py
"""
Write a function to find the length of a string.
assert length("hello") == 5
"""

def length(string):
    return len(string)

assert length("hello") == 5
<file_sep>/02_data_types/02_lists/02_lists.py
"""
Write a function to find the length of a list.
assert length([1, 2, 3]) == 3
"""

def length(list):
    return len(list)

assert length([1, 2, 3]) == 3
<file_sep>/02_data_types/03_strings/03_strings.py
"""
Write a function to find the first character of a string.
assert first_character("hello") == "h"
"""

def first_character(string):
    return string[0]

assert first_character("hello") == "h"
<file_sep>/02_data_types/03_strings/04_strings.py
"""
Write a function to find the last character of a string.
assert last_character("hello") == "o"
"""

def last_character(string):
    return string[-1]

assert last_character("hello") == "o"
<file_sep>/02_data_types/03_strings/05_strings.py
"""
Write a function to find the nth character of a string.
assert nth_character("hello", 1) == "e"
"""

def nth_character(string, n):
    return string[n]

assert nth_character("hello", 1) == "e"
<file_sep>/02_data_types/02_lists/03_lists.py
"""
Write a function to find the first element of a list.
assert first_element([1, 2, 3]) == 1
"""

def first_element(list):
    return list[0]

assert first_element([1, 2, 3]) == 1
<file_sep>/02_data_types/02_lists/04_lists.py
"""
Write a function to find the last element of a list.
assert last_element([1, 2, 3]) == 3
"""

def last_element(list):
    return list[-1]

assert last_element([1, 2, 3]) == 3
<file_sep>/02_data_types/03_strings/06_strings.py
"""
Write a function to find the nth character of a string.
assert nth_character("hello", 1) == "e"
"""

def nth_character(string, n):
    return string[n]

assert nth_character("hello", 1) == "e