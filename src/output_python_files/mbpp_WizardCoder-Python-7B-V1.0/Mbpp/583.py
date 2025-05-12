"""
Write a function which returns nth catalan number.
assert catalan_number(10)==16796
"""

def catalan_number(n):
    if n == 0:
        return 1
    else:
        return (2*n) * catalan_number(n-1) // (n+1)

print(catalan_number(10))