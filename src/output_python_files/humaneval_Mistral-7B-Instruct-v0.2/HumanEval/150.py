def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """
    import math
    if math.isqrt(n) + 1 > 2:
        return y
    else:
        return x

# Testing the function
print(x_or_y(7, 34, 12))
print(x_or_y(15, 8, 5))
print(x_or_y(17, 34, 12))
print(x_or_y(2, 8, 5))