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
    assert polar_rect(1,2)==((1.732306499761903, 0.9272952180016122), (-1.4142135623730951j, -0.9272952180016122))
    assert polar_rect(0,0)==((0.0, 0.0), (0.0, 0.0))
    assert polar_rect(1,0)==((1.0, 0.0), (0.0, 0.0))
    assert polar_rect(0,1)==((0.0, 0.0), (0.0, 1.0))
    assert polar_rect(-1,1)==((-1.0, 0.0), (0.0, 1.0))
    assert polar_rect(-1,0)==((-1.0, 0.0), (0.0, 0.0))
    assert polar_rect(1,-1)==((1.0, 0.0), (0.0, -1.0))
    assert polar_rect(-1,-1)==((-1.0, 0.0), (0.0, -1.0))
    assert polar_rect(0,0)==((0.0, 0.0), (0.0, 0.0))
    assert polar_rect(1,2)==((1.732306499761903, 0.9272952180016122), (-1.4142135623730951j, -0.9272952180016122))
    assert polar_rect(1,2)==((1.732306499761903, 0.9272952180016122), (-1.4142135623730951j, -0.9272952180016122))
    assert polar_rect(1,2)==((1.732306499761903, 0.9272952180016122), (-1.4142135623730951j, -0.9272952180016122))
    assert polar_rect(1,2)==((1.732306499761903, 0.9272952180016122), (-1.4142135623730951j, -0.9272952180016122))
    assert polar_rect(1,2)==((1.732306499761903, 0.9272952180016122), (-1.