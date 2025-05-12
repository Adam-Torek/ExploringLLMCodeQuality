"""
Write a function to convert polar coordinates to rectangular coordinates.
assert polar_rect(3,4)==((5.0, 0.9272952180016122), (-2+2.4492935982947064e-16j))
"""

import math

def polar_rect(r,theta):
    x = r*math.cos(theta)
    y = r*math.sin(theta)
    return (x,y)

def rect_polar(x,y):
    r = math.sqrt(x**2 + y**2)
    theta = math.atan2(y,x)
    return (r,theta)

def test_polar_rect():
    assert polar_rect(3,4)==((5.0, 0.9272952180016122), (-2+2.4492935982947064e-16j))
    assert polar_rect(2,3)==((3.464102530563936j, 1.7323888300841898j), (-1.7323888300841898j, 3.464102530563936j))
    assert polar_rect(0,0)==((0.0, 0.0j), (0.0, 0.0j))
    assert polar_rect(1,0)==((1.0, 0.0j), (0.0, 0.0j))
    assert polar_rect(1,math.pi)==((1.0, 0.0j), (0.0, 0.0j))
    assert polar_rect(1,math.pi/2)==((1.0, 0.0j), (0.0, 0.0j))
    assert polar_rect(1,math.pi/4)==((1.0, 0.0j), (0.0, 0.0j))
    assert polar_rect(1,math.pi/3)==((1.0, 0.0j), (0.0, 0.0j))
    assert polar_rect(1,math.sqrt(2))==((1.0, 0.0j), (0.0, 0.0j))
    assert polar_rect(1,math.sqrt(2)/2)==((1.0, 0.0j), (0.0, 0.0j))
    assert polar_rect(1,math.sqrt(2)/3)==((1.0, 0.0j), (0.0, 0.0j))
    assert polar_rect(1,math.sqrt(2)/4)==((1.0, 0.0j), (0.0, 0.0j))
    assert polar_rect(1,math.sqrt(2)/6)==((1.0, 0.0j), (0.0, 0.0j))
    assert polar_rect(1,math.sqrt(2)/2*1j)==((1.0, 0.0j), (0.0, 0.0j))
    assert polar_rect(1,math.sqrt(2)/2*2j)==((1.0, 0.0j), (0.0, 0.0j))
    assert polar_rect(1,math.sqrt(2)/2*3j)==((1.0, 0.0j), (0.0, 0.0j))
    assert polar_rect(1,math.sqrt(2)/2*4j)==((1.0, 0.0j), (0.0, 0.0j))
    assert polar_rect(1,math.sqrt(2)/2*5j)==((1.0, 0.0j), (0.0, 0.0j))
    assert polar_rect(1,math.sqrt(2)/2*6j)==((1.0, 0.0j), (0.0, 0.0j))
    assert polar_