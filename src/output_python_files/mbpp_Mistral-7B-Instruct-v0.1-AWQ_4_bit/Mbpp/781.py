"""
Write a python function to check whether the count of divisors is even. https://www.w3resource.com/python-exercises/basic/python-basic-1-exercise-24.php
assert count_divisors(10)
"""

def count_divisors(n):
    count = 1
    for i in range(2, n+1):
        if n % i == 0:
            count += 1
    return count


if __name__ == "__main__":
    assert count_divisors(10) == 4
    assert count_divisors(15) == 6
    assert count_divisors(20) == 8
    assert count_divisors(25) == 10
    assert count_divisors(30) == 12