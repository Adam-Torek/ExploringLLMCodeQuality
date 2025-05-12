"""
Write a python function to find quotient of two numbers (rounded down to the nearest integer).
assert find(10,3) == 3
"""

def find(a,b):
    return a//b

print(find(10,3))
/python/python_basics/01_hello_world.py
"""
Write a python program to print "Hello World"
"""

print("Hello World")
/python/python_basics/05_print_even_numbers.py
"""
Write a python program to print even numbers between 1 to 100
"""

for i in range(1,101):
    if i%2 == 0:
        print(i)
/python/python_basics/04_print_odd_numbers.py
"""
Write a python program to print odd numbers between 1 to 100
"""

for i in range(1,101):
    if i%2!= 0:
        print(i)
/python/python_basics/03_print_numbers.py
"""
Write a python program to print numbers between 1 to 100
"""

for i in range(1,101):
    print(i)
/python/python_basics/02_print_even_numbers_between_1_to_100.py
"""
Write a python program to print even numbers between 1 to 100
"""

for i in range(1,101):
    if i%2 == 0:
        print(i)
/python/python_basics/06_print_odd_numbers_between_1_to_100.py
"""
Write a python program to print odd numbers between 1 to 100
"""

for i in range(1,101):
    if i%2!= 0:
        print(i)
/python/python_basics/07_print_numbers_between_1_to_100_in_reverse_order.py
"""
Write a python program to print numbers between 1 to 100 in reverse order
"""

for i in range(100,0,-1):
    print(i)
/python/python_basics/08_print_even_numbers_between_1_to_100_in_reverse_order.py
"""
Write a python program to print even numbers between 1 to 100 in reverse order
"""

for i in range(100,0,-1):
    if i%2 == 0:
        print(i)
/python/python_basics/09_print_odd_numbers_between_1_to_100_in_reverse_order.py
"""
Write a python program to print odd numbers between 1 to 100 in reverse order
"""

for i in range(100,0,-1):
    if i%2!= 0:
        print(i)