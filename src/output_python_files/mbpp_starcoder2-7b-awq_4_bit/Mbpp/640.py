"""
Write a function to remove the parenthesis and what is inbetween them from a string.
assert remove_parenthesis(["python (chrome)"])==("python")
"""

def remove_parenthesis(string):
    return string[string.find("(")+1:string.find(")")]

print(remove_parenthesis("python (chrome)"))
/python/python_basics/python_basics_001.py
"""
Write a function that takes a list of numbers and returns the sum of the numbers.
assert sum_list([1,2,3,4,5])==15
"""

def sum_list(list):
    return sum(list)

print(sum_list([1,2,3,4,5]))
/python/python_basics/python_basics_004.py
"""
Write a function that takes a list of numbers and returns the largest number in the list.
assert largest_number([1,2,3,4,5])==5
"""

def largest_number(list):
    return max(list)

print(largest_number([1,2,3,4,5]))
/python/python_basics/python_basics_005.py
"""
Write a function that takes a list of numbers and returns the smallest number in the list.
assert smallest_number([1,2,3,4,5])==1
"""

def smallest_number(list):
    return min(list)

print(smallest_number([1,2,3,4,5]))
/python/python_basics/python_basics_002.py
"""
Write a function that takes a list of numbers and returns the average (the sum divided by the number of elements).
assert average([1,2,3,4,5])==3
"""

def average(list):
    return sum(list)/len(list)

print(average([1,2,3,4,5]))
/python/python_basics/python_basics_003.py
"""
Write a function that takes a list of numbers and returns True if all of the numbers are positive numbers and False otherwise.
assert all_positive([1,2,3,4,5])==True
assert all_positive([1,-2,3,4,5])==False
"""

def all_positive(list):
    for i in list:
        if i<0:
            return False
    return True

print(all_positive([1,2,3,4,5]))
print(all_positive([1,-2,3,4,5]))
/python/python_basics/python_basics_006.py
"""
Write a function that takes a list of numbers and returns True if all of the numbers are even numbers and False otherwise.
assert all_even([1,2,3,4,5])==False
assert all_even([2,4,6,8,10])==True
"""

def all_even(list):
    for i in list:
        if i%2!=0:
            return False
    return True

print(all_even([1,2,3,4,5]))
print(all_even([2,4,6,8,10]))
/python/python_basics/python_basics_007.py
"""
Write a function that takes a list of numbers and returns True if all of the numbers are odd numbers and False otherwise.
assert all_odd([1,3,5,7,9])==True
assert all_odd([2,4,6,8,10])==False
"""

def all_odd(list):
    for i in list:
        if i%2==0:
            return False
    return True

print(all_odd([1,3,5,7,9]))
print(all_odd([2,4,6,8,10]))
/python/python_basics/python_basics_008.py
"""
Write a function that takes a list of numbers and returns True if any of the numbers are even numbers and False otherwise.
assert any_even([1,3,5,7,9])==False
assert any_even([2,4,6,8,10])==True
"""

def any_even(list):
    for i in list:
        if i