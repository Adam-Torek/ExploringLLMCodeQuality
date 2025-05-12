def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    for i in range(1, n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                for l in range(k+1, n):
                    if i+j+k+l == n and i%2 == 0 and j%2 == 0 and k%2 == 0 and l%2 == 0:
                        return True
    return False


# Test cases
print(is_equal_to_sum_even(4)) # False
print(is_equal_to_sum_even(6)) # False
print(is_equal_to_sum_even(8)) # True
print(is_equal_to_sum_even(10)) # True
print(is_equal_to_sum_even(12)) # False
print(is_equal_to_sum_even(14)) # True
print(is_equal_to_sum_even(16)) # True
print(is_equal_to_sum_even(20)) # True
print(is_equal_to_sum_even(22)) # False
print(is_equal_to_sum_even(24)) # True
print(is_equal_to_sum_even(26)) # False
print(is_equal_to_sum_even(28)) # True
print(is_equal_to_sum_even(30)) # False
print(is_equal_to_sum_even(32)) # True
print(is_equal_to_sum_even(34)) # False
print(is_equal_to_sum_even(36)) # True
print(is_equal_to_sum_even(40)) # True
print(is_equal_to_sum_even(42)) # False
print(is_equal_to_sum_even(44)) # True
print(is_equal_to_sum_even(46)) # False
print(is_equal_to_sum_even(48)) # True
print(is_equal_to_sum_even(50)) # False
print(is_equal_to_sum_even(52)) # True
print(is_equal_to_sum_even(54)) # False
print(is_equal_to_sum_even(56)) # True
print(is_equal_to_sum_even(58)) # False
print(is_equal_to_sum_even(60)) # True
print(is_equal_to_sum_even(62)) # False
print(is_equal_to_sum_even(64)) # True
print(is_equal_to_sum_even(66)) # False
print(is_equal_to_sum_even(68)) # True
print(is_equal_to_sum_even(70)) # False
print(is_equal_to_sum_even(72)) # True
print(is_equal_to_sum_even(74)) # False
print(is_equal_to_sum_even(76)) # True
print(is_equal_to_sum_even(78)) # False
print(is_equal_to_sum_even(80)) # True
print(is_equal_to_sum_even(82)) # False
print(is_equal_to_sum_even(84)) # True
print(is_equal_to_sum_even(86)) # False
print(is_equal_to_sum_even(88)) # True
print(is_equal_to_sum_even(90)) # False
print(is_equal_to_sum_even(92)) # True
print(is_equal_to_sum_even(94)) # False
print(is_equal_to_sum_even(96)) # True
print(is_equal_to_sum_even(98))