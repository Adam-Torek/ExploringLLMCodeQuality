"""
Write a function to find the specified number of largest products from two given lists, selecting one factor from each list.
assert large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],3)==[60, 54, 50]
"""

def large_product(list1, list2, n):
    list1.sort()
    list2.sort()
    list1.reverse()
    list2.reverse()
    return [list1[i]*list2[i] for i in range(n)]

print(large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],3))/Python/Python_Basics/Python_Basics_1.py
"""
Write a function that takes a list of numbers and returns the sum of the numbers.
assert sum_list([1,2,3,4])==10
"""

def sum_list(list):
    return sum(list)

print(sum_list([1,2,3,4]))/Python/Python_Basics/Python_Basics_10.py
"""
Write a function that takes a list of numbers and returns the largest number in the list.
assert largest_number([1,2,3,4])==4
"""

def largest_number(list):
    return max(list)

print(largest_number([1,2,3,4]))/Python/Python_Basics/Python_Basics_12.py
"""
Write a function that takes a list of numbers and returns the smallest number in the list.
assert smallest_number([1,2,3,4])==1
"""

def smallest_number(list):
    return min(list)

print(smallest_number([1,2,3,4]))/Python/Python_Basics/Python_Basics_11.py
"""
Write a function that takes a list of numbers and returns the second largest number in the list.
assert second_largest([1,2,3,4])==3
"""

def second_largest(list):
    list.sort()
    list.reverse()
    return list[1]

print(second_largest([1,2,3,4]))/Python/Python_Basics/Python_Basics_13.py
"""
Write a function that takes a list of numbers and returns the second smallest number in the list.
assert second_smallest([1,2,3,4])==2
"""

def second_smallest(list):
    list.sort()
    return list[1]

print(second_smallest([1,2,3,4]))/Python/Python_Basics/Python_Basics_14.py
"""
Write a function that takes a list of numbers and returns the sum of all the numbers in the list.
assert sum_list([1,2,3,4])==10
"""

def sum_list(list):
    return sum(list)

print(sum_list([1,2,3,4]))/Python/Python_Basics/Python_Basics_15.py
"""
Write a function that takes a list of numbers and returns the average (mean) of all the numbers in the list.
assert average([1,2,3,4])==2.5
"""

def average(list):
    return sum(list)/len(list)

print(average([1,2,3,4]))/Python/Python_Basics/Python_Basics_16.py
"""
Write a function that takes a list of numbers and returns the product of all the numbers in the list.
assert product([1,2,3,4])==24
"""

def product(list):
    return reduce(lambda x,y:x*y,list)

print(product([1,2,3,4]))/Python/Python_Basics/Python_Basics_17.py
"""
Write a function that takes a list of numbers and returns the product of all the numbers in the list.
assert product([1,2,3,4])==24
"""

def product(list):
    return reduce(lambda x,y:x*y,list)

print(product([1,2,3,4]))/Python/Python_Basics/Python_Basics_18.py
"""
Write