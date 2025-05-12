def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    # your code here
    for i in range(2, int(a**0.5)+1):
        if a % i == 0:
            return False
    for j in range(2, int(a**0.5)+1):
        if a % j == 0 and is_multiply_prime(j) and is_multiply_prime(a//j):
            return True
    return False

# Testing
print(is_multiply_prime(30)) # True
print(is_multiply_prime(25)) # False
print(is_multiply_prime(15)) # True
print(is_multiply_prime(12)) # False
print(is_multiply_prime(11)) # True
print(is_multiply_prime(10)) # False
print(is_multiply_prime(9)) # False
print(is_multiply_prime(8)) # False
print(is_multiply_prime(7)) # True
print(is_multiply_prime(6)) # False
print(is_multiply_prime(5)) # True
print(is_multiply_prime(4)) # False
print(is_multiply_prime(3)) # True
print(is_multiply_prime(2)) # False
print(is_multiply_prime(1)) # False