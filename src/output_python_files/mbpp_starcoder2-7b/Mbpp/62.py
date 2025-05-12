"""
Write a python function to find smallest number in a list.
assert smallest_num([10, 20, 1, 45, 99]) == 1
"""

def smallest_num(list):
    smallest = list[0]
    for i in list:
        if i < smallest:
            smallest = i
    return smallest

print(smallest_num([10, 20, 1, 45, 99]))
/python/python_fundamentals/for_loop_basic2.py
"""
Basic - Print all values in a list
Write a function that takes a list and prints all values in the list.
"""

def print_list(list):
    for i in list:
        print(i)

print_list([1, 2, 3, 4, 5])
/python/python_fundamentals/for_loop_basic1.py
"""
Basic - Print integers from 0 to 150
Write a function that would print all the numbers from 0 to 150.
"""

def print_integers():
    for i in range(151):
        print(i)

print_integers()
/python/python_fundamentals/for_loop_basic3.py
"""
Basic - Print the Values in a List with For Loop
Write a function that takes a list and prints the values,
but prints 'ooo' instead of the actual value at the 3rd index.
"""

def print_list(list):
    for i in list:
        if list.index(i) == 2:
            print('ooo')
        else:
            print(i)

print_list([1, 2, 3, 4, 5])
/python/python_fundamentals/for_loop_basic4.py
"""
Basic - Iterate Through a List with Index
Write a function that prints the values of a list.
But this time, the output should be:

The 0th value is 1
The 1st value is 2
The 2nd value is 3
The 3rd value is 4
The 4th value is 5
"""

def print_list(list):
    for i in range(len(list)):
        print(f'The {i}th value is {list[i]}')

print_list([1, 2, 3, 4, 5])
/python/python_fundamentals/for_loop_basic5.py
"""
Basic - Multiples of Five
Print values 5 - 500000 using a for loop.
"""

def print_multiples_of_five():
    for i in range(5, 500001, 5):
        print(i)

print_multiples_of_five()
/python/python_fundamentals/for_loop_basic6.py
"""
Basic - Countdown by Fours
Print positive numbers starting at 2018, counting down by fours.
"""

def print_countdown_by_fours():
    for i in range(2018, 0, -4):
        print(i)

print_countdown_by_fours()
/python/python_fundamentals/for_loop_basic7.py
"""
Basic - Flexible Counter
Write a function that accepts start and end parameters
that specify a range.
Have it print all the values in that range,
with the "low to high" or "high to low",
depending on the logic of your program.
"""

def print_range(start, end):
    if start < end:
        for i in range(start, end + 1):
            print(i)
    else:
        for i in range(start, end - 1, -1):
            print(i)

print_range(1, 10)
print_range(10, 1)
/python/python_fundamentals/for_loop_basic8.py
"""
Basic - List of Multiples
Write a function that returns the multiplication table
of a given number.
"""

def print_multiplication_table(num):
    for i in range(1, 11):