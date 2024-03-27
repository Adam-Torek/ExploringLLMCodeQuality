"""
Write a function to find the perimeter of a regular pentagon from the length of its sides.
assert perimeter_pentagon(5) == 25
"""
import math

def perimeter_pentagon(sides_length):
    """
    Calculate the perimeter of a regular pentagon given the length of one side.
    """
    sides_number = 5
    side_length = sides_length
    perimeter = sides_number * side_length
    return perimeter

assert perimeter_pentagon(5) == 25</s>