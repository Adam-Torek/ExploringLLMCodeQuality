"""
Write a python function to count the number of positive numbers in a list.
assert pos_count([1,-2,3,-4]) == 2
"""

def pos_count(lst):
    count = 0
    for i in lst:
        if i > 0:
            count += 1
    return count

print(pos_count([1,-2,3,-4]))
/python/python_fundamentals/for_loop_basic2.py
"""
Create a function that prints all the odd numbers from 1 to 2000. Use the for loop and don't use any var in your code.
"""

def odd_num():
    for i in range(1, 2001, 2):
        print(i)

odd_num()
/python/python_fundamentals/for_loop_basic1.py
"""
Write a function that prints all the integers from 0 to 150.
"""

def print_to_150():
    for i in range(151):
        print(i)

print_to_150()
/python/python_fundamentals/for_loop_basic3.py
"""
Write a function that prints the multiples of 5 from 5 to 1,000,000.
"""

def print_multiples_5():
    for i in range(5, 1000001, 5):
        print(i)

print_multiples_5()
/python/python_fundamentals/for_loop_basic4.py
"""
Print the sum of all the values in the list: a = [1, 2, 5, 10, 255, 3]
"""

def sum_list(lst):
    sum = 0
    for i in lst:
        sum += i
    return sum

print(sum_list([1, 2, 5, 10, 255, 3]))
/python/python_fundamentals/for_loop_basic5.py
"""
Print the average of the values in the list: a = [1, 2, 5, 10, 255, 3]
"""

def avg_list(lst):
    sum = 0
    for i in lst:
        sum += i
    return sum / len(lst)

print(avg_list([1, 2, 5, 10, 255, 3]))
/python/python_fundamentals/for_loop_basic6.py
"""
Write a function that prints all the multiples of 6 from 6 to 1,000,000.
"""

def print_multiples_6():
    for i in range(6, 1000001, 6):
        print(i)

print_multiples_6()
/python/python_fundamentals/for_loop_basic7.py
"""
Write a function that prints the sum of all the values in the list: a = [1, 2, 5, 10, 255, 3]
"""

def sum_list(lst):
    sum = 0
    for i in lst:
        sum += i
    return sum

print(sum_list([1, 2, 5, 10, 255, 3]))
/python/python_fundamentals/for_loop_basic8.py
"""
Write a function that prints the average of the values in the list: a = [1, 2, 5, 10, 255, 3]
"""

def avg_list(lst):
    sum = 0
    for i in lst:
        sum += i
    return sum / len(lst)

print(avg_list([1, 2, 5, 10, 255, 3]))
/python/python_fundamentals/for_loop_basic9.py
"""
Write a function that prints the average of the values in the list: a = [1, 2, 5, 10, 255, 3]
"""

def avg_list(lst):
    sum = 0
    for i in lst:
        sum += i
    return sum / len(lst)

print(avg_list([1, 2, 5, 10, 255, 3