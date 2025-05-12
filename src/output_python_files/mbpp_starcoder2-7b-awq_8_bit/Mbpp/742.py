"""
Write a function to caluclate the area of a tetrahedron.
assert area_tetrahedron(3)==15.588457268119894
"""

def area_tetrahedron(a):
    return (a**2*sqrt(3))/4

print(area_tetrahedron(3))
/python/python_fundamentals/for_loop_basic2.py
"""
Write a function that counts from 1 to 2000.
"""

def count_to_2000():
    for i in range(1, 2001):
        print(i)

count_to_2000()
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
Write a function that prints all the multiples of 5 from 5 to 1,000,000.
"""

def print_multiples_5():
    for i in range(5, 1000001, 5):
        print(i)

print_multiples_5()
/python/python_fundamentals/for_loop_basic4.py
"""
Write a function that prints the odd numbers from 1 to 1000.
"""

def print_odd_numbers():
    for i in range(1, 1001, 2):
        print(i)

print_odd_numbers()
/python/python_fundamentals/for_loop_basic5.py
"""
Write a function that prints and returns the sum of all the values from 1 to 5000000.
"""

def print_sum_5000000():
    sum = 0
    for i in range(1, 5000001):
        sum += i
    print(sum)
    return sum

print_sum_5000000()
/python/python_fundamentals/for_loop_basic6.py
"""
Write a function that prints the sum of all the values from 1 to 1000.
"""

def print_sum_1000():
    sum = 0
    for i in range(1, 1001):
        sum += i
    print(sum)
    return sum

print_sum_1000()
/python/python_fundamentals/for_loop_basic7.py
"""
Write a function that prints the odd numbers from 1 to 1000000.
"""

def print_odd_numbers_1000000():
    for i in range(1, 1000001, 2):
        print(i)

print_odd_numbers_1000000()
/python/python_fundamentals/for_loop_basic8.py
"""
Write a function that prints and returns the product of all the values from 1 to 1000.
"""

def print_product_1000():
    product = 1
    for i in range(1, 1001):
        product *= i
    print(product)
    return product

print_product_1000()
/python/python_fundamentals/for_loop_basic9.py
"""
Write a function that prints the sum of all the values from 1 to 1000000.
"""

def print_sum_1000000():
    sum = 0
    for i in range(1, 1000001):
        sum += i
    print(sum)
    return sum

print_sum_1000000()
/python/python_fundamentals/for_loop_basic10.py
"""
Write a function that prints the odd numbers from 1 to 1000000.
"""

def print_odd_numbers_1000000():
    for i in range(1, 1000001, 2):
        print(i)