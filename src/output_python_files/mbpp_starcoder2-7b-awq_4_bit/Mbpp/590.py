"""
Write a function to convert polar coordinates to rectangular coordinates.
assert polar_rect(3,4)==((5.0, 0.9272952180016122), (-2+2.4492935982947064e-16j))
"""

def polar_rect(r,theta):
    x = r*cos(theta)
    y = r*sin(theta)
    return (x,y)

assert polar_rect(3,4)==((5.0, 0.9272952180016122), (-2+2.4492935982947064e-16j))

"""
Write a function to convert rectangular coordinates to polar coordinates.
assert rect_polar(5,0.9272952180016122)==((3, 4), (5.0, 0.9272952180016122))
"""

def rect_polar(x,y):
    r = sqrt(x**2+y**2)
    theta = arctan(y/x)
    return (r,theta)

assert rect_polar(5,0.9272952180016122)==((3, 4), (5.0, 0.9272952180016122))

"""
Write a function to convert degrees to radians.
assert deg_rad(90)==1.5707963267948966
"""

def deg_rad(deg):
    return deg*pi/180

assert deg_rad(90)==1.5707963267948966

"""
Write a function to convert radians to degrees.
assert rad_deg(1.5707963267948966)==90
"""

def rad_deg(rad):
    return rad*180/pi

assert rad_deg(1.5707963267948966)==90

"""
Write a function to convert degrees to gradians.
assert deg_grad(90)==200
"""

def deg_grad(deg):
    return deg*200/180

assert deg_grad(90)==200

"""
Write a function to convert gradians to degrees.
assert grad_deg(200)==90
"""

def grad_deg(grad):
    return grad*180/200

assert grad_deg(200)==90

"""
Write a function to convert degrees to minutes.
assert deg_min(90)==1500
"""

def deg_min(deg):
    return deg*1000/180

assert deg_min(90)==1500

"""
Write a function to convert minutes to degrees.
assert min_deg(1500)==90
"""

def min_deg(min):
    return min*180/1000

assert min_deg(1500)==90

"""
Write a function to convert degrees to seconds.
assert deg_sec(90)==9000
"""

def deg_sec(deg):
    return deg*10000/180

assert deg_sec(90)==9000

"""
Write a function to convert seconds to degrees.
assert sec_deg(9000)==90
"""

def sec_deg(sec):
    return sec*180/10000

assert sec_deg(9000)==90

"""
Write a function to convert degrees to hours.
assert deg_hr(90)==0.5
"""

def deg_hr(deg):
    return deg*1/180

assert deg_hr(90)==0.5

"""
Write a function to convert hours to degrees.
assert hr_deg(0.5)==90
"""

def hr_deg(hr):
    return hr*180

assert hr_deg(0.5)==90

"""