"""
Write a function to find the ration of positive numbers in an array of integers.
assert positive_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8])==0.54
"""

def positive_count(arr):
    count = 0
    for i in arr:
        if i > 0:
            count += 1
    return count / len(arr)

print(positive_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8]))"""
Write a function that takes a list of numbers and returns the sum of the numbers.
assert sum_numbers([1, 2, 3, 4]) == 10
"""

def sum_numbers(arr):
    return sum(arr)

print(sum_numbers([1, 2, 3, 4]))"""
Write a function that takes a list of numbers and returns the largest number in the list.
assert largest_number([1, 2, 3, 4]) == 4
"""

def largest_number(arr):
    return max(arr)

print(largest_number([1, 2, 3, 4]))"""
Write a function that takes a list of numbers and returns the smallest number in the list.
assert smallest_number([1, 2, 3, 4]) == 1
"""

def smallest_number(arr):
    return min(arr)

print(smallest_number([1, 2, 3, 4]))"""
Write a function that takes a list of numbers and returns the average (mean) of the numbers.
assert average([1, 2, 3, 4]) == 2.5
"""

def average(arr):
    return sum(arr) / len(arr)

print(average([1, 2, 3, 4]))"""
Write a function that takes a list of numbers and returns the sum of all the even numbers in the list.
assert sum_even([1, 2, 3, 4]) == 6
"""

def sum_even(arr):
    sum = 0
    for i in arr:
        if i % 2 == 0:
            sum += i
    return sum

print(sum_even([1, 2, 3, 4]))"""
Write a function that takes a list of numbers and returns the sum of all the odd numbers in the list.
assert sum_odd([1, 2, 3, 4]) == 9
"""

def sum_odd(arr):
    sum = 0
    for i in arr:
        if i % 2!= 0:
            sum += i
    return sum

print(sum_odd([1, 2, 3, 4]))"""
Write a function that takes a list of numbers and returns the sum of all the negative numbers in the list.
assert sum_negative([1, 2, 3, -4]) == -4
"""

def sum_negative(arr):
    sum = 0
    for i in arr:
        if i < 0:
            sum += i
    return sum

print(sum_negative([1, 2, 3, -4]))"""
Write a function that takes a list of numbers and returns the sum of all the positive numbers in the list.
assert sum_positive([1, 2, 3, 4]) == 10
"""

def sum_positive(arr):
    sum = 0
    for i in arr:
        if i > 0:
            sum += i
    return sum

print(sum_positive([1, 2, 3, 4]))"""
Write a function that takes a list of numbers and returns the sum of all the negative numbers in the list.
assert sum_negative([1, 2, 3, -4]) == -4
"""

def sum_negative(arr):
    sum = 0
    for i in arr:
        if i < 0:
            sum += i
    return sum

print(sum_negative([1, 2, 3, -4]))"""
Write a function that takes a list of numbers and returns the sum of all the negative numbers in the list.
assert sum_negative([1, 2, 3, -4]) == -4
"""