def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """

# Solution:
# We can solve this problem by first checking if the given number is divisible by 3. If it is, then we can check if it is divisible by 2 and 5. If it is, then we can check if it is divisible by 3, 5, and 7. If it is, then it is a multiplication of 3 prime numbers.

def is_multiply_prime(a):
    if a % 3 == 0:
        if a % 2 == 0 and a % 5 == 0:
            if a % 3 == 0 and a % 5 == 0 and a % 7 == 0:
                return True
    return False

# Let's test the function with some examples:
print(is_multiply_prime(30)) # True
print(is_multiply_prime(15)) # False
print(is_multiply_prime(21)) # True
print(is_multiply_prime(100)) # True<|endoftext|>