"""
Write a python function to check whether every odd index contains odd numbers of a given list.
assert odd_position([2,1,4,3,6,7,6,3]) == True
"""

def odd_position(lst):
    for i in range(1, len(lst), 2):
        if lst[i] % 2 == 0:
            return False
    return True

print(odd_position([2,1,4,3,6,7,6,3]))
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
Write a program that prints all the integers from 0 to 1000.
Have the program count by fours.
(Ex. 0, 4, 8, 12, 16,... 996, 1000)
"""

for i in range(0, 1001, 4):
    print(i)
/python/python_fundamentals/for_loop_basic3.py
"""
Write a program that prints the multiples of 5 from 5 to 1,000,000.
Have the program count down by fives.
(Ex. 1000000, 999995, 999990, 999985,...)
"""

for i in range(1000000, 0, -5):
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
Write a program that prints all the multiples of 6 up to 60,000,000.
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
    if i % 2 == 0:
        continue
    print(i)
/python/python_fundamentals/for_loop_basic8.py
"""
Write a program that prints the odd numbers from 1 to 1000.
Use a FOR loop and not a WHILE loop.
"""

for i in range(1, 1001):
    if i % 2 == 0:
        continue
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

for i in range(1, 1001):
    if i % 2 == 0:
        continue