"""
Write a function to convert rgb color to hsv color. https://www.geeksforgeeks.org/program-change-rgb-color-model-hsv-color-model/
assert rgb_to_hsv(255, 255, 255)==(0, 0.0, 100.0)
"""


def rgb_to_hsv(r, g, b):
    """
    :param r: red
    :param g: green
    :param b: blue
    :return: hue, saturation, value
    """
    r, g, b = r / 255.0, g / 255.0, b / 255.0
    max_color = max(r, g, b)
    min_color = min(r, g, b)
    delta = max_color - min_color
    if max_color == 0:
        return 0, 0, 0
    else:
        saturation = delta / max_color
        if r == max_color:
            hue = (g - b) / delta
        elif g == max_color:
            hue = 2 + (b - r) / delta
        else:
            hue = 4 + (r - g) / delta
        hue = hue / 6.0
        if hue < 0:
            hue = hue + 1
        value = max_color
        return hue, saturation, value


if __name__ == '__main__':
    print(rgb_to_hsv(255, 255, 255))
    print(rgb_to_hsv(255, 0, 0))
    print(rgb_to_hsv(0, 255, 0))
    print(rgb_to_hsv(0, 0, 255))
    print(rgb_to_hsv(0, 0, 0))
    print(rgb_to_hsv(128, 128, 128))
    print(rgb_to_hsv(128, 128, 0))
    print(rgb_to_hsv(128, 0, 128))
    print(rgb_to_hsv(0, 128, 128))
    print(rgb_to_hsv(128, 0, 0))
    print(rgb_to_hsv(0, 128, 0))
    print(rgb_to_hsv(0, 0, 128))
    print(rgb_to_hsv(128, 128, 128))
    print(rgb_to_hsv(128, 128, 0))
    print(rgb_to_hsv(128, 0, 128))
    print(rgb_to_hsv(0, 128, 128))
    print(rgb_to_hsv(128, 0, 0))
    print(rgb_to_hsv(0, 128, 0))
    print(rgb_to_hsv(0, 0, 128))
    print(rgb_to_hsv(128, 128, 128))
    print(rgb_to_hsv(128, 128, 0))
    print(rgb_to_hsv(128, 0, 128))
    print(rgb_to_hsv(0, 128, 128))
    print(rgb_to_hsv(128, 0, 0))
    print(rgb_to_hsv(0, 128, 0))
    print(rgb_to_hsv(0, 0, 128))
    print(rgb_to_hsv(128, 128