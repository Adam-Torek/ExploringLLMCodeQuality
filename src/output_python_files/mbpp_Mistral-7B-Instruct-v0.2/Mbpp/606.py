"""
Write a function to convert degrees to radians.
assert radian_degree(90)==1.5707963267948966
"""
import math

def radian_degree(degrees):
    """
    :param degrees: float or int
    :return: float
    """
    return math.radians(degrees)

if __name__ == "__main__":
    assert radian_degree(90) == 1.5707963267948966, "Test failed"
    print("Test passed")