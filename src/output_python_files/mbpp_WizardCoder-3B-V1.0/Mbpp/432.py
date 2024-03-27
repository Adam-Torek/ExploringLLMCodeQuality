"""
Write a function to find the median length of a trapezium.
assert median_trapezium(15,25,35)==20
"""

def median_trapezium(a,b,c):
    # sort the three sides
    sides = sorted([a,b,c])
    # calculate the length of the trapezium
    length = (sides[0] + sides[1]) / 2
    # calculate the area of the trapezium
    area = sides[0] * sides[1]
    # calculate the height of the trapezium
    height = (sides[2] - sides[0]) / 2
    # calculate the area of the base
    base_area = sides[0] * height
    # calculate the area of the top
    top_area = sides[1] * height
    # calculate the area of the trapezium
    trapezium_area = area - base_area - top_area
    # calculate the median length of the trapezium
    median_length = length * (trapezium_area / (area + base_area + top_area))
    return median_length<|endoftext|>