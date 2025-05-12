"""
Write a function to convert rgb color to hsv color. https://www.geeksforgeeks.org/program-change-rgb-color-model-hsv-color-model/
assert rgb_to_hsv(255, 255, 255)==(0, 0.0, 100.0)
"""
import math

def rgb_to_hsv(r, g, b):
    """
    Convert RGB color to HSV color
    :param r: Red component of RGB color
    :param g: Green component of RGB color
    :param b: Blue component of RGB color
    :return: Tuple of HSV color (Hue, Saturation, Value)
    """
    max_value = max(r, g, b)
    min_value = min(r, g, b)

    # Hue calculation
    delta = max_value - min_value
    if max_value == 0:
        hue = 0
    elif delta > 0:
        hue = (g - b) / delta if max_value == g else (b - g) / delta
        hue *= 60.0
    else:
        hue = (g + b) / abs(delta) * 60.0
        hue += 360.0 if hue < 0 else 0

    # Saturation and Value calculation
    saturation = (max_value - min_value) / max_value if max_value > 0 else 0
    value = max_value

    return hue, saturation, value

if __name__ == "__main__":
    assert rgb_to_hsv(255, 255, 255) == (0, 0.0, 100.0)
    assert rgb_to_hsv(0, 0, 255) == (240.0, 100.0, 100.0)
    assert rgb_to_hsv(255, 0, 0) == (0, 100.0, 100.0)
    assert rgb_to_hsv(255, 128, 0) == (30.0, 100.0, 100.0)
    assert rgb_to_hsv(0, 128, 128) == (180.0, 50.0, 100.0)
    assert rgb_to_hsv(128, 128, 128) == (60.0, 0.0, 100.0)
    assert rgb_to_hsv(255, 255, 0) == (60.0, 100.0, 100.0)
    assert rgb_to_hsv(0, 0, 0) == (0, 0.0, 0.0)
    assert rgb_to_hsv(128, 128, 128) == (60.0, 0.0, 100.0)
    assert rgb_to_hsv(128, 128, 128) == (60.0, 0.0, 100.0)
    assert rgb_to_hsv(128, 128, 128) == (60.0, 0.0, 100.0)
    assert rgb_to_hsv(128, 128, 128) == (60.0, 0.0, 100.0)
    assert rgb_to_hsv(128, 128, 128) == (60.0, 0.0, 100.0)
    assert rgb_to_hsv(128, 128, 128) ==