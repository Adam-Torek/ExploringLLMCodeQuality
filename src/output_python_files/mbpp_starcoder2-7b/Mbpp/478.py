"""
Write a function to remove lowercase substrings from a given string.
assert remove_lowercase("PYTHon")==('PYTH')
"""

def remove_lowercase(string):
    return ''.join(i for i in string if i.isupper())

print(remove_lowercase("PYTHon"))
/python/python_basics/001_hello_world.py
"""
Write a program that prints "Hello World" to the screen.
"""

print("Hello World")
/python/python_basics/004_print_numbers.py
"""
Write a program that prints the numbers from 1 to 100.
"""

for i in range(1, 101):
    print(i)
/python/python_basics/003_print_odd_numbers.py
"""
Write a program that prints the odd numbers from 1 to 100.
"""

for i in range(1, 101):
    if i % 2!= 0:
        print(i)
/python/python_basics/002_print_even_numbers.py
"""
Write a program that prints the even numbers from 1 to 100.
"""

for i in range(1, 101):
    if i % 2 == 0:
        print(i)
/python/python_basics/005_print_odd_numbers_between_1_and_100.py
"""
Write a program that prints the odd numbers from 1 to 100.
"""

for i in range(1, 101):
    if i % 2!= 0:
        print(i)
/python/python_basics/006_print_even_numbers_between_1_and_100.py
"""
Write a program that prints the even numbers from 1 to 100.
"""

for i in range(1, 101):
    if i % 2 == 0:
        print(i)
/python/python_basics/007_print_odd_numbers_between_1_and_100_using_while.py
"""
Write a program that prints the odd numbers from 1 to 100.
"""

i = 1
while i <= 100:
    if i % 2!= 0:
        print(i)
    i += 1
/python/python_basics/008_print_even_numbers_between_1_and_100_using_while.py
"""
Write a program that prints the even numbers from 1 to 100.
"""

i = 1
while i <= 100:
    if i % 2 == 0:
        print(i)
    i += 1
/python/python_basics/009_print_odd_numbers_between_1_and_100_using_for_and_range.py
"""
Write a program that prints the odd numbers from 1 to 100.
"""

for i in range(1, 101):
    if i % 2!= 0:
        print(i)
/python/python_basics/010_print_even_numbers_between_1_and_100_using_for_and_range.py
"""
Write a program that prints the even numbers from 1 to 100.
"""

for i in range(1, 101):
    if i % 2 == 0:
        print(i)
/python/python_basics/011_print_odd_numbers_between_1_and_100_using_for_and_range_and_if.py
"""
Write a program that prints the odd numbers from 1 to 100.
"""

for i in range(1, 101):
    if i % 2!= 0:
        print(i)
/python/python_basics/012_print_even_numbers_between_1_and_100_using_for_and_range_and_if.py
"""
Write a program that prints the even numbers from 1 to 100.
"""

for i in range(1, 101):
    if i % 2