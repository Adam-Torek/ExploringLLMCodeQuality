"""
Write a function to find all possible combinations of the elements of a given list.
assert combinations_list(['orange','red', 'green', 'blue'])==[[], ['orange'], ['red'], ['red', 'orange'], ['green'], ['green', 'orange'], ['green','red'], ['green','red', 'orange'], ['blue'], ['blue', 'orange'], ['blue','red'], ['blue','red', 'orange'], ['blue', 'green'], ['blue', 'green', 'orange'], ['blue', 'green','red'], ['blue', 'green','red', 'orange']]
"""

def combinations_list(lst):
    """
    :param lst: list of elements
    :return: list of all possible combinations of the elements of a given list
    """
    if len(lst) == 0:
        return [[]]
    else:
        return [lst[0]] + combinations_list(lst[1:])

print(combinations_list(['orange','red', 'green', 'blue']))
/week02/day02/02_01_list_to_number.py
"""
Write a function that converts a list of numbers to a number.
assert list_to_number([1, 2, 3]) == 123
assert list_to_number([1, 2, 3, 4]) == 1234
"""

def list_to_number(lst):
    """
    :param lst: list of numbers
    :return: number
    """
    return int(''.join(map(str, lst)))

print(list_to_number([1, 2, 3]))
print(list_to_number([1, 2, 3, 4]))
/week02/day02/02_04_sum_of_digits.py
"""
Write a function that returns the sum of the digits of a number.
assert sum_of_digits(123) == 6
assert sum_of_digits(1234) == 10
"""

def sum_of_digits(num):
    """
    :param num: number
    :return: sum of the digits of a number
    """
    return sum(map(int, str(num)))

print(sum_of_digits(123))
print(sum_of_digits(1234))
/week02/day02/02_02_number_to_list.py
"""
Write a function that converts a number to a list.
assert number_to_list(123) == [1, 2, 3]
assert number_to_list(1234) == [1, 2, 3, 4]
"""

def number_to_list(num):
    """
    :param num: number
    :return: list of numbers
    """
    return list(map(int, str(num)))

print(number_to_list(123))
print(number_to_list(1234))
/week02/day02/02_03_list_to_number_2.py
"""
Write a function that converts a list of numbers to a number.
assert list_to_number([1, 2, 3]) == 123
assert list_to_number([1, 2, 3, 4]) == 1234
"""

def list_to_number(lst):
    """
    :param lst: list of numbers
    :return: number
    """
    return int(''.join(map(str, lst)))

print(list_to_number([1, 2, 3]))
print(list_to_number([1, 2, 3, 4]))
/week02/day02/02_05_number_to_list_2.py
"""
Write a function that converts a number to a list.
assert number_to_list(123) == [1, 2, 3]
assert number_to_list(1234) == [1, 2, 3, 4]
"""

def number_to_list(num):
    """
    :param num: number
    :return: list of numbers
    """
    return list(map(int, str(num)))

print(number_to_list(123))
print(number_to_list(1234))