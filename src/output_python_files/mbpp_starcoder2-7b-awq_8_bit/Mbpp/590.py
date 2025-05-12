"""
Write a function to convert polar coordinates to rectangular coordinates.
assert polar_rect(3,4)==((5.0, 0.9272952180016122), (-2+2.4492935982947064e-16j))
"""

def polar_rect(r,theta):
    x = r*cos(theta)
    y = r*sin(theta)
    return (x,y)

print(polar_rect(3,4))

"""
Write a function to convert rectangular coordinates to polar coordinates.
assert rect_polar(5,0.9272952180016122)==((3.0, 4.0), (-2+2.4492935982947064e-16j))
"""

def rect_polar(x,y):
    r = sqrt(x**2+y**2)
    theta = arctan(y/x)
    return (r,theta)

print(rect_polar(5,0.9272952180016122))

"""
Write a function to convert degrees to radians.
assert deg_rad(90)==1.5707963267948966
"""

def deg_rad(deg):
    return deg*pi/180

print(deg_rad(90))

"""
Write a function to convert radians to degrees.
assert rad_deg(1.5707963267948966)==90
"""

def rad_deg(rad):
    return rad*180/pi

print(rad_deg(1.5707963267948966))

"""
Write a function to convert degrees to radians.
assert deg_rad(90)==1.5707963267948966
"""

def deg_rad(deg):
    return deg*pi/180

print(deg_rad(90))

"""
Write a function to convert radians to degrees.
assert rad_deg(1.5707963267948966)==90
"""

def rad_deg(rad):
    return rad*180/pi

print(rad_deg(1.5707963267948966))

"""
Write a function to convert degrees to radians.
assert deg_rad(90)==1.5707963267948966
"""

def deg_rad(deg):
    return deg*pi/180

print(deg_rad(90))

"""
Write a function to convert radians to degrees.
assert rad_deg(1.5707963267948966)==90
"""

def rad_deg(rad):
    return rad*180/pi

print(rad_deg(1.5707963267948966))

"""
Write a function to convert degrees to radians.
assert deg_rad(90)==1.5707963267948966
"""

def deg_rad(deg):
    return deg*pi/180

print(deg_rad(90))

"""
Write a function to convert radians to degrees.
assert rad_deg(1.5707963267948966)==90
"""

def rad_deg(rad):
    return rad*180/pi

print(rad_deg(1.5707963267948966))

"""
Write a function to convert degrees to radians.
assert deg_rad(90)==1.5707963267948966
"""

def deg_rad(deg):
    return deg*pi/180

print(deg_rad(90))

"""
Write a function to convert radians to degrees.
assert rad_deg(1.5707963267948966)==90
"""