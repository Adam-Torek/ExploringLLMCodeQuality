"""
Write a function to convert rgb color to hsv color. https://www.geeksforgeeks.org/program-change-rgb-color-model-hsv-color-model/
assert rgb_to_hsv(255, 255, 255)==(0, 0.0, 100.0)
"""
import math

def rgb_to_hsv(r, g, b):
    """
    Converts an RGB color to HSV color
    :param r: Red component of RGB color
    :param g: Green component of RGB color
    :param b: Blue component of RGB color
    :return: A tuple of three values representing Hue, Saturation and Value of the HSV color
    """
    max_value = max(r, g, b)
    min_value = min(r, g, b)

    # Calculate hue
    if max_value == min_value:
        hue = 0
    elif max_value == r:
        hue = (g - b) / (max_value - min_value)
    elif max_value == g:
        hue = 2.0 + (b - r) / (max_value - min_value)
    else:
        hue = 4.0 + (r - g) / (max_value - min_value)

    hue *= 60.0

    # Calculate saturation and value
    saturation = 0.0
    if max_value != 0:
        saturation = 1.0 - min_value / max_value

    value = max_value

    return hue, saturation, value

if __name__ == "__main__":
    assert rgb_to_hsv(255, 255, 255) == (0, 0.0, 100.0)
    assert rgb_to_hsv(0, 0, 255) == (240.0, 100.0, 100.0)
    assert rgb_to_hsv(255, 0, 0) == (0.0, 100.0, 100.0)
    assert rgb_to_hsv(255, 128, 0) == (30.0, 100.0, 100.0)
    assert rgb_to_hsv(255, 255, 0) == (60.0, 100.0, 100.0)
    assert rgb_to_hsv(0, 255, 255) == (120.0, 100.0, 100.0)
    assert rgb_to_hsv(255, 255, 128) == (60.0, 100.0, 94.1176)
    assert rgb_to_hsv(255, 128, 128) == (30.0, 50.0, 94.1176)
    assert rgb_to_hsv(128, 128, 128) == (0.0, 0.0, 50.0)
    assert rgb_to_hsv(0, 0, 0) == (0.0, 0.0, 0.0)
    assert rgb_to_hsv(128, 0, 0) == (336.0, 100.0, 100.0)
    assert rgb_to_hsv(128, 128, 0) == (315.0, 50.0, 94.1176)
    assert rgb_to_hsv(0, 128, 0) == (150.0, 100.0, 100.0)
    assert rgb_to_hsv(0, 128, 128) == (180.0, 50.0, 94.1176