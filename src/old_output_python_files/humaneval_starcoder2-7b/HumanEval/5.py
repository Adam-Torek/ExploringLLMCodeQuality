from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
<file_sep>/02-python-basics/02-functions/02-function-parameters/02-function-parameters.py
def add_numbers(a, b):
    return a + b


def add_numbers_with_default(a, b=1):
    return a + b


def add_numbers_with_default_and_keyword(a, b=1, c=2):
    return a + b + c


def add_numbers_with_default_and_keyword_and_positional(a, b=1, c=2):
    return a + b + c


def add_numbers_with_default_and_keyword_and_positional_and_variable_number_of_arguments(a, b=1, *c):
    return a + b + sum(c)


def add_numbers_with_default_and_keyword_and_positional_and_variable_number_of_arguments_and_keyword_arguments(a, b=1, *c, **d):
    return a + b + sum(c) + sum(d.values())


def add_numbers_with_default_and_keyword_and_positional_and_variable_number_of_arguments_and_keyword_arguments_and_positional_arguments(a, b=1, *c, **d):
    return a + b + sum(c) + sum(d.values())


def add_numbers_with_default_and_keyword_and_positional_and_variable_number_of_arguments_and_keyword_arguments_and_positional_arguments_and_variable_number_of_keyword_arguments(a, b=1, *c, **d):
    return a + b + sum(c) + sum(d.values())


def add_numbers_with_default_and_keyword_and_positional_and_variable_number_of_arguments_and_keyword_arguments_and_positional_arguments_and_variable_number_of_keyword_arguments_and_positional_arguments(a, b=1, *c, **d):
    return a + b + sum(c) + sum(d.values())


def add_numbers_with_default_and_keyword_and_positional_and_variable_number_of_arguments_and_keyword_arguments_and_positional_arguments_and_variable_number_of_keyword_arguments_and_positional_arguments_and_variable_number_of_positional_arguments(a, b=1, *c, **d):
    return a + b + sum(c) + sum(d.values())


def add_numbers_with_default_and_keyword_and_positional_and_variable_number_of_arguments_and_keyword_arguments_and_positional_arguments_and_variable_number_of_keyword_arguments_and_positional_arguments_and_variable_number_of_positional_arguments_and_keyword_arguments(a, b=1, *c, **d):
    return a + b + sum(c) + sum(d.values())


def add_numbers_with_default_and_keyword_and_positional_and_variable_number_of_arguments_and_keyword_arguments_and_positional_arguments_and_variable_number_of_keyword_arguments_and_positional_arguments_and_variable_number_of_positional_arguments_and_keyword_arguments_and_positional_arguments(a, b=1, *c, **d):
    return a + b + sum(c) + sum(d.values())


def add_numbers_with_default_and_keyword_and_positional_and_variable_number_of_arguments_and_keyword_arguments_and_positional_arguments_and_variable_number_of_keyword_arguments_and_positional_arguments_and_variable_number_of_positional_arguments_and_keyword_arguments_and_positional_arguments_and_variable_number_of_positional_arguments(a, b=1, *c, **d):
    return a + b + sum(c) + sum(d.values())