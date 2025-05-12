"""
Write a function to sum the length of the names of a given list of names after removing the names that start with a lowercase letter.
assert sample_nam(['sally', 'Dylan','rebecca', 'Diana', 'Joanne', 'keith'])==16
"""

def sample_nam(names):
    sum = 0
    for name in names:
        if name[0].isupper():
            sum += len(name)
    return sum

print(sample_nam(['sally', 'Dylan','rebecca', 'Diana', 'Joanne', 'keith']))/python_fundamentals/fundamentals/for_loop_basic2.py
"""
Create a function that prints the numbers from 1 to 20.
"""

def print_to_20():
    for i in range(1, 21):
        print(i)

print_to_20()/python_fundamentals/fundamentals/for_loop_basic1.py
"""
Create a function that prints the numbers from 1 to 20.
"""

def print_to_20():
    for i in range(1, 21):
        print(i)

print_to_20()/python_fundamentals/fundamentals/for_loop_basic3.py
"""
Create a function that prints the odd numbers from 1 to 20.
"""

def print_odd_to_20():
    for i in range(1, 21):
        if i % 2!= 0:
            print(i)

print_odd_to_20()/python_fundamentals/fundamentals/for_loop_basic4.py
"""
Create a function that prints the multiples of 5 from 5 to 1,000,000.
"""

def print_multiples_of_5():
    for i in range(5, 1000001, 5):
        print(i)

print_multiples_of_5()/python_fundamentals/fundamentals/for_loop_basic5.py
"""
Create a function that prints the odd numbers from 1 to 1000.
"""

def print_odd_to_1000():
    for i in range(1, 1001):
        if i % 2!= 0:
            print(i)

print_odd_to_1000()/python_fundamentals/fundamentals/for_loop_basic6.py
"""
Create a function that prints the multiples of 6 from 6 to 1,000,000.
"""

def print_multiples_of_6():
    for i in range(6, 1000001, 6):
        print(i)

print_multiples_of_6()/python_fundamentals/fundamentals/for_loop_basic7.py
"""
Create a function that prints the odd numbers from 1 to 1000.
"""

def print_odd_to_1000():
    for i in range(1, 1001):
        if i % 2!= 0:
            print(i)

print_odd_to_1000()/python_fundamentals/fundamentals/for_loop_basic8.py
"""
Create a function that prints the multiples of 7 from 7 to 1,000,000.
"""

def print_multiples_of_7():
    for i in range(7, 1000001, 7):
        print(i)

print_multiples_of_7()/python_fundamentals/fundamentals/for_loop_basic9.py
"""
Create a function that prints the multiples of 12 from 12 to 1,000,000.
"""

def print_multiples_of_12():
    for i in range(12, 1000001, 12):
        print(i)

print_multiples_of_12()/python_fundamentals/fundamentals/for_loop_basic10.py
"""
Create a function that prints the multiples of 19 from 19 to 1,000,000.
"""

def print_multiples_of_