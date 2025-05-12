"""
Write a python function to convert complex numbers to polar coordinates.
assert convert(1) == (1.0, 0.0)
"""

def convert(complex_number):
    """
    Convert a complex number to polar coordinates.
    """
    real_part = complex_number.real
    imag_part = complex_number.imag
    magnitude = (real_part**2 + imag_part**2) ** 0.5
    angle = (180/3.14159) * (2 * (180/3.14159) * (math.atan(imag_part/real_part)))
    return (magnitude, angle)

# Test the function
print(convert(1))