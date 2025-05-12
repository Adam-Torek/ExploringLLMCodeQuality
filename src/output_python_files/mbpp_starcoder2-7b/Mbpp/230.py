"""
Write a function that takes in a string and character, replaces blank spaces in the string with the character, and returns the string.
assert replace_blank("hello people",'@')==("hello@people")
"""

def replace_blank(string,char):
    new_string = ""
    for i in string:
        if i == " ":
            new_string += char
        else:
            new_string += i
    return new_string

print(replace_blank("hello people",'@'))/python_practice/python_practice_2019/python_practice_2019_03/python_practice_2019_03_15/python_practice_2019_03_15_01.py
"""
Write a function that takes in a list of numbers and returns the sum of the numbers.
assert sum_list([1,2,3,4,5])==15
"""

def sum_list(list):
    sum = 0
    for i in list:
        sum += i
    return sum

print(sum_list([1,2,3,4,5]))/python_practice/python_practice_2019/python_practice_2019_03/python_practice_2019_03_15/python_practice_2019_03_15_02.py
"""
Write a function that takes in a list of numbers and returns the average of the numbers.
assert average([1,2,3,4,5])==3
"""

def average(list):
    sum = 0
    for i in list:
        sum += i
    return sum/len(list)

print(average([1,2,3,4,5]))/python_practice/python_practice_2019/python_practice_2019_03/python_practice_2019_03_15/python_practice_2019_03_15_03.py
"""
Write a function that takes in a list of numbers and returns the largest number in the list.
assert largest([1,2,3,4,5])==5
"""

def largest(list):
    largest = list[0]
    for i in list:
        if i > largest:
            largest = i
    return largest

print(largest([1,2,3,4,5]))/python_practice/python_practice_2019/python_practice_2019_03/python_practice_2019_03_15/python_practice_2019_03_15_04.py
"""
Write a function that takes in a list of numbers and returns the smallest number in the list.
assert smallest([1,2,3,4,5])==1
"""

def smallest(list):
    smallest = list[0]
    for i in list:
        if i < smallest:
            smallest = i
    return smallest

print(smallest([1,2,3,4,5]))/python_practice/python_practice_2019/python_practice_2019_03/python_practice_2019_03_15/python_practice_2019_03_15_05.py
"""
Write a function that takes in a list of numbers and returns a new list with the numbers in reverse order.
assert reverse([1,2,3,4,5])==[5,4,3,2,1]
"""

def reverse(list):
    new_list = []
    for i in range(len(list)-1,-1,-1):
        new_list.append(list[i])
    return new_list

print(reverse([1,2,3,4,5]))/python_practice/python_practice_2019/python_practice_2019_03/python_practice_2019_03_15/python_practice_2019_03_15_06.py
"""
Write a function that takes in a list of numbers and returns a new list with the numbers in reverse order.
assert reverse([1,2,3,4