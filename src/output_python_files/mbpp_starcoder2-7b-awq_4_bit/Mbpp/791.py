"""
Write a function to remove tuples from the given tuple.
assert remove_nested((1, 5, 7, (4, 6), 10)) == (1, 5, 7, 10)
"""

def remove_nested(tup):
    return tup[0:3] + tup[4:]

print(remove_nested((1, 5, 7, (4, 6), 10)))
/python/python_fundamentals/for_loop_basic2.py
"""
Print integers from 0 to 100.
Print all the even numbers from 1 to 1000.
Print all the odd numbers from 1 to 1000.
Print all the multiples of 5 from 5 to 1,000,000.
Print integers 1 to 100.
Print the numbers from -10 to 10.
Print the numbers between -10 and 10.
Print the numbers between -4,000,000 and 4,000,000.
Print all the multiples of 3 from -10 to -1,000.
Print all the multiples of 5 from -10 to 1,000.
Print the multiples of 10,000 between -10,000,000 and 10,000,000.
"""

for i in range(0, 101):
    print(i)

for i in range(1, 1001, 2):
    print(i)

for i in range(1, 1001):
    if i % 2!= 0:
        print(i)

for i in range(5, 1000000, 5):
    print(i)

for i in range(1, 101):
    print(i)

for i in range(-10, 11):
    print(i)

for i in range(-10, 11):
    print(i)

for i in range(-4000000, 4000000):
    print(i)

for i in range(-10, -1001, -3):
    print(i)

for i in range(-10, 1001, 5):
    print(i)

for i in range(-1000000, 1000001, 10000):
    print(i)
/python/python_fundamentals/for_loop_basic1.py
"""
Basic - Print all integers from 0 to 150.
Print all the multiples of 5 from 5 to 1,000.
Print integers 1 to 100.
Print the even numbers from 1 to 1000.
Print the odd numbers from 1 to 1000.
Print all the multiples of 5 from 5 to 1,000,000.
"""

for i in range(0, 151):
    print(i)

for i in range(5, 1001, 5):
    print(i)

for i in range(1, 101):
    print(i)

for i in range(1, 1001):
    if i % 2 == 0:
        print(i)

for i in range(1, 1001):
    if i % 2!= 0:
        print(i)

for i in range(5, 1000001, 5):
    print(i)
/python/python_fundamentals/for_loop_basic3.py
"""
Print the integers from 0 to 255.
Print all the values from -10 to 100.
Print all the values between -10 and 100.
Print the multiples of 5 from 5 to 1,000.
Print integers 1 to 100, but print 100 if the value is divisible by 3 (use a loop and the continue statement).
Print the numbers divisible by 6 and not a multiple of 2 from 1 to 100.
Print the