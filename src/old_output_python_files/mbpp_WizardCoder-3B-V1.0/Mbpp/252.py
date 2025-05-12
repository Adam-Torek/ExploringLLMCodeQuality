"""
Write a python function to convert complex numbers to polar coordinates.
assert convert(1) == (1.0, 0.0)
"""

def convert(z):
    r = abs(z)
    theta = angle(z)
    return (r, theta)

def angle(z):
    return (z.real**2 + z.imag**2)**0.5<|endoftext|>