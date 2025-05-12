"""
Write a function to return the sum of all divisors of a number.
assert sum_div(8)==7
"""

def sum_div(n):
    sum = 0
    for i in range(1,n):
        if n%i == 0:
            sum += i
    return sum

print(sum_div(8))
/python/python_fundamentals/for_loop_basic2.py
"""
Write a function that counts from 1 to 2000.
"""

def count():
    for i in range(1,2001):
        print(i)

count()
/python/python_fundamentals/for_loop_basic1.py
"""
Write a function that prints all the integers from 0 to 150.
"""

def count():
    for i in range(0,151):
        print(i)

count()
/python/python_fundamentals/for_loop_basic3.py
"""
Write a function that prints all the multiples of 5 from 5 to 1,000,000.
"""

def count():
    for i in range(5,1000001,5):
        print(i)

count()
/python/python_fundamentals/for_loop_basic4.py
"""
Write a function that prints the odd numbers from 1 to 1000.
"""

def count():
    for i in range(1,1001):
        if i%2!= 0:
            print(i)

count()
/python/python_fundamentals/for_loop_basic5.py
"""
Write a function that prints and returns the sum of all the values from 1 to 5000000.
"""

def count():
    sum = 0
    for i in range(1,5000001):
        sum += i
    print(sum)
    return sum

count()
/python/python_fundamentals/for_loop_basic6.py
"""
Write a function that prints the sum of all the values from -1000000 to 1000000.
"""

def count():
    sum = 0
    for i in range(-1000000,1000001):
        sum += i
    print(sum)
    return sum

count()
/python/python_fundamentals/for_loop_basic7.py
"""
Write a function that prints the sum of all the values from -1000000 to 1000000.
"""

def count():
    sum = 0
    for i in range(-1000000,1000001):
        if i%2!= 0:
            sum += i
    print(sum)
    return sum

count()
/python/python_fundamentals/for_loop_basic8.py
"""
Write a function that prints the sum of all the values from -1000000 to 1000000.
"""

def count():
    sum = 0
    for i in range(-1000000,1000001):
        if i%2 == 0:
            sum += i
    print(sum)
    return sum

count()
/python/python_fundamentals/for_loop_basic9.py
"""
Write a function that prints the sum of all the values from -1000000 to 1000000.
"""

def count():
    sum = 0
    for i in range(-1000000,1000001):
        if i%2 == 0:
            sum += i
        elif i%2!= 0:
            sum -= i
    print(sum)
    return sum

count()
/python/python_fundamentals/for_loop_basic10.py