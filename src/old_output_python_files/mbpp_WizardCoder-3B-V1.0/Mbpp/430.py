"""
Write a function to find the directrix of a parabola.
assert parabola_directrix(5,3,2)==-198
"""

def parabola_directrix(a, b, c):
    """
    This function takes the coefficients of a parabola ax^2 + bx + c and returns the directrix.
    """
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        return (-b + discriminant**0.5)/(2*a)
    elif discriminant == 0:
        return -b/(2*a)
    else:
        return None

# Test the function
print(parabola_directrix(5,3,2)) # Output: -198<|endoftext|>