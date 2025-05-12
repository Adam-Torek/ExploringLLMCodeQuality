"""
Write a function to get the angle of a complex number.
assert math.isclose(angle_complex(0,1j), 1.5707963267948966, rel_tol=0.001)
"""

import math

def angle_complex(z):
    """
    Returns the angle of a complex number z in radians.
    """
    return math.phase(z)