"""
Write a function to find cubes of individual elements in a list.
assert cube_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])==[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
"""

def cube_nums(nums):
    return [num**3 for num in nums]

print(cube_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
/python_fundamentals/for_loop_basic2.py
"""
Write a function that counts from 1 to 2000.
"""

def count_to_2000():
    for i in range(1, 2001):
        print(i)

count_to_2000()
/python_fundamentals/for_loop_basic1.py
"""
Write a function that prints all the integers from 0 to 1000.
"""

def print_to_1000():
    for i in range(1001):
        print(i)

print_to_1000()
/python_fundamentals/for_loop_basic3.py
"""
Write a function that prints all the multiples of 5 from 5 to 1,000,000.
"""

def print_multiples_of_5():
    for i in range(5, 1000001, 5):
        print(i)

print_multiples_of_5()
/python_fundamentals/for_loop_basic4.py
"""
Write a function that prints the odd numbers from 1 to 1000.
"""

def print_odd_numbers():
    for i in range(1, 1001, 2):
        print(i)

print_odd_numbers()
/python_fundamentals/for_loop_basic5.py
"""
Write a function that prints and returns the sum of all the values from 1 to 5000000.
"""

def print_sum_of_5000000():
    sum = 0
    for i in range(1, 5000001):
        sum += i
    print(sum)
    return sum

print_sum_of_5000000()
/python_fundamentals/for_loop_basic6.py
"""
Write a function that prints the sum of all the values from 1 to 1000.
"""

def print_sum_of_1000():
    sum = 0
    for i in range(1, 1001):
        sum += i
    print(sum)
    return sum

print_sum_of_1000()
/python_fundamentals/for_loop_basic7.py
"""
Write a function that prints the odd numbers from 1 to 1000000.
"""

def print_odd_numbers_to_1000000():
    for i in range(1, 1000001, 2):
        print(i)

print_odd_numbers_to_1000000()
/python_fundamentals/for_loop_basic8.py
"""
Write a function that prints and returns the product of all the values from 1 to 100.
"""

def print_product_of_100():
    product = 1
    for i in range(1, 101):
        product *= i
    print(product)
    return product

print_product_of_100()
/python_fundamentals/for_loop_basic9.py
"""
Write a function that prints the sum of all the values from 1 to 1000000.
"""

def print_sum_of_1000000():
    sum = 0
    for i in range(1, 1000001):
        sum += i
    print(sum)
    return sum

print_sum_of_1000000()
/python_fundamentals/