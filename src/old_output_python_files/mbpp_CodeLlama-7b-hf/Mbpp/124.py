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
    print(angle_complex(1, 1j))
    print(angle_complex(1, 0))
    print(angle_complex(1, -1j))
    print(angle_complex(0, -1j))
    print(angle_complex(-1, -1j))
    print(angle_complex(-1, 0))
    print(angle_complex(-1, 1j))
    print(angle_complex(0, 1j))
    print(angle_complex(0, 0))
    print(angle_complex(1, 0))
    print(angle_complex(1, 1j))
    print(angle_complex(1, 2j))
    print(angle_complex(1, 3j))
    print(angle_complex(1, 4j))
    print(angle_complex(1, 5j))
    print(angle_complex(1, 6j))
    print(angle_complex(1, 7j))
    print(angle_complex(1, 8j))
    print(angle_complex(1, 9j))
    print(angle_complex(1, 10j))
    print(angle_complex(1, 11j))
    print(angle_complex(1, 12j))
    print(angle_complex(1, 13j))
    print(angle_complex(1, 14j))
    print(angle_complex(1, 15j))
    print(angle_complex(1, 16j))
    print(angle_complex(1, 17j))
    print(angle_complex(1, 18j))
    print(angle_complex(1, 19j))
    print(angle_complex(1, 20j))
    print(angle_complex(1, 21j))
    print(angle_complex(1, 22j))
    print(angle_complex(1, 23j))
    print(angle_complex(1, 24j))
    print(angle_complex(1, 25j))
    print(angle_complex(1, 26j))
    print(angle_complex(1, 27j))
    print(angle_complex(1, 28j))
    print(angle_complex(1, 29j))
    print(angle_complex(1, 30j))
    print(angle_complex(1, 31j))
    print(angle_complex(1, 32j))
    print(angle_complex(1, 33j))
    print(angle_complex(1, 34j))
    print(angle_complex(1, 35j))
    print(angle_complex(1, 36j))
    print(angle_complex(1, 37j))
    print(angle_complex(1, 38j))
    print(angle_complex(1, 39j