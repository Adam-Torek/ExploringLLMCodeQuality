"""
Write a function to find the directrix of a parabola.
assert parabola_directrix(5,3,2)==-198
"""

def parabola_directrix(a,b,c):
    """
    Finds the directrix of a parabola given the coefficients a, b, and c.
    """
    # Find the discriminant
    d = b**2 - 4*a*c
    # Find the vertex
    x_vertex = -b/(2*a)
    y_vertex = f(x_vertex)
    # Find the directrix
    x_directrix = -b/(2*a)
    y_directrix = -c/(2*a)
    # Return the directrix
    return (x_directrix, y_directrix)

def f(x):
    """
    Returns the y value of the parabola given the x value.
    """
    return a*x**2 + b*x + c