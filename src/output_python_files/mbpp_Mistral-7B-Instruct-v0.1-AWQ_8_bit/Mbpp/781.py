"""
Write a python function to check whether the count of divisors is even. https://www.w3resource.com/python-exercises/basic/python-basic-1-exercise-24.php
assert count_divisors(10)
"""

def count_divisors(n):
    count = 0
    for i in range(1, n+1):
        if n % i == 0:
            count += 1
    return count


if __name__ == "__main__":
    n = int(input("Enter a number: "))
    if count_divisors(n) % 2 == 0:
        print(f"The number {n} has an even number of divisors.")
    else:
        print(f"The number {n} has an odd number of divisors.")