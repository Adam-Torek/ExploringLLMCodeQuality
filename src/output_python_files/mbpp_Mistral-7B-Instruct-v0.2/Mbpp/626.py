"""
Write a python function to find the area of the largest triangle that can be inscribed in a semicircle with a given radius.
assert triangle_area(-1) == None
"""
from math import pi, sqrt, pow


def triangle_area(semi_circle_radius):
    if semi_circle_radius <= 0:
        return None

    side_length = semi_circle_radius * sqrt(3) / 2
    return pi * pow(side_length / 2, 2)


if __name__ == "__main__":
    radius = float(input("Enter the radius of the semicircle: "))
    area = triangle_area(radius)
    if area is not None:
        print(f"The area of the largest triangle that can be inscribed in a semicircle with a radius of {radius} is {area:.2f}")
    else:
        print("Invalid input")