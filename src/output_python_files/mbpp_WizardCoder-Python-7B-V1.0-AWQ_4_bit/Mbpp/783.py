"""
Write a function to convert rgb color to hsv color. https://www.geeksforgeeks.org/program-change-rgb-color-model-hsv-color-model/
assert rgb_to_hsv(255, 255, 255)==(0, 0.0, 100.0)
"""
import math

def rgb_to_hsv(r, g, b):
    r, g, b = r/255.0, g/255.0, b/255.0
    cmax, cmin = max(r, g, b), min(r, g, b)
    delta = cmax - cmin
    if delta == 0:
        h = 0
    elif cmax == r:
        h = (((g - b) / delta) % 6)
    elif cmax == g:
        h = (b - r) / delta + 2
    else:
        h = (r - g) / delta + 4
    h = round(60 * h)
    if h < 0:
        h += 360
    s = 0 if cmax == 0 else (cmax - cmin) / cmax
    v = cmax
    return h, s, v

print(rgb_to_hsv(255, 255, 255))

# Test cases
assert rgb_to_hsv(255, 255, 255) == (0, 0.0, 100.0)
assert rgb_to_hsv(0, 0, 0) == (0, 0.0, 0.0)
assert rgb_to_hsv(255, 0, 0) == (0, 1.0, 100.0)
assert rgb_to_hsv(0, 255, 0) == (120, 1.0, 100.0)
assert rgb_to_hsv(0, 0, 255) == (240, 1.0, 100.0)
assert rgb_to_hsv(255, 255, 0) == (60, 1.0, 100.0)
assert rgb_to_hsv(255, 0, 255) == (180, 1.0, 100.0)
assert rgb_to_hsv(0, 255, 255) == (300, 1.0, 100.0)
assert rgb_to_hsv(255, 127.5, 0) == (60, 1.0, 50.0)
assert rgb_to_hsv(255, 0, 127.5) == (120, 1.0, 50.0)
assert rgb_to_hsv(0, 255, 127.5) == (180, 1.0, 50.0)
assert rgb_to_hsv(127.5, 255, 0) == (300, 1.0, 50.0)
assert rgb_to_hsv(127.5, 0, 255) == (60, 1.0, 50.0)
assert rgb_to_hsv(0, 127.5, 255) == (120, 1.0, 50.0)
assert rgb_to_hsv(255, 255, 127.5) == (30, 1.0, 50.0)
assert rgb_to_hsv(127.5, 255, 255) == (90, 1.0, 50.0)
assert