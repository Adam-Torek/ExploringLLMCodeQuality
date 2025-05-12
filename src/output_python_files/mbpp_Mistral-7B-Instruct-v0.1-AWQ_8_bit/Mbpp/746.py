"""
Write a function to find area of a sector. The function takes the radius and angle as inputs. Function should return None if the angle is larger than 360 degrees.
assert sector_area(4,45)==6.283185307179586
"""

def sector_area(r, angle):
    if angle > 360:
        return None
    else:
        return (r**2)*(angle/360)