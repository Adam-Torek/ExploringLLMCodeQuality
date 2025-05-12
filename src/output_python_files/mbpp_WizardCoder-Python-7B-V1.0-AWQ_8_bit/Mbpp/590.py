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

# Output: ((5.0, 0.9272952180016122), (-2+2.4492935982947064e-16j))