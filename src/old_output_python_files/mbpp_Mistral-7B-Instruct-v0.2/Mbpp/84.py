"""
Write a function to find the nth number in the newman conway sequence.
assert sequence(10) == 6
"""
def sequence(n):
    a, b, c = 0, 1, 1
    for _ in range(n):
        a, b, c = b, c, a + b
    return c

assert sequence(10) == 6
assert sequence(1) == 1
assert sequence(2) == 1
assert sequence(3) == 2
assert sequence(4) == 3
assert sequence(5) == 5
assert sequence(6) == 8
assert sequence(7) == 13
assert sequence(8) == 21
assert sequence(9) == 34
assert sequence(10) == 55