def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """
    if n == 2:
        return x
    if n == 3:
        return x
    if n % 2 == 0:
        return y
    for i in range(3, n, 2):
        if n % i == 0:
            return y
    return x


# Testing code

x = 34
y = 12
print(x_or_y(7, x, y))

x = 8
y = 5
print(x_or_y(15, x, y))