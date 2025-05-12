"""
Write a function to convert rgb color to hsv color. https://www.geeksforgeeks.org/program-change-rgb-color-model-hsv-color-model/
assert rgb_to_hsv(255, 255, 255)==(0, 0.0, 100.0)
"""

def rgb_to_hsv(r, g, b):
    """
    Converts an RGB color to an HSV color.

    Args:
        r (int): The red component of the RGB color.
        g (int): The green component of the RGB color.
        b (int): The blue component of the RGB color.

    Returns:
        tuple: A tuple of three floats representing the HSV color.
    """
    # Convert the RGB values to a list
    rgb = [r, g, b]

    # Normalize the RGB values
    rgb = [x / 255.0 for x in rgb]

    # Calculate the minimum and maximum values
    min_rgb = min(rgb)
    max_rgb = max(rgb)

    # Calculate the difference between the minimum and maximum values
    diff = max_rgb - min_rgb

    # Calculate the hue, saturation, and value
    hue = 0
    saturation = 0
    value = 0

    # If the difference between the minimum and maximum values is 0, the color is achromatic
    if diff == 0:
        saturation = 100
        value = max_rgb

    # If the difference between the minimum and maximum values is 1, the color is achromatic
    elif diff == 1:
        saturation = 100
        value = min_rgb

    # If the difference between the minimum and maximum values is greater than 1, the color is achromatic
    else:
        # Calculate the hue
        hue = (max_rgb - min_rgb) / diff

        # Calculate the saturation
        saturation = 100 * (1 - (max_rgb - min_rgb) / diff)

        # Calculate the value
        value = (max_rgb + min_rgb) / 2

    # Return the HSV color as a tuple
    return (hue, saturation, value)