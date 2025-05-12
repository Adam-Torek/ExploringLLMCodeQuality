"""
Write a function to find area of a sector. The function takes the radius and angle as inputs. Function should return None if the angle is larger than 360 degrees.
assert sector_area(4,45)==6.283185307179586
"""
import math

def sector_area(radius, angle):
    if angle > 360:
        return None
    else:
        sector_angle = angle / 360 * 2 * math.pi
        area = (sector_angle / 2) * (radius ** 2)
        return area