"""
Write a python function to find the maximum of two numbers.
assert maximum(5,10) == 10
"""

def maximum(a,b):
    if a > b:
        return a
    else:
        return b

assert maximum(5,10) == 10
assert maximum(10,5) == 10
assert maximum(10,10) == 10
assert maximum(5,5) == 5

"""
Write a python function to find the maximum of three numbers.
assert maximum(5,10,15) == 15
"""

def maximum(a,b,c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

assert maximum(5,10,15) == 15
assert maximum(10,5,15) == 15
assert maximum(10,15,5) == 15
assert maximum(5,5,15) == 15
assert maximum(5,15,5) == 15
assert maximum(15,5,5) == 15
assert maximum(5,5,5) == 5

"""
Write a python function to find the maximum of four numbers.
assert maximum(5,10,15,20) == 20
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

assert maximum(5,10,15,20) == 20
assert maximum(10,5,15,20) == 20
assert maximum(10,15,5,20) == 20
assert maximum(10,15,20,5) == 20
assert maximum(5,5,15,20) == 20
assert maximum(5,15,5,20) == 20
assert maximum(5,15,20,5) == 20
assert maximum(5,5,5,20) == 20
assert maximum(5,5,20,5) == 20
assert maximum(5,20,5,5) == 20
assert maximum(20,5,5,5) == 20
assert maximum(5,5,5,5) == 5

"""
Write a python function to find the maximum of five numbers.
assert maximum(5,10,15,20,25) == 25
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

assert maximum(5,10,15,20,25) == 25
assert maximum(10,5,15,20,25) == 25
assert maximum(10,15,5,20,25) == 25
assert maximum(10,15,20,5,25) == 25
assert maximum(10,15,20,25,5) == 25
assert maximum(5,5,15,20,25) == 25
assert maximum(5,15,5,20,25) == 25
assert maximum(5,15,20,5,25) == 25
assert maximum(5,15,20,25,5) == 25
assert maximum(5,5,5,20,25) == 25