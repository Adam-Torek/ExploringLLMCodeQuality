"""
Write a function to check whether it follows the sequence given in the patterns array.
assert is_samepatterns(["red","green","green"], ["a", "b", "b"])==True
"""

def is_samepatterns(patterns, sequence):
    for i in range(len(patterns)):
        if patterns[i]!= sequence[i]:
            return False
    return True

print(is_samepatterns(["red","green","green"], ["a", "b", "b"]))
<file_sep>/python/python_basics/python_basics_01.py
"""
Write a function that takes a list of numbers and returns the sum of the numbers.
assert sum_numbers([1,2,3,4])==10
"""

def sum_numbers(numbers):
    sum = 0
    for i in numbers:
        sum += i
    return sum

print(sum_numbers([1,2,3,4]))
<file_sep>/python/python_basics/python_basics_02.py
"""
Write a function that takes a list of numbers and returns the largest number in the list.
assert largest_number([1,2,3,4])==4
"""

def largest_number(numbers):
    largest = numbers[0]
    for i in numbers:
        if i > largest:
            largest = i
    return largest

print(largest_number([1,2,3,4]))
<file_sep>/python/python_basics/python_basics_03.py
"""
Write a function that takes a list of numbers and returns a new list with only the odd numbers.
assert odd_numbers([1,2,3,4])==[1,3]
"""

def odd_numbers(numbers):
    odd_list = []
    for i in numbers:
        if i % 2!= 0:
            odd_list.append(i)
    return odd_list

print(odd_numbers([1,2,3,4]))
<file_sep>/python/python_basics/python_basics_04.py
"""
Write a function that takes a list of numbers and returns a new list with only the even numbers.
assert even_numbers([1,2,3,4])==[2,4]
"""

def even_numbers(numbers):
    even_list = []
    for i in numbers:
        if i % 2 == 0:
            even_list.append(i)
    return even_list

print(even_numbers([1,2,3,4]))
<file_sep>/python/python_basics/python_basics_05.py
"""
Write a function that takes a list of numbers and returns a new list with only the positive numbers.
assert positive_numbers([1,-2,3,-4])==[1,3]
"""

def positive_numbers(numbers):
    positive_list = []
    for i in numbers:
        if i > 0:
            positive_list.append(i)
    return positive_list

print(positive_numbers([1,-2,3,-4]))
<file_sep>/python/python_basics/python_basics_06.py
"""
Write a function that takes a list of numbers and returns a new list with only the negative numbers.
assert negative_numbers([1,-2,3,-4])==[-2,-4]
"""

def negative_numbers(numbers):
    negative_list = []
    for i in numbers:
        if i < 0:
            negative_list.append(i)
    return negative_list

print(negative_numbers([1,-2,3,-4]))
<file_sep>/python/python_basics/python_basics_07.py
"""
Write a function that takes a list of numbers and returns a new list with only the unique numbers.
assert unique_numbers([1,1,1,1,2,2,2,2,3,3,3,3])==[1,2,3]
"""

def unique_numbers(numbers):
    unique_list = []
    for i in numbers:
        if i not in unique_list:
            unique_list.append(i)
    return unique_list

print(unique_numbers([1,1,1,1,2,2,2,2,3,3,3,3]))
<file_sep>/python/python_basics/python_basics_08.py
"""
Write a function that takes a list of numbers and returns a new list with only the even numbers.
assert unique_numbers([1,1,1,1,2,2,2,2,3,3,3,3