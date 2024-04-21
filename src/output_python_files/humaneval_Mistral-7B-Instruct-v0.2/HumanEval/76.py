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
    for i in range(1, int(math.log(x, n))+1):
        if math.pow(n, i) == x:
            return True
    return False

# Testing
import math
print(is_simple_power(1, 4)) # true
print(is_simple_power(2, 2)) # true
print(is_simple_power(8, 2)) # true
print(is_simple_power(3, 2)) # false
print(is_simple_power(3, 1)) # false
print(is_simple_power(5, 3)) # false</s>