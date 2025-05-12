"""
Write a function to convert a given tuple of positive integers into a single integer.
assert tuple_to_int((1,2,3))==123
"""

def tuple_to_int(tup):
    return int(''.join(map(str,tup)))

print(tuple_to_int((1,2,3)))
/python_practice/python_practice_1/python_practice_1_1.py
"""
Write a function that takes a list of numbers and returns the largest number in the list.
"""

def largest_number(lst):
    return max(lst)

print(largest_number([1,2,3,4,5]))
/python_practice/python_practice_1/python_practice_1_2.py
"""
Write a function that takes a list of numbers and returns the smallest number in the list.
"""

def smallest_number(lst):
    return min(lst)

print(smallest_number([1,2,3,4,5]))
/python_practice/python_practice_1/python_practice_1_3.py
"""
Write a function that takes a list of numbers and returns the sum of all the numbers in the list.
"""

def sum_of_list(lst):
    return sum(lst)

print(sum_of_list([1,2,3,4,5]))
/python_practice/python_practice_1/python_practice_1_4.py
"""
Write a function that takes a list of numbers and returns the average (mean) of all the numbers in the list.
"""

def average_of_list(lst):
    return sum(lst)/len(lst)

print(average_of_list([1,2,3,4,5]))
/python_practice/python_practice_1/python_practice_1_5.py
"""
Write a function that takes a list of numbers and returns a new list with only the even numbers.
"""

def even_numbers(lst):
    return [x for x in lst if x%2==0]

print(even_numbers([1,2,3,4,5]))
/python_practice/python_practice_1/python_practice_1_6.py
"""
Write a function that takes a list of strings and returns a new list with all strings converted to upper case.
"""

def upper_case(lst):
    return [x.upper() for x in lst]

print(upper_case(['a','b','c','d','e']))
/python_practice/python_practice_1/python_practice_1_7.py
"""
Write a function that takes a list of numbers and returns a new list with only the odd numbers.
"""

def odd_numbers(lst):
    return [x for x in lst if x%2!=0]

print(odd_numbers([1,2,3,4,5]))
/python_practice/python_practice_1/python_practice_1_8.py
"""
Write a function that takes a list of numbers and returns a new list with only the prime numbers.
"""

def prime_numbers(lst):
    return [x for x in lst if x>1 and all(x%i!=0 for i in range(2,x))]

print(prime_numbers([1,2,3,4,5]))
/python_practice/python_practice_1/python_practice_1_9.py
"""
Write a function that takes a list of numbers and returns a new list with only the positive numbers.
"""

def positive_numbers(lst):
    return [x for x in lst if x>0]

print(positive_numbers([1,-2,3,-4,5]))
/python_practice/python_practice_1/python_practice_1_10.py
"""
Write a function that takes a list of numbers and returns a new list with only the negative numbers.
"""

def negative_numbers(lst):
    return [x for x in lst if x<0]

print(negative_numbers([1,-2,3,-4,5]))
/python_practice/python_practice_1/python_practice_1_11.py
"""
Write a function that takes a list of numbers and returns a new list with only the even numbers.
"""

def even_numbers(lst):
    return [x for x in lst if x%