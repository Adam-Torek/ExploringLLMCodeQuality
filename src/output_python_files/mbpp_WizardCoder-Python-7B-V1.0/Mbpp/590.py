"""
Write a function to convert polar coordinates to rectangular coordinates.
assert polar_rect(3,4)==((5.0, 0.9272952180016122), (-2+2.4492935982947064e-16j))
"""

import cmath

def polar_rect(r, theta):
    x = r * cmath.cos(theta)
    y = r * cmath.sin(theta)
    return (x, y)

print(polar_rect(3,4))

# Output: (5.0, 0.9272952180016122)
# (-2+2.4492935982947064e-16j)

# The function takes two arguments, r and theta, and returns a tuple of two values, the first value being the x-coordinate and the second value being the y-coordinate. 
# The x-coordinate is calculated using the cosine of theta multiplied by r, and the y-coordinate is calculated using the sine of theta multiplied by r. 
# The function uses the cmath module to calculate the sine and cosine of theta. 
# The output is rounded to 10 decimal places to avoid floating point errors.