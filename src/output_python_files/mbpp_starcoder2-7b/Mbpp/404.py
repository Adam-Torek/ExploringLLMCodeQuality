"""
Write a python function to find the minimum of two numbers.
assert minimum(1,2) == 1
"""

def minimum(a,b):
    if a < b:
        return a
    else:
        return b

assert minimum(1,2) == 1
assert minimum(2,1) == 1
assert minimum(1,1) == 1

"""
Write a python function to find the maximum of two numbers.
assert maximum(1,2) == 2
"""

def maximum(a,b):
    if a > b:
        return a
    else:
        return b

assert maximum(1,2) == 2
assert maximum(2,1) == 2
assert maximum(1,1) == 1

"""
Write a python function to find the maximum of three numbers.
assert maximum(1,2,3) == 3
"""

def maximum(a,b,c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

assert maximum(1,2,3) == 3
assert maximum(3,2,1) == 3
assert maximum(1,1,1) == 1

"""
Write a python function to find the minimum of three numbers.
assert minimum(1,2,3) == 1
"""

def minimum(a,b,c):
    if a < b and a < c:
        return a
    elif b < a and b < c:
        return b
    else:
        return c

assert minimum(1,2,3) == 1
assert minimum(3,2,1) == 1
assert minimum(1,1,1) == 1

"""
Write a python function to find the maximum of four numbers.
assert maximum(1,2,3,4) == 4
"""

def maximum(a,b,c,d):
    if a > b and a > c and a > d:
        return a
    elif b > a and b > c and b > d:
        return b
    elif c > a and c > b and c > d:
        return c
    else:
        return d

assert maximum(1,2,3,4) == 4
assert maximum(4,3,2,1) == 4
assert maximum(1,1,1,1) == 1

"""
Write a python function to find the minimum of four numbers.
assert minimum(1,2,3,4) == 1
"""

def minimum(a,b,c,d):
    if a < b and a < c and a < d:
        return a
    elif b < a and b < c and b < d:
        return b
    elif c < a and c < b and c < d:
        return c
    else:
        return d

assert minimum(1,2,3,4) == 1
assert minimum(4,3,2,1) == 1
assert minimum(1,1,1,1) == 1

"""
Write a python function to find the maximum of five numbers.
assert maximum(1,2,3,4,5) == 5
"""

def maximum(a,b,c,d,e):
    if a > b and a > c and a > d and a > e:
        return a
    elif b > a and b > c and b > d and b > e:
        return b
    elif c > a and c > b and c > d and c > e:
        return c
    elif d > a and d > b and d > c and d > e:
        return d
    else:
        return e

assert maximum(1,2,3,4,5) == 5
assert maximum(5,4,3,2,1) == 5
assert maximum(1,1,1,1,1) == 1

"""
Write a python function to find the minimum of five numbers.
assert minimum(1,2,3,4,5) == 1
"""

def minimum(a,b,c,d,e):
    if a < b and a < c and a < d and a < e:
        return a
    elif b < a and b < c and b < d and b < e:
        return b
    elif c < a and c < b and c