"""
Write a function to convert degrees to radians.
assert radian_degree(90)==1.5707963267948966
"""

def radian_degree(degrees):
    """
    Convert degrees to radians
    """
    return degrees * math.pi/180


if __name__ == '__main__':
    assert radian_degree(90)==1.5707963267948966