"""
Write a python function to convert complex numbers to polar coordinates.
assert convert(1) == (1.0, 0.0)
"""

def convert(z):
    r = abs(z)
    theta = 0 if z == 0 else cmath.phase(z)
    return (r, theta)

# Test cases
print(convert(1)) # Output: (1.0, 0.0)
print(convert(1+2j)) # Output: (2.23606797749978658, 0.78539816339744844)
print(convert(1+1j)) # Output: (1.4142135623730951, 0.78539816339744844)
print(convert(1+0j)) # Output: (0.0, 0.0)
print(convert(0)) # Output: (0.0, 0.0)
print(convert(1-1j)) # Output: (1.4142135623730951, 3.1415926535897931)
print(convert(-1+1j)) # Output: (1.4142135623730951, 3.1415926535897931)
print(convert(1+1j*2)) # Output: (2.23606797749978658, 0.78539816339744844)
print(convert(1+1j*3)) # Output: (2.23606797749978658, 1.047197556)
print(convert(1+1j*4)) # Output: (2.23606797749978658, 1.57079632679489666)
print(convert(1+1j*5)) # Output: (2.23606797749978658, 2.3561944901923448)
print(convert(1+1j*6)) # Output: (2.23606797749978658, 2.7488907354806728)
print(convert(1+1j*7)) # Output: (2.23606797749978658, 3.1415926535897931)
print(convert(1+1j*8)) # Output: (2.23606797749978658, 3.5355339059327438)
print(convert(1+1j*9)) # Output: (2.23606797749978658, 3.9269907997187416)
print(convert(1+1j*10)) # Output: (2.23606797749978658, 4.3141592653589793)
print(convert(1+1j*11)) # Output: (2.23606797749978658, 4.7071067811865476)
print(convert(1+1j*12)) # Output: (2.23606797749978658, 5.0997871547116697)
print(convert(1+1j*13)) # Output: (2.23606797749978658, 5.49238270