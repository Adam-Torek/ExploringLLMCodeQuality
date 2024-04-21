"""
Write a function to find the directrix of a parabola.
assert parabola_directrix(5,3,2)==-198
"""
def parabola_directrix(a, h, k):
    """
    Finds the equation of the directrix of a parabola given its vertex (h,k) and focus (a,0).
    """
    return -(h + a) / 2

assert parabola_directrix(5,3,2) == -198 # Directrix of parabola y^2 = 4x - 11 intersects x-axis at x = -198
assert parabola_directrix(1,1,1) == -3 # Directrix of parabola y^2 = x intersects x-axis at x = -3
assert parabola_directrix(3,0,0) == 0 # Directrix of parabola y^2 = x intersects x-axis at x = 0
assert parabola_directrix(1,1,3) == -2 # Directrix of parabola y^2 = 4(x-1) + 3 intersects x-axis at x = -2</s>