def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True

    count = 0
    for i in range(2, 10):
        if is_prime(i) and a % i == 0:
            count += 1
            if count == 3:
                return True
    return False


print(is_multiply_prime(30))  # True
print(is_multiply_prime(25))  # False
print(is_multiply_prime(45))  # True
print(is_multiply_prime(60))  # False
print(is_multiply_prime(75))  # False
print(is_multiply_prime(90))  # True
print(is_multiply_prime(100))  # False


# Another solution:
def is_multiply_prime(a):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True

    count = 0
    for i in range(2, a):
        if is_prime(i) and a % i == 0:
            count += 1
            if count == 3:
                return True
    return False


print(is_multiply_prime(30))  # True
print(is_multiply_prime(25))  # False
print(is_multiply_prime(45))  # True
print(is_multiply_prime(60))  # False
print(is_multiply_prime(75))  # False
print(is_multiply_prime(90))  # True
print(is_multiply_prime(100))  # False

# Another solution:
def is_multiply_prime(a):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True

    count = 0
    for i in range(2, a):
        if is_prime(i) and a % i == 0:
            count += 1
            if count == 3:
                return True
    return False


print(is_multiply_prime(30))  # True
print(is_multiply_prime(25))  # False
print(is_multiply_prime(45))  # True
print(is_multiply_prime(60))  # False
print(is_multiply_prime(75))  # False
print(is_multiply_prime(90))  # True
print(is_multiply_prime(100))  # False

# Another solution:
def is_multiply_prime(a):
    def is_prime(n):
        if n <