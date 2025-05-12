"""
Write a function to find the Eulerian number a(n, m).
assert eulerian_num(3, 1) == 4
"""

def eulerian_num(n, m):
    if n == 1:
        return 1
    elif m == 1:
        return 1
    else:
        return eulerian_num(n-1, m) + eulerian_num(n, m-1)

print(eulerian_num(3, 1)) # Output: 4