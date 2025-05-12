"""
Write a function to find the number of ways to partition a set of Bell numbers.
assert bell_number(2)==2
"""

def bell_number(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return bell_number(n-1) + sum([bell_number(i) * bell_number(n-i-1) for i in range(n)])

def bell_number_2(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return bell_number_2(n-1) + sum([bell_number_2(i) * bell_number_2(n-i-1) for i in range(n)])

def bell_number_3(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return bell_number_3(n-1) + sum([bell_number_3(i) * bell_number_3(n-i-1) for i in range(n)])

def bell_number_4(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return bell_number_4(n-1) + sum([bell_number_4(i) * bell_number_4(n-i-1) for i in range(n)])

def bell_number_5(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return bell_number_5(n-1) + sum([bell_number_5(i) * bell_number_5(n-i-1) for i in range(n)])

def bell_number_6(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return bell_number_6(n-1) + sum([bell_number_6(i) * bell_number_6(n-i-1) for i in range(n)])

def bell_number_7(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return bell_number_7(n-1) + sum([bell_number_7(i) * bell_number_7(n-i-1) for i in range(n)])

def bell_number_8(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return bell_number_8(n-1) + sum([bell_number_8(i) * bell_number_8(n-i-1) for i in range(n)])

def bell_number_9(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return bell_number_9(n-1) + sum([bell_number_9(i) * bell_number_9(n-i-1) for i in range(n)])

def bell_number_10(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return bell_number_10(n-1) + sum([bell_number_10(i) * bell_number_10(n-i-1) for i in range(n)])

def bell_number_11(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return bell_number_11(n-1) + sum([bell_number_11(i) * bell_number_11(n-i-1) for i in range(n)])

def bell_number_12(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return bell_number_12(n-1) + sum([bell_number_12(i) * bell_number_12(n-i-1) for i in range(n)])

def b