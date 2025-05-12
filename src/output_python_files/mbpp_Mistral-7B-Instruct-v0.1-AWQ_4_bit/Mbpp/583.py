"""
Write a function which returns nth catalan number.
assert catalan_number(10)==16796
"""

def catalan_number(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return sum([catalan_number(i) * catalan_number(n - i - 1) for i in range(1, n)])

assert catalan_number(10) == 16796