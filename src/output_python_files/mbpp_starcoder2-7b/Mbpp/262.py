"""
Write a function that takes in a list and an integer L and splits the given list into two parts where the length of the first part of the list is L, and returns the resulting lists in a tuple.
assert split_two_parts([1,1,2,3,4,4,5,1],3)==([1, 1, 2], [3, 4, 4, 5, 1])
"""

def split_two_parts(lst, L):
    return lst[:L], lst[L:]

print(split_two_parts([1,1,2,3,4,4,5,1],3))
/python/python_basics/001_hello_world.py
"""
Write a program that prints "Hello World" to the screen.
"""

print("Hello World")
/python/python_basics/004_print_numbers.py
"""
Write a program that prints the numbers 1 to 100 to the screen.
"""

for i in range(1, 101):
    print(i)
/python/python_basics/003_print_odd_numbers.py
"""
Write a program that prints the odd numbers from 1 to 100 to the screen.
"""

for i in range(1, 101):
    if i % 2!= 0:
        print(i)
/python/python_basics/002_print_even_numbers.py
"""
Write a program that prints the even numbers from 1 to 100 to the screen.
"""

for i in range(1, 101):
    if i % 2 == 0:
        print(i)
/python/python_basics/005_print_odd_numbers_between_0_and_100.py
"""
Write a program that prints the odd numbers from 1 to 100 to the screen.
"""

for i in range(1, 101):
    if i % 2!= 0:
        print(i)
/python/python_basics/006_print_even_numbers_between_0_and_100.py
"""
Write a program that prints the even numbers from 1 to 100 to the screen.
"""

for i in range(1, 101):
    if i % 2 == 0:
        print(i)
/python/python_basics/007_print_numbers_divisible_by_7_between_0_and_100.py
"""
Write a program that prints the numbers from 0 to 100 that are divisible by 7.
"""

for i in range(1, 101):
    if i % 7 == 0:
        print(i)
/python/python_basics/008_print_numbers_divisible_by_7_and_5_between_0_and_100.py
"""
Write a program that prints the numbers from 0 to 100 that are divisible by 7 and 5.
"""

for i in range(1, 101):
    if i % 7 == 0 and i % 5 == 0:
        print(i)
/python/python_basics/009_print_numbers_divisible_by_7_or_5_between_0_and_100.py
"""
Write a program that prints the numbers from 0 to 100 that are divisible by 7 or 5.
"""

for i in range(1, 101):
    if i % 7 == 0 or i % 5 == 0:
        print(i)
/python/python_basics/010_print_numbers_divisible_by_7_or_5_and_not_divisible_by_3_between_0_and_100.py
"""
Write a program that prints the numbers from 0 to 100 that are divisible by 7 or 5 but not 3.
"""

for i in range(1, 101):
    if i % 7 == 0 or i % 5 == 0:
        if i % 3!=