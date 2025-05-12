def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """
    if n > 1:
        for i in range(2, n):
            if (n % i) == 0:
                return y
        return x
    else:
        return y

# Test cases
print(x_or_y(7, 34, 12)) # Output: 34
print(x_or_y(15, 8, 5)) # Output: 5
print(x_or_y(1, 10, 20)) # Output: 20
print(x_or_y(2, 10, 20)) # Output: 20
print(x_or_y(3, 10, 20)) # Output: 10
print(x_or_y(4, 10, 20)) # Output: 20
print(x_or_y(5, 10, 20)) # Output: 10
print(x_or_y(6, 10, 20)) # Output: 20
print(x_or_y(7, 10, 20)) # Output: 10
print(x_or_y(8, 10, 20)) # Output: 20
print(x_or_y(9, 10, 20)) # Output: 20
print(x_or_y(10, 10, 20)) # Output: 20
print(x_or_y(11, 10, 20)) # Output: 10
print(x_or_y(12, 10, 20)) # Output: 20
print(x_or_y(13, 10, 20)) # Output: 10
print(x_or_y(14, 10, 20)) # Output: 20
print(x_or_y(15, 10, 20)) # Output: 20
print(x_or_y(16, 10, 20)) # Output: 20
print(x_or_y(17, 10, 20)) # Output: 10
print(x_or_y(18, 10, 20)) # Output: 20
print(x_or_y(19, 10, 20)) # Output: 20
print(x_or_y(20, 10, 20)) # Output: 20
print(x_or_y(21, 10, 20)) # Output: 20
print(x_or_y(22, 10, 20)) # Output: 20
print(x_or_y(23, 10, 20)) # Output: 10
print(x_or_y(24, 10, 20)) # Output: 20
print(x_or_y(25, 10, 20)) # Output: 20
print(x_or_y(26, 10, 20)) # Output: 20
print(x_or_y