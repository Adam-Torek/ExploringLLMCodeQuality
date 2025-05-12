"""
Write a function to calculate the sum of the negative numbers of a given list of numbers.
assert sum_negativenum([2, 4, -6, -9, 11, -12, 14, -5, 17])==-32
"""

def sum_negativenum(list):
    sum = 0
    for i in list:
        if i < 0:
            sum += i
    return sum

print(sum_negativenum([2, 4, -6, -9, 11, -12, 14, -5, 17]))
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
Create a function that prints all the integers from 0 to 1000. Use the for loop and don't use any var in your code.
"""

def int_num():
    for i in range(0, 1001):
        print(i)

int_num()
/python/python_fundamentals/for_loop_basic3.py
"""
Create a function that prints all the multiples of 5 from 5 to 1,000,000. Use the for loop and don't use any var in your code.
"""

def mult_5():
    for i in range(5, 1000001, 5):
        print(i)

mult_5()
/python/python_fundamentals/for_loop_basic4.py
"""
Print the sum of all the values in the list: a = [1, 2, 5, 10, 255, 3]
"""

def sum_list(list):
    sum = 0
    for i in list:
        sum += i
    return sum

print(sum_list([1, 2, 5, 10, 255, 3]))
/python/python_fundamentals/for_loop_basic5.py
"""
Print the average of the values in the list: a = [1, 2, 5, 10, 255, 3]
"""

def avg_list(list):
    sum = 0
    for i in list:
        sum += i
    return sum / len(list)

print(avg_list([1, 2, 5, 10, 255, 3]))
/python/python_fundamentals/for_loop_basic6.py
"""
Print the length of the list: a = [1, 2, 5, 10, 255, 3]
"""

def len_list(list):
    return len(list)

print(len_list([1, 2, 5, 10, 255, 3]))
/python/python_fundamentals/for_loop_basic7.py
"""
Print the minimum value of the list: a = [1, 2, 5, 10, 255, 3]
"""

def min_list(list):
    min = list[0]
    for i in list:
        if i < min:
            min = i
    return min

print(min_list([1, 2, 5, 10, 255, 3]))
/python/python_fundamentals/for_loop_basic8.py
"""
Print the maximum value of the list: a = [1, 2, 5, 10, 255, 3]
"""

def max_list(list):
    max = list[0]
    for i in list:
        if i > max:
            max = i
    return max

print(max_list([1, 2, 5, 10, 255, 3]))
/python/python_fundamentals/for_loop_