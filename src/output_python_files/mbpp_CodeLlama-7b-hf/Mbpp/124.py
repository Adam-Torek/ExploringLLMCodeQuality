"""
Write a function to get the angle of a complex number.
assert math.isclose(angle_complex(0,1j), 1.5707963267948966, rel_tol=0.001)
"""

import math


def angle_complex(real, imag):
    """
    Get the angle of a complex number.
    """
    if real == 0 and imag == 0:
        return 0
    if real == 0:
        if imag > 0:
            return math.pi / 2
        else:
            return -math.pi / 2
    if imag == 0:
        if real > 0:
            return 0
        else:
            return math.pi
    if real > 0:
        if imag > 0:
            return math.atan(imag / real)
        else:
            return math.pi + math.atan(imag / real)
    else:
        if imag > 0:
            return math.pi * 2 + math.atan(imag / real)
        else:
            return math.pi * 2 + math.atan(imag / real)


if __name__ == "__main__":
    print(angle_complex(0, 1j))
    print(angle_complex(0, -1j))
    print(angle_complex(1, 0))
    print(angle_complex(1, 1))
    print(angle_complex(1, -1))
    print(angle_complex(-1, 0))
    print(angle_complex(-1, 1))
    print(angle_complex(-1, -1))
    print(angle_complex(1, 1j))
    print(angle_complex(1, -1j))
    print(angle_complex(-1, 1j))
    print(angle_complex(-1, -1j))
    print(angle_complex(1j, 0))
    print(angle_complex(1j, 1))
    print(angle_complex(1j, -1))
    print(angle_complex(-1j, 0))
    print(angle_complex(-1j, 1))
    print(angle_complex(-1j, -1))
    print(angle_complex(1j, 1j))
    print(angle_complex(1j, -1j))
    print(angle_complex(-1j, 1j))
    print(angle_complex(-1j, -1j))
    print(angle_complex(1, 1j))
    print(angle_complex(1, -1j))
    print(angle_complex(-1, 1j))
    print(angle_complex(-1, -1j))
    print(angle_complex(1j, 1))
    print(angle_complex(1j, -1))
    print(angle_complex(-1j, 1))
    print(angle_complex(-1j, -1))
    print(angle_complex(1, 1j))
    print(angle_complex(1, -1j))
    print(angle_complex(-1, 1j))
    print(angle_complex(-1, -1j))
    print(angle_complex(1j, 1))
    print(angle_complex(1j, -1))
    print(angle_complex(-1j, 1))
    print(angle_complex(-1j, -1))
    print(angle_complex(1, 1j))
    print(angle_complex(1, -1j))
    print(angle_complex(-1, 1j))
    print(angle_complex(-1, -1j))
    print(angle_complex(1j, 1))
    print(angle_complex(1j, -1))
    print(angle_complex(-1j, 1))
    print(angle_complex(-1j, -1))
    print(angle_complex(1, 1j))
    print(angle_complex(1, -1j))
    print(angle_complex(-1, 1j))
    print(angle_complex(-1, -1j))
    print(angle_complex(1j, 1))
    print(angle_complex(1j, -1