"""
Write a function to drop empty items from a given dictionary.
assert drop_empty({'c1': 'Red', 'c2': 'Green', 'c3':None})=={'c1': 'Red', 'c2': 'Green'}
"""

def drop_empty(d):
    return {k:v for k,v in d.items() if v}

print(drop_empty({'c1': 'Red', 'c2': 'Green', 'c3':None}))
/python/python_basics/001_hello_world.py
"""
Write a program that prints "Hello World" to the screen.
"""

print("Hello World")
/python/python_basics/003_print_numbers.py
"""
Write a program that prints the numbers from 1 to 100.
"""

for i in range(1,101):
    print(i)
/python/python_basics/002_print_odd_numbers.py
"""
Write a program that prints the odd numbers from 1 to 100.
"""

for i in range(1,101):
    if i%2!= 0:
        print(i)
/python/python_basics/004_print_even_numbers.py
"""
Write a program that prints the even numbers from 1 to 100.
"""

for i in range(1,101):
    if i%2 == 0:
        print(i)
/python/python_basics/005_print_odd_numbers_between_50_and_100.py
"""
Write a program that prints the odd numbers from 50 to 100.
"""

for i in range(50,101):
    if i%2!= 0:
        print(i)
/python/python_basics/006_print_even_numbers_between_50_and_100.py
"""
Write a program that prints the even numbers from 50 to 100.
"""

for i in range(50,101):
    if i%2 == 0:
        print(i)
/python/python_basics/007_print_numbers_divisible_by_7_and_5_between_500_and_1000.py
"""
Write a program that prints the numbers from 500 to 1000 that are divisible by 7 and 5.
"""

for i in range(500,1001):
    if i%7 == 0 and i%5 == 0:
        print(i)
/python/python_basics/008_print_numbers_divisible_by_7_or_5_between_500_and_1000.py
"""
Write a program that prints the numbers from 500 to 1000 that are divisible by 7 or 5.
"""

for i in range(500,1001):
    if i%7 == 0 or i%5 == 0:
        print(i)
/python/python_basics/009_print_numbers_divisible_by_7_and_5_between_500_and_1000_but_not_both.py
"""
Write a program that prints the numbers from 500 to 1000 that are divisible by 7 and 5 but not both.
"""

for i in range(500,1001):
    if i%7 == 0 and i%5!= 0:
        print(i)
/python/python_basics/010_print_numbers_divisible_by_7_or_5_but_not_both_between_500_and_1000.py
"""
Write a program that prints the numbers from 500 to 1000 that are divisible by 7 or 5 but not both.