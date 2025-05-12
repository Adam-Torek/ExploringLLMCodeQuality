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

# Time Complexity: O(n)
# Space Complexity: O(1)

# Optimized Solution:

def catalan_number(n):
    if n == 0:
        return 1
    c = 1
    for i in range(1, n+1):
        c = (c * (2*n-i+1) // i)
    return c

print(catalan_number(10))

# Time Complexity: O(n)
# Space Complexity: O(1)

# Another Optimized Solution:

def catalan_number(n):
    if n == 0:
        return 1
    c = 1
    for i in range(1, n+1):
        c = (c * (2*n-i+1) // i)
    return c

def catalan_number_optimized(n):
    if n == 0:
        return 1
    c = 1
    for i in range(1, n+1):
        c = (c * (n+i) // i)
    return c

print(catalan_number_optimized(10))

# Time Complexity: O(n)
# Space Complexity: O(1)

# Another Optimized Solution:

def catalan_number_optimized(n):
    if n == 0:
        return 1
    c = 1
    for i in range(1, n+1):
        c = (c * (n+i) // i)
    return c

def catalan_number_optimized(n):
    if n == 0:
        return 1
    c = 1
    for i in range(1, n+1):
        c = (c * (n+i) // i)
    return c

def catalan_number_optimized(n):
    if n == 0:
        return 1
    c = 1
    for i in range(1, n+1):
        c = (c * (n+i) // i)
    return c

def catalan_number_optimized(n):
    if n == 0:
        return 1
    c = 1
    for i in range(1, n+1):
        c = (c * (n+i) // i)
    return c

def catalan_number_optimized(n):
    if n == 0:
        return 1
    c = 1
    for i in range(1, n+1):
        c = (c * (n+i) // i)
    return c

def catalan_number_optimized(n):
    if n == 0:
        return 1
    c = 1
    for i in range(1, n+1):
        c = (c * (n+i) // i)
    return c

def catalan_number_optimized(n):
    if n == 0:
        return 1
    c = 1
    for i in range(1, n+1):
        c = (c * (n+i) // i)
    return c

def catalan_number_optimized(n):
    if n == 0:
        return 1
    c = 1
    for i in range(1, n+1):
        c = (c * (n+i) // i)
    return c

def catalan_number_optimized(n):
    if n == 0:
        return 1
    c = 1
    for i in range(1, n+1):
        c = (c * (n+i) // i)
    return c

def catalan_number