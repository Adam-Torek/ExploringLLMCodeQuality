"""
Write a python function to find the last digit of a given number.
assert last_Digit(123) == 3
"""

def last_Digit(num):
    return num % 10

print(last_Digit(123))
<file_sep>/python/python_fundamentals/for_loop_basic_1.py
"""
Basic - Print all integers from 0 to 150.
"""

for i in range(0, 151):
    print(i)

"""
Basic II - Print all the multiples of 5 from 5 to 1,000
"""

for i in range(5, 1001, 5):
    print(i)

"""
Basic III - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
"""

for i in range(1, 101):
    if i % 10 == 0:
        print("Coding Dojo")
    elif i % 5 == 0:
        print("Coding")
    else:
        print(i)

"""
Basic IV - Add odd integers from 0 to 500,000, and print the final sum.
"""

sum = 0
for i in range(0, 500001, 2):
    sum += i
print(sum)

"""
Basic V - Print positive numbers starting at 2018, counting down by fours.
"""

for i in range(2018, 0, -4):
    print(i)

"""
FizzBuzz - Print numbers 1 to 100. If divisible by 3, print "Fizz" instead. If divisible by 5, print "Buzz". If divisible by both 3 and 5, print "FizzBuzz".
"""

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
<file_sep>/python/python_fundamentals/functions_intermediate_1.py
"""
Write a function that takes a list and returns a new list that contains all the values for which the function func returns True.

The function will take two parameters:

list: the list to iterate over
func: the function called per iteration
"""

def new_list(list, func):
    new_list = []
    for i in list:
        if func(i):
            new_list.append(i)
    return new_list

print(new_list([1, 2, 3, 4, 5, 6], lambda x: x > 3))

"""
Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False

Example:

greater_than_second([5,2,3,2,1,4]) should print 3 and return [5,3,4]
greater_than_second([3]) should return False
"""

def greater_than_second(list):
    if len(list) < 2:
        return False
    else:
        new_list = []
        for i in list:
            if i > list[1]:
                new_list.append(i)
        print(len(new_list))
        return new_list

print(greater_than_second([5,2,3,2,1,4]))

"""
Write a function that accepts any list and returns a new list containing only the values in the original list that are greater than a given value k. For example, filter_list([1,2,3,4,5], 3) should return [4,5].

Example:

filter_list([1,2,3,4,5], 3) should return [4,5]
filter_list([6,3,5], 2) should return [5]
"""

def filter_list(list, k):
    new_list = []
    for i in list:
        if i > k:
            new_list