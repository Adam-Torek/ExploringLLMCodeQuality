def is_simple_power(x, n):
    """Your task is to write a function that returns true if a number x is a simple
    power of n and false in other cases.
    x is a simple power of n if n**int=x
    For example:
    is_simple_power(1, 4) => true
    is_simple_power(2, 2) => true
    is_simple_power(8, 2) => true
    is_simple_power(3, 2) => false
    is_simple_power(3, 1) => false
    is_simple_power(5, 3) => false
    """
    return x == n ** int(x ** (1 / n))



# Test cases
print(is_simple_power(1, 4))  # True
print(is_simple_power(2, 2))  # True
print(is_simple_power(8, 2))  # True
print(is_simple_power(3, 2))  # False
print(is_simple_power(1, 1))  # True
print(is_simple_power(5, 3))  # False
print(is_simple_power(10, 2))  # False
print(is_simple_power(16, 2))  # True
print(is_simple_power(27, 3))  # False
print(is_simple_power(100, 10))  # True
print(is_simple_power(10000, 10))  # False
print(is_simple_power(10000, 100))  # True
print(is_simple_power(100000, 10))  # False
print(is_simple_power(100000, 100))  # True
print(is_simple_power(1000000, 10))  # False
print(is_simple_power(1000000, 100))  # True
print(is_simple_power(10000000, 10))  # False
print(is_simple_power(10000000, 100))  # True
print(is_simple_power(100000000, 10))  # False
print(is_simple_power(100000000, 100))  # True
print(is_simple_power(1000000000, 10))  # False
print(is_simple_power(1000000000, 100))  # True
print(is_simple_power(10000000000, 10))  # False
print(is_simple_power(10000000000, 100))  # True
print(is_simple_power(100000000000, 10))  # False
print(is_simple_power(100000000000, 100))  # True
print(is_simple_power(1000000000000, 10))  # False
print(is_simple_power(1000000000000, 100))  # True
print(is_simple_power(10000000000000, 10))  # False
print(is_simple_power(10000000000000, 100))  # True
print(is_simple_power(100000000000000, 10))  # False
print(is_simple_power(100000000000000, 100))  # True
print(is_simple_power(1000000000000000, 10))  # False
print(is_simple_power(1000000000000000, 10