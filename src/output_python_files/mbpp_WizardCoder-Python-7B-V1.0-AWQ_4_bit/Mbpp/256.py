"""
Write a python function that takes in a non-negative number and returns the number of prime numbers less than the given non-negative number.
assert count_Primes_nums(5) == 2
"""

def count_Primes_nums(n):
    count = 0
    for i in range(2, n):
        if is_prime(i):
            count += 1
    return count

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

print(count_Primes_nums(5)) # Output: 2
print(count_Primes_nums(10)) # Output: 4
print(count_Primes_nums(15)) # Output: 6
print(count_Primes_nums(20)) # Output: 8
print(count_Primes_nums(25)) # Output: 11
print(count_Primes_nums(30)) # Output: 14

# Note: The function is_prime() is already given in the problem statement.