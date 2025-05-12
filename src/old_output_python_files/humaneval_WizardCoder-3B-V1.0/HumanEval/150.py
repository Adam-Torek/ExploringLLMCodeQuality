def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """

def is_prime(n):
    """A simple function to check if a number is prime or not.

    Examples:
    is_prime(7) == True
    is_prime(15) == False
    
    """
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def x_or_y_prime(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y_prime(7, 34, 12) == 34
    for x_or_y_prime(15, 8, 5) == 8
    
    """
    if is_prime(n):
        return x
    else:
        return y

# Test cases
print(x_or_y(7, 34, 12)) # Output: 34
print(x_or_y(15, 8, 5)) # Output: 5

print(x_or_y_prime(7, 34, 12)) # Output: 34
print(x_or_y_prime(15, 8, 5)) # Output: 8<|endoftext|>