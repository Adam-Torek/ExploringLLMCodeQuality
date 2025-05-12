"""
Write a function to get the angle of a complex number.
assert math.isclose(angle_complex(0,1j), 1.5707963267948966, rel_tol=0.001)
"""
import math

def angle_complex(z):
    """
    Calculate the angle of a complex number in radians.
    :param z: complex number
    :return: angle in radians
    """
    arg = math.atan2(z.imag, z.real)
    return arg

if __name__ == "__main__":
    import math

    assert math.isclose(angle_complex(0,1j), 1.5707963267948966, rel_tol=0.001)
    print("Test passed!")