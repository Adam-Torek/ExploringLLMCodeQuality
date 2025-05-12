"""
Write a function to convert rgb color to hsv color. https://www.geeksforgeeks.org/program-change-rgb-color-model-hsv-color-model/
assert rgb_to_hsv(255, 255, 255)==(0, 0.0, 100.0)
"""

def rgb_to_hsv(r, g, b):
    r, g, b = r/255.0, g/255.0, b/255.0
    mx = max(r, g, b)
    mn = min(r, g, b)
    df = mx-mn
    if mx == mn:
        h = 0
    elif mx == r:
        h = (60 * ((g-b)/df) + 360) % 360
    elif mx == g:
        h = (60 * ((b-r)/df) + 120) % 360
    elif mx == b:
        h = (60 * ((r-g)/df) + 240) % 360
    if mx == 0:
        s = 0
    else:
        s = df/mx
    v = mx
    return h, s, v

def test_rgb_to_hsv():
    assert rgb_to_hsv(255, 255, 255)==(0, 0.0, 100.0)
    assert rgb_to_hsv(0, 0, 0)==(0, 0.0, 0.0)
    assert rgb_to_hsv(255, 0, 0)==(0, 1.0, 100.0)
    assert rgb_to_hsv(0, 255, 0)==(120, 1.0, 100.0)
    assert rgb_to_hsv(0, 0, 255)==(240, 1.0, 100.0)
    assert rgb_to_hsv(128, 128, 128)==(0, 0.0, 50.0)
    assert rgb_to_hsv(128, 0, 0)==(0, 1.0, 50.0)
    assert rgb_to_hsv(0, 128, 0)==(120, 1.0, 50.0)
    assert rgb_to_hsv(0, 0, 128)==(240, 1.0, 50.0)
    assert rgb_to_hsv(255, 255, 0)==(60, 1.0, 100.0)
    assert rgb_to_hsv(255, 0, 255)==(300, 1.0, 100.0)
    assert rgb_to_hsv(0, 255, 255)==(180, 1.0, 100.0)
    assert rgb_to_hsv(255, 128, 0)==(60, 0.5, 100.0)
    assert rgb_to_hsv(255, 0, 128)==(300, 0.5, 100.0)
    assert rgb_to_hsv(0, 255, 128)==(180, 0.5, 100.0)
    assert rgb_to_hsv(128, 255, 0)==(60, 0.5, 100.0)
    assert rgb_to_hsv(0, 128, 255)==(300, 0.5, 100.0)
    assert rgb_to_hsv(128, 0, 255)==(180, 0.5, 100.0)
    assert rgb_to_hsv(128, 128, 128)==