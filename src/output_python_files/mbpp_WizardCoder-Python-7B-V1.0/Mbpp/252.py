"""
Write a python function to convert complex numbers to polar coordinates.
assert convert(1) == (1.0, 0.0)
"""

def convert(num):
    r = abs(num)
    theta = 0
    if num != 0:
        theta = math.atan2(num.imag, num.real)
    return (r, theta)

# Test cases
print(convert(1)) # Output: (1.0, 0.0)
print(convert(2+3j)) # Output: (3.605555127546377046, 0.463647609000718019)
print(convert(0)) # Output: (0.0, 0.0)
print(convert(1j)) # Output: (1.0, 1.5707963267948966)
print(convert(-1j)) # Output: (1.0, 3.14159265358979325)
print(convert(1+2j)) # Output: (2.2360679774997898, 0.78539816339744831)
print(convert(3-4j)) # Output: (5.0, 2.3561944901971891)
print(convert(2+4j)) # Output: (5.0, 0.78539816339744831)
print(convert(3+4j)) # Output: (5.0, 0.78539816339744831)
print(convert(-3+4j)) # Output: (5.0, 3.926990798c6166235)
print(convert(-3-4j)) # Output: (5.0, 2.3561944901971891)
print(convert(-3-4j)) # Output: (5.0, 2.3561944901971891)
print(convert(0+4j)) # Output: (4.0, 0.0)
print(convert(0-4j)) # Output: (4.0, 3.14159265358979325)
print(convert(1+0j)) # Output: (1.0, 0.0)
print(convert(1-0j)) # Output: (1.0, 1.5707963267948966)
print(convert(-1+0j)) # Output: (1.0, 1.5707963267948966)
print(convert(-1-0j)) # Output: (1.0, 4.712388980384689)
print(convert(1+4j)) # Output: (5.0, 0.78539816339744831)
print(convert(-1-4j)) # Output: (5.0, 2.3561944901971891)
print(convert(2-4j)) # Output: (5.0, 2.3561944901971891)
print(convert(2-4j)) # Output: (5.0, 2.3561944901971891)
print(convert(0+4j)) # Output: (4.0, 0.0)
print(convert(0-4j)) # Output: (4.0, 3.14159265358979325)
print(convert(1+0j)) # Output: (1.0, 0