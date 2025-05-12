"""
Write a function that takes two lists and returns true if they have at least one common element.
assert common_element([1,2,3,4,5], [5,6,7,8,9])==True
"""

def common_element(list1, list2):
    for i in list1:
        if i in list2:
            return True
    return False

print(common_element([1,2,3,4,5], [5,6,7,8,9]))
/python/python_fundamentals/for_loop_basic2.py
"""
Create a function that prints all the odd numbers from 1 to 1000. Use the for loop and don't use any var in your code.
"""

def odd_numbers():
    for i in range(1, 1001, 2):
        print(i)

odd_numbers()
/python/python_fundamentals/for_loop_basic1.py
"""
Create a function that prints all the integers from 0 to 1000. Use the for loop and don't use any var in your code.
"""

def integers_to_1000():
    for i in range(0, 1001):
        print(i)

integers_to_1000()
/python/python_fundamentals/for_loop_basic3.py
"""
Create a function that prints all the multiples of 5 from 5 to 1,000,000. Use the for loop and don't use any var in your code.
"""

def multiples_of_5():
    for i in range(5, 1000001, 5):
        print(i)

multiples_of_5()
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

def average_list(list):
    sum = 0
    for i in list:
        sum += i
    return sum / len(list)

print(average_list([1, 2, 5, 10, 255, 3]))
/python/python_fundamentals/for_loop_basic6.py
"""
Create a function that prints the maximum, minimum and average values in a list.
"""

def max_min_avg(list):
    max = list[0]
    min = list[0]
    sum = 0
    for i in list:
        if i > max:
            max = i
        if i < min:
            min = i
        sum += i
    return max, min, sum / len(list)

print(max_min_avg([1, 2, 5, 10, 255, 3]))
/python/python_fundamentals/for_loop_basic7.py
"""
Create a function that prints the first 50 multiples of 3.
"""

def multiples_of_3():
    for i in range(1, 51):
        print(i * 3)

multiples_of_3()
/python/python_fundamentals/for_loop_basic8.py
"""
Create a function that prints the first 50 multiples of 5.
"""

def multiples_of_5():
    for i in range(1, 51):
        print(i * 5)

multiples_of_5()
/python/python_fundamentals/for_loop_basic9.py
"""
Create a function that prints the odd numbers from 1 to 1000.
"""

def odd_numbers():
    for i in range(1, 1001, 2):
        print(i)

odd_numbers()
/python/python_fundamentals/for_