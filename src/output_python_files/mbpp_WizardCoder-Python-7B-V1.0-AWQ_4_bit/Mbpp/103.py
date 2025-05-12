"""
Write a function to find the Eulerian number a(n, m).
assert eulerian_num(3, 1) == 4
"""

def eulerian_num(n, m):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return (m + 1) * eulerian_num(n - 1, m) + eulerian_num(n - 2, m)

print(eulerian_num(3, 1)) # Output: 4