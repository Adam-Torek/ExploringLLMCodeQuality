"""
Write a python function that takes in an integer n and returns the sum of the squares of the first n odd natural numbers.
assert square_Sum(2) == 10
"""

def square_Sum(n):
    sum = 0
    for i in range(1, n+1):
        sum += i**2
    return sum

print(square_Sum(2))
/python/python_fundamentals/for_loop_basic2.py
"""
Write a program that prints all the integers from 0 to 1000.
Have the program count by 5's.
(Ex. 0, 5, 10,...)
"""

for i in range(0, 1001, 5):
    print(i)
/python/python_fundamentals/for_loop_basic1.py
"""
Write a program that prints all the integers from 0 to 1000.
Have the program count by 2's.
(Ex. 0, 2, 4, 6,...)
"""

for i in range(0, 1001, 2):
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
Write a program that prints all the multiples of 6 up to 60,000,000 (60 billion).
(Ex. 6, 12, 18, 24,...)
"""

for i in range(6, 60000001, 6):
    print(i)
/python/python_fundamentals/for_loop_basic6.py
"""
Write a program that prints the odd numbers from 1 to 1000.
Use a FOR loop and not a WHILE loop.
"""

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

for i in range(1, 1001, 2):
    print(i)

# or

for i in range(1, 1001):
    if i % 2!= 0:
        print(i)

# or

for i in range(1, 1001):
    if i % 2!= 0:
        print(i)

# or

for i in range(1, 1001):
    if i % 2!= 0:
        print(i)

# or

for i in range(1, 1001):
    if i % 2!= 0:
        print(i)

# or