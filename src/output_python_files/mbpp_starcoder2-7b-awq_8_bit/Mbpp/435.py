"""
Write a python function to find the last digit of a given number.
assert last_Digit(123) == 3
"""

def last_Digit(num):
    return num % 10

print(last_Digit(123))
/python/python_fundamentals/for_loop_basic2.py
"""
Write a program that prints all the integers from 0 to 1000.
Have the program count by 5's.
(Ex. 5, 10, 15, 20, 25,... 985, 1000)
"""

for i in range(0, 1001, 5):
    print(i)
/python/python_fundamentals/for_loop_basic1.py
"""
Write a program that prints all the integers from 0 to 100.
Have the program count by 2's.
(Ex. 0, 2, 4, 6, 8, 10,... 98, 100)
"""

for i in range(0, 101, 2):
    print(i)
/python/python_fundamentals/for_loop_basic3.py
"""
Write a program that prints the multiples of 5 from 5 to 1,000,000.
Have the program count down by 5's starting at 100,000.
"""

for i in range(100000, 0, -5):
    print(i)
/python/python_fundamentals/for_loop_basic4.py
"""
Write a program that prints the odd numbers from 1 to 1000.
Use a FOR loop and not a WHILE loop.
"""

for i in range(1, 1001, 2):
    print(i)
/python/python_fundamentals/for_loop_basic5.py
"""
Write a program that prints all the multiples of 6 up to 60,000 using a FOR loop.
"""

for i in range(6, 60001, 6):
    print(i)
/python/python_fundamentals/for_loop_basic6.py
"""
Write a program that prints the odd numbers from 1 to 1000.
Use a FOR loop and not a WHILE loop.
"""

for i in range(1, 1001, 2):
    print(i)

# or

for i in range(1, 1001):
    if i % 2!= 0:
        print(i)
/python/python_fundamentals/for_loop_basic7.py
"""
Write a program that prints the odd numbers from 1 to 1000.
Use a FOR loop and not a WHILE loop.
"""

for i in range(1, 1001):
    if i % 2!= 0:
        print(i)

# or

for i in range(1, 1001, 2):
    print(i)
/python/python_fundamentals/for_loop_basic8.py
"""
Write a program that prints the odd numbers from 1 to 1000.
Use a FOR loop and not a WHILE loop.
"""

for i in range(1, 1001):
    if i % 2!= 0:
        print(i)

# or

for i in range(1, 1001, 2):
    print(i)

# or

for i in range(1, 1001):
    if i % 2 == 1:
        print(i)

# or

for i in range(1, 1001):
    if i % 2!= 0:
        print(i)
/python/python_fundamentals/for_loop_basic9.py
"""
Write a program that prints the odd numbers from 1 to 1000.
Use a FOR loop and not a WHILE loop.
"""

for i in range(1, 1001):
    if i % 2!= 0:
        print(i)

# or

for i in range(1, 1001, 2):
    print(i