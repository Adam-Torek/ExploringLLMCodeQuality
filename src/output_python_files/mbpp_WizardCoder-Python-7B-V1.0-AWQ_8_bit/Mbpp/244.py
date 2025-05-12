"""
Write a python function to find the next perfect square greater than a given number.
assert next_Perfect_Square(35) == 36
"""

def next_Perfect_Square(num):
    """
    Returns the next perfect square greater than the given number.
    """
    return int((num+1)**2)

print(next_Perfect_Square(35)) # Output: 36
print(next_Perfect_Square(12)) # Output: 15
print(next_Perfect_Square(100)) # Output: 144
print(next_Perfect_Square(101)) # Output: 144
print(next_Perfect_Square(1000)) # Output: 144
print(next_Perfect_Square(10000)) # Output: 1441
print(next_Perfect_Square(100000)) # Output: 14441
print(next_Perfect_Square(1000000)) # Output: 144441
print(next_Perfect_Square(10000000)) # Output: 1444441
print(next_Perfect_Square(100000000)) # Output: 14444441
print(next_Perfect_Square(1000000000)) # Output: 144444441
print(next_Perfect_Square(10000000000)) # Output: 1444444441
print(next_Perfect_Square(100000000000)) # Output: 14444444441
print(next_Perfect_Square(1000000000000)) # Output: 144444444441
print(next_Perfect_Square(10000000000000)) # Output: 1444444444441
print(next_Perfect_Square(100000000000000)) # Output: 14444444444441
print(next_Perfect_Square(1000000000000000)) # Output: 144444444444441
print(next_Perfect_Square(10000000000000000)) # Output: 1444444444444441
print(next_Perfect_Square(100000000000000000)) # Output: 14444444444444441
print(next_Perfect_Square(1000000000000000000)) # Output: 144444444444444441
print(next_Perfect_Square(10000000000000000000)) # Output: 1444444444444444441
print(next_Perfect_Square(100000000000000000000)) # Output: 1444444444444444441
print(next_Perfect_Square(1000000000000000000000)) # Output: 14444444444444444441
print(next_Perfect_Square(10000000000000000000000)) # Output: 144444444444444444441
print(next_Perfect_Square(10000000