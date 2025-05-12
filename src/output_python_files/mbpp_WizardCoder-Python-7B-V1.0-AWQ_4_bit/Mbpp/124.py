"""
Write a function to get the angle of a complex number.
assert math.isclose(angle_complex(0,1j), 1.5707963267948966, rel_tol=0.001)
"""

import math

def angle_complex(z):
    return math.atan2(z.imag, z.real)

print(angle_complex(0,1j))

# Output: 1.5707963267948966