"""
Write a python function to check if a given number is one less than twice its reverse.
assert check(70) == False
"""

def check(n):
    return n == int(str(n)[::-1]) - 1

assert check(70) == False
assert check(101) == True
assert check(1001) == True
assert check(10001) == False
assert check(100001) == False
assert check(1000001) == False
assert check(10000001) == False
assert check(100000001) == False
assert check(1000000001) == False
assert check(10000000001) == False
assert check(100000000001) == False
assert check(1000000000001) == False
assert check(10000000000001) == False
assert check(100000000000001) == False
assert check(1000000000000001) == False
assert check(10000000000000001) == False
assert check(100000000000000001) == False
assert check(1000000000000000001) == False
assert check(10000000000000000001) == False
assert check(100000000000000000001) == False
assert check(1000000000000000000001) == False
assert check(10000000000000000000001) == False
assert check(100000000000000000000001) == False
assert check(1000000000000000000000001) == False
assert check(10000000000000000000000001) == False
assert check(100000000000000000000000001) == False
assert check(1000000000000000000000000001) == False
assert check(10000000000000000000000000001) == False
assert check(100000000000000000000000000001) == False
assert check(1000000000000000000000000000001) == False
assert check(10000000000000000000000000000001) == False
assert check(100000000000000000000000000000001) == False
assert check(1000000000000000000000000000000001) == False
assert check(10000000000000000000000000000000001) == False
assert check(100000000000000000000000000000000001) == False
assert check(1000000000000000000000000000000000001) == False
assert check(10000000000