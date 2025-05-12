def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n % 2 != 0:
        return False
    for i in range(int(n/2), 0, -2):
        if n - i - (i+2) // 2 - (i+2) // 2 == 0:
            return True
    return False

# test
print(is_equal_to_sum_even(4))
print(is_equal_to_sum_even(6))
print(is_equal_to_sum_even(8))
print(is_equal_to_sum_even(10))
print(is_equal_to_sum_even(12))
print(is_equal_to_sum_even(14))
print(is_equal_to_sum_even(16))
print(is_equal_to_sum_even(18))
print(is_equal_to_sum_even(20))