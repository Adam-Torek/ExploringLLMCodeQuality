"""
Write a function to find area of a sector. The function takes the radius and angle as inputs. Function should return None if the angle is larger than 360 degrees.
assert sector_area(4,45)==6.283185307179586
"""
import math

def sector_area(radius, angle):
    if angle > 360:
        return None
    else:
        return radius * radius * math.sin(math.radians(angle/2))

print(sector_area(4,45))

# Test cases
assert sector_area(4,45) == 6.283185307179586
assert sector_area(5,90) == 78.5398163397448485
assert sector_area(3,120) == None
assert sector_area(2,180) == None
assert sector_area(1,360) == 12.56637061435917
assert sector_area(0,0) == 0
assert sector_area(1,0) == 0
assert sector_area(1,180) == 0
assert sector_area(1,360) == 3.141592653589793
assert sector_area(1,720) == 12.56637061435917
assert sector_area(1,1080) == 25.13274122871124
assert sector_area(1,270) == 0
assert sector_area(1,30) == 0.0019669934299875211417
assert sector_area(1,300) == None
assert sector_area(1,10000) == None
assert sector_area(1,100000) == None
assert sector_area(1,3600) == None
assert sector_area(1,7200) == None
assert sector_area(1,1000000) == None
assert sector_area(1,10000000) == None
assert sector_area(1,100000000) == None
assert sector_area(1,1000000000) == None
assert sector_area(1,10000000000) == None
assert sector_area(1,100000000000) == None
assert sector_area(1,1000000000000) == None
assert sector_area(1,10000000000000) == None
assert sector_area(1,100000000000000) == None
assert sector_area(1,1000000000000000) == None
assert sector_area(1,10000000000000000) == None
assert sector_area(1,100000000000000000) == None
assert sector_area(1,1000000000000000000) == None
assert sector_area(1,10000000000000000000) == None
assert sector_area(1,100000000000000000000) == None
assert sector_area(1,1000000000000000000000) == None
assert sector_area(1,10000000000000000000000) == None
assert