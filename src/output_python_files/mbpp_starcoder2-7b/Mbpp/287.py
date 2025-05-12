"""
Write a python function takes in an integer n and returns the sum of squares of first n even natural numbers.
assert square_Sum(2) == 20
"""

def square_Sum(n):
    sum = 0
    for i in range(1,n+1):
        sum += i**2
    return sum

print(square_Sum(2))/Python/Python_Basics/Python_Basics_1/Python_Basics_1_1.py
"""
Write a python function takes in a list of numbers and returns the sum of all the numbers.
assert sum_List([1,2,3,4,5]) == 15
"""

def sum_List(list):
    sum = 0
    for i in list:
        sum += i
    return sum

print(sum_List([1,2,3,4,5]))/Python/Python_Basics/Python_Basics_1/Python_Basics_1_2.py
"""
Write a python function takes in a list of numbers and returns the average of all the numbers.
assert average_List([1,2,3,4,5]) == 3
"""

def average_List(list):
    sum = 0
    for i in list:
        sum += i
    return sum/len(list)

print(average_List([1,2,3,4,5]))/Python/Python_Basics/Python_Basics_1/Python_Basics_1_3.py
"""
Write a python function takes in a list of numbers and returns the largest number.
assert largest_Number([1,2,3,4,5]) == 5
"""

def largest_Number(list):
    largest = list[0]
    for i in list:
        if i > largest:
            largest = i
    return largest

print(largest_Number([1,2,3,4,5]))/Python/Python_Basics/Python_Basics_1/Python_Basics_1_4.py
"""
Write a python function takes in a list of numbers and returns the smallest number.
assert smallest_Number([1,2,3,4,5]) == 1
"""

def smallest_Number(list):
    smallest = list[0]
    for i in list:
        if i < smallest:
            smallest = i
    return smallest

print(smallest_Number([1,2,3,4,5]))/Python/Python_Basics/Python_Basics_1/Python_Basics_1_5.py
"""
Write a python function takes in a list of numbers and returns the second largest number.
assert second_Largest_Number([1,2,3,4,5]) == 4
"""

def second_Largest_Number(list):
    largest = list[0]
    second_largest = list[0]
    for i in list:
        if i > largest:
            second_largest = largest
            largest = i
        elif i > second_largest:
            second_largest = i
    return second_largest

print(second_Largest_Number([1,2,3,4,5]))/Python/Python_Basics/Python_Basics_1/Python_Basics_1_6.py
"""
Write a python function takes in a list of numbers and returns the second smallest number.
assert second_Smallest_Number([1,2,3,4,5]) == 2
"""

def second_Smallest_Number(list):
    smallest = list[0]
    second_smallest = list[0]
    for i in list:
        if i < smallest:
            second_smallest = smallest
            smallest = i
        elif i < second_smallest:
            second_smallest = i
    return second_smallest

print(second_Smallest_Number([1,2,3,4,5]))/Python/Python_Basics/Python_Basics_1/Python_Basics_1_7.py
"""
Write a python function takes in a list of numbers and returns the second largest number.
assert second_Largest_Number([1,2,3,4,5]) == 4
"""

def second_Largest_Number(list):
    largest = list[0]
    second_largest = list[0]
    for i in list:
        if i > largest:
            second_largest = largest
            largest = i
        elif i > second_largest:
            second_largest = i