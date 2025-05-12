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
    if n == 1:
        return x == 1
    if n == 2:
        return x == 4 or x == 1
    if x % n != 0:
        return False
    return x == n ** int(x / n)


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
print(is_simple_power(1000, 10))  # False
print(is_simple_power(1000, 100))  # False
print(is_simple_power(1000, 101))  # False
print(is_simple_power(1000, 1000))  # False
print(is_simple_power(1000, 101))  # False
print(is_simple_power(1000, 101))  # False
print(is_simple_power(1000, 1000))  # False
print(is_simple_power(1000, 1000))  # False
print(is_simple_power(1000, 10000))  # False
print(is_simple_power(10000, 1000))  # True
print(is_simple_power(10000, 10000))  # True
print(is_simple_power(10000, 10001))  # False
print(is_simple_power(10000, 100000))  # False
print(is_simple_power(100000, 1000))  # True
print(is_simple_power(100000, 10000))  # True
print(is_simple_power(100000, 10001))  # False
print(is_simple_power(100000, 100000))  # True
print(is_simple_power(100000, 10000