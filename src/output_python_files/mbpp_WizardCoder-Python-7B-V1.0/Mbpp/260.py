"""
Write a function to find the nth newman–shanks–williams prime number.
assert newman_prime(3) == 7
"""
import math

def newman_prime(n):
    if n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        i = 4
        while True:
            is_prime = True
            for j in range(2, int(math.sqrt(i))+1):
                if i % j == 0:
                    is_prime = False
                    break
            if is_prime:
                n -= 1
                if n == 0:
                    return i
            i += 2

print(newman_prime(3))
print(newman_prime(10))
print(newman_prime(100))
print(newman_prime(10000))
print(newman_prime(100000))
print(newman_prime(1000000))
print(newman_prime(10000000))
print(newman_prime(100000000))
print(newman_prime(1000000000))
print(newman_prime(10000000000))
print(newman_prime(100000000000))
print(newman_prime(1000000000000))
print(newman_prime(10000000000000))
print(newman_prime(100000000000000))
print(newman_prime(1000000000000000))
print(newman_prime(10000000000000000))
print(newman_prime(100000000000000000))
print(newman_prime(1000000000000000000))
print(newman_prime(10000000000000000000))
print(newman_prime(100000000000000000000))
print(newman_prime(1000000000000000000000))
print(newman_prime(10000000000000000000000))
print(newman_prime(100000000000000000000000))
print(newman_prime(1000000000000000000000000))
print(newman_prime(10000000000000000000000000))
print(newman_prime(100000000000000000000000000))
print(newman_prime(1000000000000000000000000000))
print(newman_prime(10000000000000000000000000000))
print(newman_prime(100000000000000000000000000000))
print(newman_prime(1000000000000000000000000000000))
print(newman_prime(100000000000000000