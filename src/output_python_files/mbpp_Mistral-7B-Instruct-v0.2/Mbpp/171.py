"""
Write a function to find the perimeter of a regular pentagon from the length of its sides.
assert perimeter_pentagon(5) == 25
"""
import math

def perimeter_pentagon(sides_length):
    """
    Calculate the perimeter of a regular pentagon
    :param sides_length: length of one side of the pentagon
    :return: the perimeter of the regular pentagon
    """
    sides_number = 5
    perimeter = sides_length * sides_number
    return perimeter

if __name__ == "__main__":
    assert perimeter_pentagon(5) == 25
    print("Test passed")