"""
Write a function to create a new tuple from the given string and list.
assert new_tuple(["WEB", "is"], "best") == ('WEB', 'is', 'best')
"""

def new_tuple(list, string):
    return tuple(list + [string])

print(new_tuple(["WEB", "is"], "best"))
<file_sep>/python/python_basics/001_hello_world.py
"""
Write a program that prints "Hello World" to the screen.
"""

print("Hello World")
<file_sep>/python/python_basics/004_print_numbers.py
"""
Write a program that prints the numbers 1 to 10 to the screen.
"""

for i in range(1, 11):
    print(i)
<file_sep>/python/python_basics/005_print_odd_numbers.py
"""
Write a program that prints the odd numbers from 1 to 10 to the screen.
"""

for i in range(1, 11):
    if i % 2 == 1:
        print(i)
<file_sep>/python/python_basics/003_print_numbers_with_for.py
"""
Write a program that prints the numbers 1 to 10 to the screen.
"""

for i in range(1, 11):
    print(i)
<file_sep>/python/python_basics/002_print_numbers_with_while.py
"""
Write a program that prints the numbers 1 to 10 to the screen.
"""

i = 1
while i <= 10:
    print(i)
    i += 1
<file_sep>/python/python_basics/006_print_even_numbers.py
"""
Write a program that prints the even numbers from 1 to 10 to the screen.
"""

for i in range(1, 11):
    if i % 2 == 0:
        print(i)
<file_sep>/python/python_basics/007_print_numbers_with_while_and_break.py
"""
Write a program that prints the numbers 1 to 10 to the screen.
"""

i = 1
while True:
    print(i)
    i += 1
    if i > 10:
        break
<file_sep>/python/python_basics/008_print_numbers_with_while_and_continue.py
"""
Write a program that prints the numbers 1 to 10 to the screen.
"""

i = 1
while True:
    i += 1
    if i > 10:
        break
    if i % 2 == 1:
        continue
    print(i)
<file_sep>/python/python_basics/009_print_numbers_with_for_and_break.py
"""
Write a program that prints the numbers 1 to 10 to the screen.
"""

for i in range(1, 11):
    if i > 10:
        break
    print(i)
<file_sep>/python/python_basics/010_print_numbers_with_for_and_continue.py
"""
Write a program that prints the numbers 1 to 10 to the screen.
"""

for i in range(1, 11):
    if i % 2 == 1:
        continue
    print(i)
<|endoftext|>