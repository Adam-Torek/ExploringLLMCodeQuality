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
    return n ** int(x) == x



# Test cases
print(is_simple_power(1, 4))  # True
print(is_simple_power(2, 2))  # True
print(is_simple_power(8, 2))  # True
print(is_simple_power(3, 2))  # False
print(is_simple_power(1, 1))  # True
print(is_simple_power(5, 3))  # False
print(is_simple_power(10, 2))  # False
print(is_simple_power(10, 3))  # False
print(is_simple_power(10, 5))  # False
print(is_simple_power(10, 10))  # True
print(is_simple_power(10, 11))  # False
print(is_simple_power(10, 0))  # False
print(is_simple_power(0, 10))  # False
print(is_simple_power(0, 0))  # False