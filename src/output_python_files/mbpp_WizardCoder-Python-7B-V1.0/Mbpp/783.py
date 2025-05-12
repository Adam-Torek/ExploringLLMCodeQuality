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
        hue = 0
    elif cmax == r:
        hue = 60 * ((g - b) / delta % 6)
    elif cmax == g:
        hue = 60 * ((b - r) / delta + 2)
    else:
        hue = 60 * ((r - g) / delta + 4)

    if cmax == 0:
        sat = 0
    else:
        sat = (cmax - cmin) / cmax

    val = cmax

    return hue, sat, val

print(rgb_to_hsv(255, 255, 255))

# Test cases
assert rgb_to_hsv(255, 255, 255) == (0, 0.0, 100.0)
assert rgb_to_hsv(0, 0, 0) == (0, 0.0, 0.0)
assert rgb_to_hsv(255, 0, 0) == (0, 100.0, 100.0)
assert rgb_to_hsv(0, 255, 0) == (120, 100.0, 100.0)
assert rgb_to_hsv(0, 0, 255) == (240, 100.0, 100.0)
assert rgb_to_hsv(255, 255, 0) == (60, 100.0, 100.0)
assert rgb_to_hsv(255, 0, 255) == (300, 100.0, 100.0)
assert rgb_to_hsv(0, 255, 255) == (180, 100.0, 100.0)
assert rgb_to_hsv(255, 128, 0) == (60, 50.0, 100.0)
assert rgb_to_hsv(255, 0, 128) == (300, 50.0, 100.0)
assert rgb_to_hsv(128, 255, 0) == (120, 50.0, 100.0)
assert rgb_to_hsv(0, 128, 255) == (180, 50.0, 100.0)
assert rgb_to_hsv(128, 0, 255) == (300, 50.0, 100.0)
assert rgb_to_hsv(255, 128, 255) == (120, 50.0, 100.0)
assert rgb_to_hsv(255, 255, 128) == (60, 50.0, 100.0)
assert rgb_to_hsv(128, 255, 128) == (