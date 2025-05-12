"""
Write a python function to find the surface area of a square pyramid with a given base edge and height.
assert surface_Area(3,4) == 33
"""

def surface_Area(base, height):
    return (base * base) + (base * height * 4)

print(surface_Area(3,4))
/python/python_fundamentals/for_loop_basic2.py
"""
Create a function that prints all the odd numbers from 1 to 2000. Use the for loop and don't use any var in your code.
"""

def odd_numbers():
    for i in range(1, 2001, 2):
        print(i)

odd_numbers()
/python/python_fundamentals/for_loop_basic1.py
"""
Create a function that prints all the integers from 0 to 2000. Use the for loop and don't use any var in your code.
"""

def integers():
    for i in range(0, 2001):
        print(i)

integers()
/python/python_fundamentals/for_loop_basic3.py
"""
Create a function that prints the multiples of 5 from 5 to 1,000,000. Use the for loop and don't use any var in your code.
"""

def multiples_of_five():
    for i in range(5, 1000001, 5):
        print(i)

multiples_of_five()
/python/python_fundamentals/for_loop_basic4.py
"""
Print the sum of all the values in the list: a = [1, 2, 5, 10, 255, 3]
"""

def sum_list(a):
    sum = 0
    for i in a:
        sum += i
    print(sum)

a = [1, 2, 5, 10, 255, 3]
sum_list(a)
/python/python_fundamentals/for_loop_basic5.py
"""
Print the average of the values in the list: a = [1, 2, 5, 10, 255, 3]
"""

def average_list(a):
    sum = 0
    for i in a:
        sum += i
    print(sum / len(a))

a = [1, 2, 5, 10, 255, 3]
average_list(a)
/python/python_fundamentals/for_loop_basic6.py
"""
Print the min and max values in the list: a = [1, 2, 5, 10, 255, 3]
"""

def min_max_list(a):
    min = a[0]
    max = a[0]
    for i in a:
        if i < min:
            min = i
        if i > max:
            max = i
    print(min, max)

a = [1, 2, 5, 10, 255, 3]
min_max_list(a)
/python/python_fundamentals/for_loop_basic7.py
"""
Print the sum of all the values in the list: a = [1, 2, 5, 10, 255, 3]
"""

def sum_list(a):
    sum = 0
    for i in a:
        sum += i
    print(sum)

a = [1, 2, 5, 10, 255, 3]
sum_list(a)
/python/python_fundamentals/for_loop_basic8.py
"""
Print the average of all the values in the list: a = [1, 2, 5, 10, 255, 3]
"""

def average_list(a):
    sum = 0
    for i in a:
        sum += i
    print(sum / len(a))

a = [1, 2, 5, 10, 255, 3]
average_list(a)
/python/python_fundamentals/for_loop_basic9.py
"""
Print the average of all the values in the list: a = [1