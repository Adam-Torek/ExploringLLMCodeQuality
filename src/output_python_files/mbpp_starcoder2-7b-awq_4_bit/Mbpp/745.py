"""
Write a function to find numbers within a given range from startnum ti endnum where every number is divisible by every digit it contains. https://www.w3resource.com/python-exercises/lambda/python-lambda-exercise-24.php
assert divisible_by_digits(1,22)==[1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
"""

def divisible_by_digits(startnum, endnum):
    return [i for i in range(startnum, endnum+1) if all(i%int(j)==0 for j in str(i))]

print(divisible_by_digits(1,22))/Python/Python_Basics/Python_Basics_10.py
"""
Write a function to find the maximum and minimum numbers from a sequence of numbers. https://www.w3resource.com/python-exercises/python-basic-exercises-on-sequences-and-sets/python-basic-exercise-sequence-10.php
assert max_min([1,2,3,4,5])==[5,1]
"""

def max_min(seq):
    return [max(seq), min(seq)]

print(max_min([1,2,3,4,5]))/Python/Python_Basics/Python_Basics_12.py
"""
Write a function to find the sum of the elements of set0. https://www.w3resource.com/python-exercises/python-basic-exercises-on-sequences-and-sets/python-basic-exercise-sequence-12.php
assert sum_set([1,2,3,4,5])==15
"""

def sum_set(set0):
    return sum(set0)

print(sum_set([1,2,3,4,5]))/Python/Python_Basics/Python_Basics_13.py
"""
Write a function to find the elements that are not common to the two given lists. https://www.w3resource.com/python-exercises/python-basic-exercises-on-sequences-and-sets/python-basic-exercise-sequence-13.php
assert not_common([1,2,3,4,5],[5,6,7,8,9])==[1,2,3,4]
"""

def not_common(list1, list2):
    return [i for i in list1 if i not in list2]

print(not_common([1,2,3,4,5],[5,6,7,8,9]))/Python/Python_Basics/Python_Basics_11.py
"""
Write a function to find the sum of the elements of set0. https://www.w3resource.com/python-exercises/python-basic-exercises-on-sequences-and-sets/python-basic-exercise-sequence-11.php
assert sum_set([1,2,3,4,5])==15
"""

def sum_set(set0):
    return sum(set0)

print(sum_set([1,2,3,4,5]))/Python/Python_Basics/Python_Basics_14.py
"""
Write a function to find the elements that are not common to the two given lists. https://www.w3resource.com/python-exercises/python-basic-exercises-on-sequences-and-sets/python-basic-exercise-sequence-14.php
assert not_common([1,2,3,4,5],[5,6,7,8,9])==[1,2,3,4]
"""

def not_common(list1, list2):
    return [i for i in list1 if i not in list2]

print(not_common([1,2,3,4,5],[5,6,7,8,9]))/Python/Python_Basics/Python_Basics_15.py
"""
Write a function to find the elements that are common to the two given lists. https://www.w3resource.com/python-exercises/python-basic-exercises-on-sequences-and-sets/python-basic-exercise-sequence-15.php
assert common([1,2,3,4,5],[5,6,7,8,9])==[5]