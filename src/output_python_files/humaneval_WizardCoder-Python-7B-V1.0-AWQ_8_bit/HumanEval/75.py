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
        if is_prime(a):
            count += 1
        if count == 3:
            return True
    return False


print(is_multiply_prime(30))  # True
print(is_multiply_prime(25))  # False
print(is_multiply_prime(15))  # False
print(is_multiply_prime(48))  # True
print(is_multiply_prime(24))  # False
print(is_multiply_prime(12))  # False
print(is_multiply_prime(36))  # True
print(is_multiply_prime(10))  # False
print(is_multiply_prime(27))  # True
print(is_multiply_prime(36))  # True
print(is_multiply_prime(42))  # False
print(is_multiply_prime(50))  # False
print(is_multiply_prime(75))  # True
print(is_multiply_prime(97))  # True
print(is_multiply_prime(100))  # False
print(is_multiply_prime(1))  # False
print(is_multiply_prime(0))  # False
print(is_multiply_prime(11))  # False
print(is_multiply_prime(2))  # False
print(is_multiply_prime(3))  # False
print(is_multiply_prime(5))  # False
print(is_multiply_prime(7))  # False
print(is_multiply_prime(13))  # False
print(is_multiply_prime(17))  # False
print(is_multiply_prime(23))  # False
print(is_multiply_prime(29))  # False
print(is_multiply_prime(31))  # False
print(is_multiply_prime(37))  # False
print(is_multiply_prime(41))  # False
print(is_multiply_prime(43))  # False
print(is_multiply_prime(47))  # False
print(is_multiply_prime(53))  # False
print(is_multiply_prime(59))  # False
print(is_multiply_prime(61))  # False
print(is_multiply_prime(67))  # False
print(is_multiply_prime(71))  # False
print(is_multiply_prime(73))  # False
print(is_multiply_prime(79))  # False
print(is_multiply_prime(83))  # False
print(is_multiply_prime(89))  # False
print(is_multiply_prime(97))  # False
print(is_multiply_prime(101))  # False
print(is_multiply_prime(103))  # False
print(is_multiply_prime(107))  # False
print(is_multiply_prime(109))  # False
print(is_multiply_prime(113))  # False
print(is_multiply_prime(127))  # False
print(is_multiply_prime(131))  # False
print(is_multiply_prime(137))  # False
print(is_multiply_prime(139))  # False
print(is_multiply_prime(149))  # False