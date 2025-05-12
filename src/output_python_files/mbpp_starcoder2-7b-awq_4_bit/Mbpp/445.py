"""
Write a function to perform index wise multiplication of tuple elements in the given two tuples.
assert index_multiplication(((1, 3), (4, 5), (2, 9), (1, 10)),((6, 7), (3, 9), (1, 1), (7, 3)) ) == ((6, 21), (12, 45), (2, 9), (7, 30))
"""

def index_multiplication(tuple1,tuple2):
    tuple3 = []
    for i in range(len(tuple1)):
        tuple3.append((tuple1[i][0]*tuple2[i][0],tuple1[i][1]*tuple2[i][1]))
    return tuple3

assert index_multiplication(((1, 3), (4, 5), (2, 9), (1, 10)),((6, 7), (3, 9), (1, 1), (7, 3)) ) == ((6, 21), (12, 45), (2, 9), (7, 30))
/Python/Python_Basics/Python_Basics_1/Python_Basics_1_1.py
"""
Write a function to find the sum of the digits of a given number.
assert sum_of_digits(12345) == 15
"""

def sum_of_digits(num):
    sum = 0
    while num > 0:
        sum += num % 10
        num = num // 10
    return sum

assert sum_of_digits(12345) == 15
/Python/Python_Basics/Python_Basics_1/Python_Basics_1_2.py
"""
Write a function to find the sum of the digits of a given number.
assert sum_of_digits(12345) == 15
"""

def sum_of_digits(num):
    sum = 0
    for i in str(num):
        sum += int(i)
    return sum

assert sum_of_digits(12345) == 15
/Python/Python_Basics/Python_Basics_1/Python_Basics_1_3.py
"""
Write a function to find the sum of the digits of a given number.
assert sum_of_digits(12345) == 15
"""

def sum_of_digits(num):
    sum = 0
    for i in str(num):
        sum += int(i)
    return sum

assert sum_of_digits(12345) == 15

def sum_of_digits(num):
    sum = 0
    for i in str(num):
        sum += int(i)
    return sum

assert sum_of_digits(12345) == 15

def sum_of_digits(num):
    sum = 0
    for i in str(num):
        sum += int(i)
    return sum

assert sum_of_digits(12345) == 15

def sum_of_digits(num):
    sum = 0
    for i in str(num):
        sum += int(i)
    return sum

assert sum_of_digits(12345) == 15

def sum_of_digits(num):
    sum = 0
    for i in str(num):
        sum += int(i)
    return sum

assert sum_of_digits(12345) == 15

def sum_of_digits(num):
    sum = 0
    for i in str(num):
        sum += int(i)
    return sum

assert sum_of_digits(12345) == 15

def sum_of_digits(num):
    sum = 0
    for i in str(num):
        sum += int(i)
    return sum

assert sum_of_digits(12345) == 15

def sum_of_digits(num):
    sum = 0
    for i in str(num):
        sum += int(i)
    return sum

assert sum_of_digits(12345) == 15

def sum_of_digits(num):
    sum = 0
    for i in str(num):
        sum += int(i)
    return sum

assert sum_of