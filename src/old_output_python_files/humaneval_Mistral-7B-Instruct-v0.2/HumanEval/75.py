def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    # Your code here
    for i in range(2, int(a**0.5)+1):
        if a % i == 0:
            return False
    for j in [2,3,5]:
        if a % j != 0:
            continue
        a //= j
        if a == 1:
            return True
    return False

# Testing
print(is_multiply_prime(30)) # True
print(is_multiply_prime(25)) # False
print(is_multiply_prime(15)) # False
print(is_multiply_prime(12)) # False
print(is_multiply_prime(11)) # False
print(is_multiply_prime(2)) # True
print(is_multiply_prime(3)) # True
print(is_multiply_prime(5)) # True
print(is_multiply_prime(7)) # True
print(is_multiply_prime(13)) # True
print(is_multiply_prime(17)) # True
print(is_multiply_prime(19)) # True
print(is_multiply_prime(23)) # True
print(is_multiply_prime(29)) # True
print(is_multiply_prime(31)) # True
print(is_multiply_prime(37)) # True
print(is_multiply_prime(43)) # True
print(is_multiply_prime(47)) # True
print(is_multiply_prime(53)) # True
print(is_multiply_prime(59)) # True
print(is_multiply_prime(61)) # True
print(is_multiply_prime(67)) # True
print(is_multiply_prime(71)) # True
print(is_multiply_prime(73)) # True
print(is_multiply_prime(79)) # True
print(is_multiply_prime(83)) # True
print(is_multiply_prime(89)) # True
print(is_multiply_prime(97)) # True
print(is_multiply_prime(101)) # True
print(is_multiply_prime(103)) # True
print(is_multiply_prime(107)) # True
print(is_multiply_prime(109)) # True
print(is_multiply_prime(113)) # True
print(is_multiply_prime(127)) # True
print(is_multiply_prime(131)) # True
print(is_multiply_prime(137)) # True
print(is_multiply_prime(139)) # True
print(is_multiply_prime(149)) # True
print(is_multiply_prime(151)) # True
print(is_multiply_prime(157)) # True
print(is_multiply_prime(163)) # True
print(is_multiply_prime(167)) # True
print(is_multiply_prime(173)) # True
print(is_multiply_prime(179)) # True
print(is_multiply_prime(181)) # True
print(is_multiply_prime(191)) # True
print(is_multiply_prime(193)) # True
print(is_multiply_prime(197)) # True
print(is_multiply_prime(199)) # True
print(is_multiply_prime(211)) # True
print(is_multiply_prime(223)) # True
print(is_multiply_prime(227)) # True
print(is_multiply_prime(229)) # True
print(is_multiply_prime(233)) # True
print(is_multiply_prime