"""
Write a function to find the lateral surface area of a cone given radius r and the height h.
assert lateralsurface_cone(5,12)==204.20352248333654
"""
import math

def lateralsurface_cone(r,h):
    return math.pi * r * r + math.pi * r * h

print(lateralsurface_cone(5,12))

# Test cases
assert lateralsurface_cone(5,12) == 204.2035224833654
assert lateralsurface_cone(10, 20) == 314.1592653589793
assert lateralsurface_cone(1, 1) == 12.56637061435918
assert lateralsurface_cone(0, 10) == 12.56637061435918
assert lateralsurface_cone(10, 0) == 0
assert lateralsurface_cone(0, 0) == 0
assert lateralsurface_cone(1, -10) == 0
assert lateralsurface_cone(-10, 1) == 0
assert lateralsurface_cone(10, -1) == 0
assert lateralsurface_cone(-1, 10) == 0
assert lateralsurface_cone(10, 10) == 314.1592653589793
assert lateralsurface_cone(10, 10.5) == 314.1592653589793
assert lateralsurface_cone(10.5, 10) == 314.1592653589793
assert lateralsurface_cone(10.5, 10.5) == 314.1592653589793
assert lateralsurface_cone(10.5, 10.5) == 314.1592653589793
assert lateralsurface_cone(10.5, 10.5) == 314.1592653589793
assert lateralsurface_cone(10.5, 10.5) == 314.1592653589793
assert lateralsurface_cone(10.5, 10.5) == 314.1592653589793
assert lateralsurface_cone(10.5, 10.5) == 314.1592653589793
assert lateralsurface_cone(10.5, 10.5) == 314.1592653589793
assert lateralsurface_cone(10.5, 10.5) == 314.1592653589793
assert lateralsurface_cone(10.5, 10.5) == 314.1592653589793
assert lateralsurface_cone(10.5, 10.5) == 314.1592653589793
assert lateralsurface_cone(10.5, 10.5) == 314.1592653589793
assert lateralsurface_cone(10.5, 10.5) == 314.1592653589793
assert lateralsurface_cone(10.5, 10.5) == 314.1592653589793
assert lateralsurface_cone(10.5, 10.5