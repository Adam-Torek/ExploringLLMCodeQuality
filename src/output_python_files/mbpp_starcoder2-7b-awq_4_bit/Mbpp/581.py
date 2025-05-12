"""
Write a python function to find the surface area of a square pyramid with a given base edge and height.
assert surface_Area(3,4) == 33
"""

def surface_Area(base, height):
    return (base**2 + base*height)

print(surface_Area(3,4))/python/python_fundamentals/for_loop_basic2.py
"""
Create a function that prints all the odd numbers from 1 to 2000. Use the for loop and don't use any var in your code.
"""

def odd_numbers():
    for i in range(1, 2001, 2):
        print(i)

odd_numbers()/python/python_fundamentals/for_loop_basic1.py
"""
Create a function that prints all the integers from 0 to 1000. Use the for loop and don't use any var in your code.
"""

def integers_to_1000():
    for i in range(0, 1001):
        print(i)

integers_to_1000()/python/python_fundamentals/for_loop_basic3.py
"""
Create a function that prints the multiples of 5 from 5 to 1,000,000. Use the for loop and don't use any var in your code.
"""

def multiples_of_5():
    for i in range(5, 1000001, 5):
        print(i)

multiples_of_5()/python/python_fundamentals/for_loop_basic4.py
"""
Print the sum of all the values in the list: a = [1, 2, 5, 10, 255, 3]
"""

a = [1, 2, 5, 10, 255, 3]

def sum_list(list):
    sum = 0
    for i in list:
        sum += i
    print(sum)

sum_list(a)/python/python_fundamentals/for_loop_basic5.py
"""
Print the average of the values in the list: a = [1, 2, 5, 10, 255, 3]
"""

a = [1, 2, 5, 10, 255, 3]

def average_list(list):
    sum = 0
    for i in list:
        sum += i
    print(sum/len(list))

average_list(a)/python/python_fundamentals/for_loop_basic6.py
"""
Print the length of the list: a = [1, 2, 5, 10, 255, 3]
"""

a = [1, 2, 5, 10, 255, 3]

def length_list(list):
    print(len(list))

length_list(a)/python/python_fundamentals/for_loop_basic7.py
"""
Print the minimum value of the list: a = [1, 2, 5, 10, 255, 3]
"""

a = [1, 2, 5, 10, 255, 3]

def minimum_list(list):
    min = list[0]
    for i in list:
        if i < min:
            min = i
    print(min)

minimum_list(a)/python/python_fundamentals/for_loop_basic8.py
"""
Print the maximum value of the list: a = [1, 2, 5, 10, 255, 3]
"""

a = [1, 2, 5, 10, 255, 3]

def maximum_list(list):
    max = list[0]
    for i in list:
        if i > max:
            max = i
    print(max)

maximum_list(a)/python/python_fundamentals/for_loop_basic9.py
"""
Print the sum of all the values in the list: a = [1, 2, 5, 10