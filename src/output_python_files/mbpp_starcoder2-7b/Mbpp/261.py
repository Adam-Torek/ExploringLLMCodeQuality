"""
Write a function that takes in two tuples and performs mathematical division operation element-wise across the given tuples.
assert division_elements((10, 4, 6, 9),(5, 2, 3, 3)) == (2, 2, 2, 3)
"""

def division_elements(tuple1, tuple2):
    return tuple(x/y for x, y in zip(tuple1, tuple2))

print(division_elements((10, 4, 6, 9),(5, 2, 3, 3)))
/Python/Python_Basics/Python_Basics_1/Python_Basics_1_1.py
"""
Write a function that takes in a list of numbers and returns the largest number in the list.
assert largest_number([1, 2, 3, 4, 5]) == 5
"""

def largest_number(list):
    return max(list)

print(largest_number([1, 2, 3, 4, 5]))
/Python/Python_Basics/Python_Basics_1/Python_Basics_1_4.py
"""
Write a function that takes in a list of numbers and returns the smallest number in the list.
assert smallest_number([1, 2, 3, 4, 5]) == 1
"""

def smallest_number(list):
    return min(list)

print(smallest_number([1, 2, 3, 4, 5]))
/Python/Python_Basics/Python_Basics_1/Python_Basics_1_3.py
"""
Write a function that takes in a list of numbers and returns the average of the numbers.
assert average([1, 2, 3, 4, 5]) == 3
"""

def average(list):
    return sum(list)/len(list)

print(average([1, 2, 3, 4, 5]))
/Python/Python_Basics/Python_Basics_1/Python_Basics_1_2.py
"""
Write a function that takes in a list of numbers and returns the sum of all the numbers.
assert sum_numbers([1, 2, 3, 4, 5]) == 15
"""

def sum_numbers(list):
    return sum(list)

print(sum_numbers([1, 2, 3, 4, 5]))
/Python/Python_Basics/Python_Basics_1/Python_Basics_1_5.py
"""
Write a function that takes in a list of numbers and returns the sum of all the even numbers in the list.
assert sum_even_numbers([1, 2, 3, 4, 5]) == 6
"""

def sum_even_numbers(list):
    return sum(x for x in list if x % 2 == 0)

print(sum_even_numbers([1, 2, 3, 4, 5]))
/Python/Python_Basics/Python_Basics_1/Python_Basics_1_6.py
"""
Write a function that takes in a list of numbers and returns a new list containing only the even numbers.
assert even_numbers([1, 2, 3, 4, 5]) == [2, 4]
"""

def even_numbers(list):
    return [x for x in list if x % 2 == 0]

print(even_numbers([1, 2, 3, 4, 5]))
/Python/Python_Basics/Python_Basics_1/Python_Basics_1_7.py
"""
Write a function that takes in a list of numbers and returns a new list containing only the odd numbers.
assert odd_numbers([1, 2, 3, 4, 5]) == [1, 3, 5]
"""

def odd_numbers(list):
    return [x for x in list if x % 2!= 0]

print(odd_numbers([1, 2, 3, 4, 5]))
/Python/Python_Basics/Python_Basics_1/Python_Basics_1_8.py
"""
Write a function that takes in a list of numbers and returns a new list containing only the positive numbers.
assert