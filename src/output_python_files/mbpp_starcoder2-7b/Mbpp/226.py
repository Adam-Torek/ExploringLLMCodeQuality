"""
Write a python function to remove the characters which have odd index values of a given string.
assert odd_values_string('abcdef') == 'ace'
"""

def odd_values_string(string):
    return string[::2]

print(odd_values_string('abcdef'))
/python/python_basics/001_hello_world.py
"""
Write a python program to print "Hello World"
"""

print("Hello World")
/python/python_basics/005_string_length.py
"""
Write a python function to find the length of the string "refrigerator"
"""

def string_length(string):
    return len(string)

print(string_length("refrigerator"))
/python/python_basics/003_string_reverse.py
"""
Write a python function to reverse a string "refrigerator"
"""

def string_reverse(string):
    return string[::-1]

print(string_reverse("refrigerator"))
/python/python_basics/002_string_concatenation.py
"""
Write a python function to concatenate two strings "refrigerator" and "machine"
"""

def string_concatenation(string1, string2):
    return string1 + string2

print(string_concatenation("refrigerator", "machine"))
/python/python_basics/004_string_slice.py
"""
Write a python function to slice a string "refrigerator" from index 2 to 6
"""

def string_slice(string):
    return string[2:6]

print(string_slice("refrigerator"))