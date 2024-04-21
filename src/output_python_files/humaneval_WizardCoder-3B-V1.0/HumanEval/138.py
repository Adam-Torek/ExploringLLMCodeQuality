def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """

# Solution:
# We can solve this problem by iterating through all possible sums of 4 positive even numbers and checking if they are equal to n.
# If we find a sum that is equal to n, we return True. Otherwise, we continue iterating.
# If we reach the end of the loop without finding a sum that is equal to n, we return False.

def is_equal_to_sum_even(n):
    for i in range(2, n//2+1):
        if n - i % 2 == i % 2:
            return True
    return False

# Test cases
print(is_equal_to_sum_even(4))  # False
print(is_equal_to_sum_even(6))  # False
print(is_equal_to_sum_even(8))  # True<|endoftext|>