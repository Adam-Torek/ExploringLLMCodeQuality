"""
Write a function to convert rgb color to hsv color. https://www.geeksforgeeks.org/program-change-rgb-color-model-hsv-color-model/
assert rgb_to_hsv(255, 255, 255)==(0, 0.0, 100.0)
"""

def rgb_to_hsv(r, g, b):
    """
    Convert rgb color to hsv color
    """
    # Convert rgb to grayscale
    gray = (r + g + b) / 3

    # Calculate the difference between the max and min values
    d = max(r, g, b) - min(r, g, b)

    # Calculate the hue value
    h = 0
    if d == 0:
        h = 0
    elif d == r:
        h = (g - b) / d
    elif d == g:
        h = (b - r) / d + 2
    elif d == b:
        h = (r - g) / d + 4
    else:
        h = 6

    # Calculate the saturation value
    s = d / 255

    # Calculate the value
    v = 255 - d

    # Return the hsv color
    return (h, s, v)


# Test the function
print(rgb_to_hsv(255, 255, 255))