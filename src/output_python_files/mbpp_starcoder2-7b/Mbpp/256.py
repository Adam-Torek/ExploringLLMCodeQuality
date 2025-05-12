"""
Write a python function that takes in a non-negative number and returns the number of prime numbers less than the given non-negative number.
assert count_Primes_nums(5) == 2
"""

def count_Primes_nums(num):
    if num < 2:
        return 0
    primes = [2]
    x = 3
    while x <= num:
        for y in range(3,x,2):
            if x%y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    print(primes)
    return len(primes)

print(count_Primes_nums(100))
/Python/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python_Practice/Python