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
        return catalan_number(n-1) + catalan_number(n-2)

print(catalan_number(10))<|endoftext|>