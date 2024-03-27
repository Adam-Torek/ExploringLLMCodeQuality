"""
Write a function to convert rgb color to hsv color. https://www.geeksforgeeks.org/program-change-rgb-color-model-hsv-color-model/
assert rgb_to_hsv(255, 255, 255)==(0, 0.0, 100.0)
"""

def rgb_to_hsv(r, g, b):
    r, g, b = r/255, g/255, b/255
    max_val = max(r, g, b)
    min_val = min(r, g, b)
    h, s, v = 0, 0, max_val
    delta = max_val - min_val
    if max_val!= 0:
        s = delta / max_val
    if delta!= 0:
        if max_val == r:
            h = (g - b) / delta
        elif max_val == g:
            h = 2 + (b - r) / delta
        else:
            h = 4 + (r - g) / delta
        h *= 60
        if h < 0:
            h += 360
    return (h, s*100, v*100)

assert rgb_to_hsv(255, 255, 255)==(0, 0.0, 100.0)<|endoftext|>