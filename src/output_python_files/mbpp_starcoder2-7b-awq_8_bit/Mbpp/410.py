"""
Write a function to find the minimum value in a given heterogeneous list.
assert min_val(['Python', 3, 2, 4, 5,'version'])==2
"""

def min_val(lst):
    min_val = lst[0]
    for i in lst:
        if type(i) == int:
            if i < min_val:
                min_val = i
    return min_val

print(min_val(['Python', 3, 2, 4, 5,'version']))/python_fundamentals/functions_intermediate1/multiply.py
"""
Write a function called'multiply' that iterates through each value in a list
and returns a list where each value has been multiplied by 5.
"""

def multiply(lst):
    new_lst = []
    for i in lst:
        new_lst.append(i * 5)
    return new_lst

print(multiply([1,2,3]))/python_fundamentals/functions_intermediate1/count_positives.py
"""
Write a function that counts the number of values in a list that are greater than
zero.
"""

def count_positives(lst):
    count = 0
    for i in lst:
        if i > 0:
            count += 1
    return count

print(count_positives([1,2,3,4,5,6,7,8,9,10]))/python_fundamentals/functions_intermediate1/reverse_list.py
"""
Write a function that reverses a list.
"""

def reverse_list(lst):
    new_lst = []
    for i in range(len(lst)):
        new_lst.append(lst[len(lst) - 1 - i])
    return new_lst

print(reverse_list([1,2,3,4,5,6,7,8,9,10]))/python_fundamentals/functions_intermediate1/find_characters.py
"""
Write a function that takes a list of strings and a string containing a single
character, and returns a list of all the strings from the list that contain the
character in the string at least once.
"""

def find_characters(lst, char):
    new_lst = []
    for i in lst:
        if char in i:
            new_lst.append(i)
    return new_lst

print(find_characters(['hello', 'world','my', 'name', 'is', 'Anna'], 'o'))/python_fundamentals/functions_intermediate1/layered_multiples.py
"""
Write a function that takes a list and returns a list of the same length where
each value is the product of all the values in the original list.
"""

def layered_multiples(lst):
    new_lst = []
    for i in lst:
        new_lst.append([1] * i)
    return new_lst

print(layered_multiples([1,2,3,4,5]))/python_fundamentals/functions_intermediate1/multiply_list.py
"""
Write a function that takes a list and returns a new list with values
multiplied by 10.
"""

def multiply_list(lst):
    new_lst = []
    for i in lst:
        new_lst.append(i * 10)
    return new_lst

print(multiply_list([1,2,3,4,5,6,7,8,9,10]))/python_fundamentals/functions_intermediate1/odd_even.py
"""
Write a function that counts from 1 to 2000. As it counts, have your program
print the number of that iteration and specify whether it's an odd or even number.
"""

def odd_even():
    for i in range(1, 2001):
        if i % 2 == 0:
            print(f"Number is {i}. This is an even number.")
        else:
            print(f"Number is {i}. This is an odd number.")

odd_even()/python_fundamentals/functions_intermediate1/greater_than_y.py
"""
Write a function that takes a list and an integer as arguments. Return a new
list that contains only the values from the original list that are greater than
the value of the integer.
"""

def greater_than_y(lst, y):
    new_lst = []
    for i in lst:
        if