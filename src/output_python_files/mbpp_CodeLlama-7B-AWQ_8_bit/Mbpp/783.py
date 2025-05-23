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
    max_ = max(r, g, b)
    min_ = min(r, g, b)
    h = 0
    if max_ == min_:
        h = 0
    elif max_ == r:
        h = (g - b) / (max_ - min_)
    elif max_ == g:
        h = 2 + (b - r) / (max_ - min_)
    elif max_ == b:
        h = 4 + (r - g) / (max_ - min_)
    s = (max_ - min_) / max_
    v = max_
    return h, s, v


if __name__ == '__main__':
    print(rgb_to_hsv(255, 255, 255))
    print(rgb_to_hsv(255, 0, 0))
    print(rgb_to_hsv(0, 255, 0))
    print(rgb_to_hsv(0, 0, 255))
    print(rgb_to_hsv(0, 0, 0))
    print(rgb_to_hsv(255, 255, 0))
    print(rgb_to_hsv(255, 0, 255))
    print(rgb_to_hsv(0, 255, 255))
    print(rgb_to_hsv(128, 128, 128))
    print(rgb_to_hsv(128, 128, 0))
    print(rgb_to_hsv(128, 0, 128))
    print(rgb_to_hsv(0, 128, 128))
    print(rgb_to_hsv(128, 128, 128))
    print(rgb_to_hsv(128, 128, 0))
    print(rgb_to_hsv(128, 0, 128))
    print(rgb_to_hsv(0, 128, 128))
    print(rgb_to_hsv(128, 128, 128))
    print(rgb_to_hsv(128, 128, 0))
    print(rgb_to_hsv(128, 0, 128))
    print(rgb_to_hsv(0, 128, 128))
    print(rgb_to_hsv(128, 128, 128))
    print(rgb_to_hsv(128, 128, 0))
    print(rgb_to_hsv(128, 0, 128))
    print(rgb_to_hsv(0, 128, 128))
    print(rgb_to_hsv(128, 128, 128))
    print(rgb_to_hsv(128, 128, 0))
    print(rgb_to_hsv(128, 0, 128))
    print(rgb_to_hsv(0, 128, 128))
    print(rgb_to_hsv(128, 128, 128))
    print(rgb_to_h