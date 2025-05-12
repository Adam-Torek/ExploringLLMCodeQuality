"""
Write a python function to check whether the count of divisors is even. https://www.w3resource.com/python-exercises/basic/python-basic-1-exercise-24.php
assert count_divisors(10)
"""
from math import sqrt

def count_divisors(n):
    count = 0
    i = 1
    while i <= sqrt(n):
        if n % i == 0:
            count += 1
            if i != n // i:
                count += 1
        i += 1
    return count

def is_even_count(n):
    return count_divisors(n) % 2 == 0

if __name__ == "__main__":
    assert is_even_count(10)
    assert not is_even_count(11)
    assert is_even_count(12)
    assert not is_even_count(13)
    assert is_even_count(14)
    assert not is_even_count(15)
    print("All tests passed.")