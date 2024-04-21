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
assert minimum(0,1) == 0
assert minimum(1,0) == 0
assert minimum(0,0) == 0

print("All tests passed")
<file_sep>/python/001-hello-world/hello-world.py
"""
Write a python function to print "Hello World"
"""

def hello_world():
    print("Hello World")

hello_world()
<file_sep>/python/003-minimum-of-three/minimum-of-three.py
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
assert minimum(2,1,3) == 1
assert minimum(3,2,1) == 1
assert minimum(1,1,1) == 1
assert minimum(0,1,2) == 0
assert minimum(1,0,2) == 0
assert minimum(1,2,0) == 0
assert minimum(0,0,0) == 0

print("All tests passed")
<file_sep>/python/002-minimum-of-two/minimum-of-two.py
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
assert minimum(0,1) == 0
assert minimum(1,0) == 0
assert minimum(0,0) == 0

print("All tests passed")
<file_sep>/python/004-sum-of-n-numbers/sum-of-n-numbers.py
"""
Write a python function to find the sum of n numbers.
assert sum_of_n(1,2,3) == 6
"""

def sum_of_n(a,b,c):
    return a+b+c

assert sum_of_n(1,2,3) == 6
assert sum_of_n(2,1,3) == 6
assert sum_of_n(3,2,1) == 6
assert sum_of_n(1,1,1) == 3
assert sum_of_n(0,1,2) == 3
assert sum_of_n(1,0,2) == 3
assert sum_of_n(1,2,0) == 3
assert sum_of_n(0,0,0) == 0

print("All tests passed")
<file_sep>/python/005-sum-of-n-numbers-2/sum-of-n-numbers-2.py
"""
Write a python function to find the sum of n numbers.
assert sum_of_n(1,2,3) == 6
"""

def sum_of_n(a,b,c):
    return a+b+c

assert sum_of_n(1,2,3) == 6
assert sum_of_n(2,1,3) == 6
assert sum_of_n(3,2,1) == 6
assert sum_of_n(1,1,1) == 3
assert sum_of_n(0,1,2) == 3
assert sum_of_n(1,0,2) == 3
assert sum_of_n(1,2,0) == 3
assert sum_of_n(0,0,0) == 0

print("All tests passed")
<file_sep>/python/006-sum-of-n-numbers-3/sum-of-n-numbers-3.py