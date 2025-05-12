"""
Write a function to find then'th lucas number.
assert find_lucas(9) == 76
"""

def find_lucas(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return find_lucas(n-1) + find_lucas(n-2)

print find_lucas(9)
/week_02/day_03/01_list_to_number.py
"""
Write a function that converts a list of numbers to a number.

assert list_to_number([1, 2, 3]) == 123
"""

def list_to_number(list):
    return int(''.join(map(str, list)))

print list_to_number([1, 2, 3])
/week_02/day_03/03_number_to_list.py
"""
Write a function that converts a number to a list.

assert number_to_list(123) == [1, 2, 3]
"""

def number_to_list(number):
    return map(int, str(number))

print number_to_list(123)
/week_02/day_03/02_list_to_string.py
"""
Write a function that converts a list of strings to a string.

assert list_to_string(["a", "b", "c"]) == "abc"
"""

def list_to_string(list):
    return ''.join(list)

print list_to_string(["a", "b", "c"])
/week_02/day_03/04_string_to_list.py
"""
Write a function that converts a string to a list.

assert string_to_list("abc") == ["a", "b", "c"]
"""

def string_to_list(string):
    return list(string)

print string_to_list("abc")
/week_02/day_03/05_list_to_string_with_separator.py
"""
Write a function that converts a list of strings to a string.

assert list_to_string_with_separator(["a", "b", "c"], "-") == "a-b-c"
"""

def list_to_string_with_separator(list, separator):
    return separator.join(list)

print list_to_string_with_separator(["a", "b", "c"], "-")
/week_02/day_03/06_string_to_list_with_separator.py
"""
Write a function that converts a string to a list.

assert string_to_list_with_separator("a-b-c", "-") == ["a", "b", "c"]
"""

def string_to_list_with_separator(string, separator):
    return string.split(separator)

print string_to_list_with_separator("a-b-c", "-")
/week_02/day_03/07_list_to_string_with_separator.py
"""
Write a function that converts a list of strings to a string.

assert list_to_string_with_separator(["a", "b", "c"], "-") == "a-b-c"
"""

def list_to_string_with_separator(list, separator):
    return separator.join(list)

print list_to_string_with_separator(["a", "b", "c"], "-")
/week_02/day_03/08_string_to_list_with_separator.py
"""
Write a function that converts a string to a list.

assert string_to_list_with_separator("a-b-c", "-") == ["a", "b", "c"]
"""

def string_to_list_with_separator(string, separator):
    return string.split(separator)

print string_to_list_with_separator("a-b-c", "-")
/week_02/day_03/09_list_to_string_with_separator.py
"""
Write a function that converts a list of strings to a string.

assert list_to_string_with_