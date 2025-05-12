"""
Write a function to create a list of N empty dictionaries.
assert empty_list(5)==[{},{},{},{},{}]
"""

def empty_list(n):
    return [{} for i in range(n)]

print(empty_list(5))
/python/python_fundamentals/for_loop_basic2.py
"""
Basic - Print all integers from 0 to 150.
"""

for i in range(151):
    print(i)

"""
Multiples of Five - Print all the multiples of 5 from 5 to 1,000
"""

for i in range(5, 1001, 5):
    print(i)

"""
Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
"""

for i in range(1, 101):
    if i % 10 == 0:
        print("Coding Dojo")
    elif i % 5 == 0:
        print("Coding")
    else:
        print(i)

"""
Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
"""

sum = 0
for i in range(500001):
    if i % 2!= 0:
        sum += i
print(sum)

"""
Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
"""

for i in range(2018, 0, -4):
    print(i)

"""
Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)
"""

lowNum = 2
highNum = 9
mult = 3
for i in range(lowNum, highNum + 1):
    if i % mult == 0:
        print(i)
/python/python_fundamentals/functions_intermediate1.py
"""
Countdown - Create a function that accepts a number as an input. Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).
"""

def countdown(num):
    new_list = []
    for i in range(num, -1, -1):
        new_list.append(i)
    return new_list

print(countdown(5))

"""
Print and Return - Create a function that will receive a list with two numbers. Print the first value and return the second.
"""

def print_and_return(list):
    print(list[0])
    return list[1]

print(print_and_return([1, 2]))

"""
First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.
"""

def first_plus_length(list):
    return list[0] + len(list)

print(first_plus_length([1, 2, 3, 4, 5]))

"""
Values Greater than Second - Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False
"""

def values_greater_than_second(list):
    if len(list) < 2:
        return False
    new_list = []
    for i in range(len(list)):
        if list[i] > list[1]:
            new_list.append(list[i])
    print(len(new_list))
    return new_list

print(values_greater_than_second([5, 2, 3, 2, 1, 4]))

"""
This Length, That Value - Write a function that accepts two integers as parameters: size and value. The function should create and return a list