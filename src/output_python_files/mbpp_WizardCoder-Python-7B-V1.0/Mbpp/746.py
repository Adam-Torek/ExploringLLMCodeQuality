"""
Write a function to find area of a sector. The function takes the radius and angle as inputs. Function should return None if the angle is larger than 360 degrees.
assert sector_area(4,45)==6.283185307179586
"""
import math

def sector_area(radius, angle):
    if angle > 360:
        return None
    else:
        return radius**2 * angle * math.sin(math.radians(angle))

print(sector_area(4,45))

# Test cases
assert sector_area(4,45) == 6.283185307179586
assert sector_area(5,90) == 78.539816339744834
assert sector_area(6,180) == None
assert sector_area(7,270) == None
assert sector_area(8,360) == 200.465633862996651
assert sector_area(9,720) == 113.0973355529232542
assert sector_area(10,10) == 157.0796326777686457
assert sector_area(11,360) == 314.15926535897931
assert sector_area(12,720) == 452.631072726812565
assert sector_area(13,1440) == 628.318530717958647
assert sector_area(14,2880) == 986.66904292673566
assert sector_area(15,360) == None
assert sector_area(16,720) == None
assert sector_area(17,1080) == None
assert sector_area(18,1440) == None
assert sector_area(19,180) == 154.608009207071165
assert sector_area(20,360) == 314.15926535897931
assert sector_area(21,720) == 628.318530717958647
assert sector_area(22,1080) == 986.66904292673566
assert sector_area(23,1440) == 1477.507462026367753
assert sector_area(24,180) == 176.0319854132737414
assert sector_area(25,360) == None
assert sector_area(26,720) == None
assert sector_area(27,1080) == None
assert sector_area(28,1440) == None
assert sector_area(29,180) == 176.0319854132737414
assert sector_area(30,360) == 314.15926535897931
assert sector_area(31,720) == 628.318530717958647
assert sector_area(32,1080) == 986.66904292673566
assert sector_area(33,1440) == 1477.507462026367753