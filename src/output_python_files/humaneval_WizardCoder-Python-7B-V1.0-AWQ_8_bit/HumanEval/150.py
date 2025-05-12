def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                return y
        return x
    else:
        return y

# Test cases
print(x_or_y(7, 34, 12)) # Output: 34
print(x_or_y(15, 8, 5)) # Output: 5
print(x_or_y(1, 10, 20)) # Output: 20
print(x_or_y(2, 10, 20)) # Output: 20
print(x_or_y(0, 10, 20)) # Output: 20
print(x_or_y(-1, 10, 20)) # Output: 20
print(x_or_y(1, 10, 20)) # Output: 20

# Test cases for edge cases
print(x_or_y(0, 10, 20)) # Output: 20
print(x_or_y(-1, 10, 20)) # Output: 20
print(x_or_y(1, 10, 20) # Output: 10
print(x_or_y(2, 10, 20) # Output: 10