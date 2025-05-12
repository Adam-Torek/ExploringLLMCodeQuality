"""
Write a function to compute the sum of digits of each number of a given list.
assert sum_of_digits([10,2,56])==14
"""
def sum_of_digits(lst):
    sum = 0
    for i in lst:
        while i > 0:
            sum += i % 10
            i //= 10
    return sum

print(sum_of_digits([10,2,56]))
/python/python_basics/python_basics_01.py
"""
Write a function that takes a list of numbers and returns the sum of the numbers.
assert sum_of_numbers([1,2,3])==6
"""
def sum_of_numbers(lst):
    sum = 0
    for i in lst:
        sum += i
    return sum

print(sum_of_numbers([1,2,3]))
/python/python_basics/python_basics_03.py
"""
Write a function that takes a list of numbers and returns the largest number in the list.
assert largest_number([1,2,3])==3
"""
def largest_number(lst):
    max = 0
    for i in lst:
        if i > max:
            max = i
    return max

print(largest_number([1,2,3]))
/python/python_basics/python_basics_02.py
"""
Write a function that takes a list of numbers and returns the smallest number in the list.
assert smallest_number([1,2,3])==1
"""
def smallest_number(lst):
    min = 1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000