"""
Write a python function to check whether the count of divisors is even. https://www.w3resource.com/python-exercises/basic/python-basic-1-exercise-24.php
assert count_divisors(10)
"""

def count_divisors(n):
    count = 0
    for i in range(1, n+1):
        if n % i == 0:
            count += 1
    return count % 2 == 0

# Test cases
print(count_divisors(10)) # Output: True
print(count_divisors(15)) # Output: False<|endoftext|>