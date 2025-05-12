from typing import List


def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appeares in factorization.
    Input number should be equal to the product of all factors
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    """
/week03/day01/02_list_to_dict.py
# Create a function that takes a list of strings as parameter,
#  and returns a dictionary with every string as a key and it's length as a value
#  Example: ["hello", "edabit"] should produce {"hello": 5, "edabit": 6}

def list_to_dict(lst):
    return {i: len(i) for i in lst}
/week03/day01/01_sum_of_digits.py
# Create a function that takes a number as an argument and returns the sum of its digits.
#  Examples
#  sum_of_digits(6) ➞ 6
#  sum_of_digits(123) ➞ 6
#  sum_of_digits(4217) ➞ 12
#  sum_of_digits(1) ➞ 1
#  sum_of_digits(0) ➞ 0

def sum_of_digits(number):
    return sum([int(i) for i in str(number)])
/week03/day01/03_sum_of_numbers.py
# Create a function that takes a list of numbers and returns the sum of the first two numbers.
#  If the list only has one number, return that number.
#  Examples
#  sum_two([1, 2, 3]) ➞ 3
#  sum_two([4, 1]) ➞ 4
#  sum_two([4, 1, 7, 6]) ➞ 4
#  sum_two([1]) ➞ 1

def sum_two(lst):
    return sum(lst[:2]) if len(lst) > 1 else lst[0]
/week03/day01/04_sum_of_numbers_in_list.py
# Create a function that takes a list of numbers and returns the sum of the first and last number.
#  If the list is empty, return 0.
#  Examples
#  sum_first_and_last([2, 7, 3]) ➞ 5
#  sum_first_and_last([10]) ➞ 10
#  sum_first_and_last([]) ➞ 0

def sum_first_and_last(lst):
    return sum(lst[:2]) if len(lst) > 1 else lst[0] if len(lst) > 0 else 0
/week03/day01/05_sum_of_numbers_in_list.py
# Create a function that takes a list of numbers and returns the sum of the first and last number.
#  If the list is empty, return 0.
#  Examples
#  sum_first_and_last([2, 7, 3]) ➞ 5
#  sum_first_and_last([10]) ➞ 10
#  sum_first_and_last([]) ➞ 0

def sum_first_and_last(lst):
    return sum(lst[:2]) if len(lst) > 1 else lst[0] if len(lst) > 0 else 0
/week03/day01/06_sum_of_numbers_in_list.py
# Create a function that takes a list of numbers and returns the sum of the first and last number.
#  If the list is empty, return 0.
#  Examples
#  sum_first_and_last([2, 7, 3]) ➞ 5
#  sum_first_and_last([10]) ➞ 10
#  sum_first_and_last([]) ➞ 0

def sum_first_and_last(lst):
    return sum(lst[:2]) if len(lst) >