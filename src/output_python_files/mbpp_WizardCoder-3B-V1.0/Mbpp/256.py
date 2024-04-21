"""
Write a python function that takes in a non-negative number and returns the number of prime numbers less than the given non-negative number.
assert count_Primes_nums(5) == 2
"""

def count_Primes_nums(n):
    count = 0
    for i in range(2, n):
        if all(i % j!= 0 for j in range(2, int(i**0.5)+1)):
            count += 1
    return count

# Test the function
assert count_Primes_nums(5) == 2<|endoftext|>