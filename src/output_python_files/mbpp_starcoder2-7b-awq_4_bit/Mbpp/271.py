"""
Write a python function that takes in an integer n and finds the sum of the first n even natural numbers that are raised to the fifth power.
assert even_Power_Sum(2) == 1056
"""

def even_Power_Sum(n):
    sum = 0
    for i in range(2, n+1, 2):
        sum += i**5
    return sum

print(even_Power_Sum(2))
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
Create a function that prints all the integers from 0 to 150.
"""

def print_num():
    for i in range(151):
        print(i)

print_num()
/python/python_fundamentals/for_loop_basic3.py
"""
Create a function that prints the integers from 0 to 100 that are divisible by 5.
"""

def div_5():
    for i in range(101):
        if i % 5 == 0:
            print(i)

div_5()
/python/python_fundamentals/for_loop_basic4.py
"""
Create a function that prints all the multiples of 5 from 5 to 1,000,000.
"""

def mult_5():
    for i in range(5, 1000001, 5):
        print(i)

mult_5()
/python/python_fundamentals/for_loop_basic5.py
"""
Print the sum of all the values in the list: a = [1, 2, 5, 10, 255, 3]
"""

def sum_list(a):
    sum = 0
    for i in a:
        sum += i
    return sum

print(sum_list([1, 2, 5, 10, 255, 3]))
/python/python_fundamentals/for_loop_basic6.py
"""
Print the average of the values in the list: a = [1, 2, 5, 10, 255, 3]
"""

def avg_list(a):
    sum = 0
    for i in a:
        sum += i
    return sum / len(a)

print(avg_list([1, 2, 5, 10, 255, 3]))
/python/python_fundamentals/for_loop_basic7.py
"""
Create a function that prints the odd numbers from 1 to 1000. Use the for loop and don't use any var in your code.
"""

def odd_num():
    for i in range(1, 1001, 2):
        print(i)

odd_num()
/python/python_fundamentals/for_loop_basic8.py
"""
Create a function that prints the multiples of 6 from 6 to 1,000,000.
"""

def mult_6():
    for i in range(6, 1000001, 6):
        print(i)

mult_6()
/python/python_fundamentals/for_loop_basic9.py
"""
Create a function that prints the multiples of 5 from 5 to 1,000,000. Use the for loop and don't use any var in your code.
"""

def mult_5():
    for i in range(5, 1000001, 5):
        print(i)

mult_5()
/python/python_fundamentals/for_loop_basic10.py
"""
Create a function that prints the multiples of 12 from 12 to 100. Use the for loop and don't use any var in your code.