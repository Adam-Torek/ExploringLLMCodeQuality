"""
Write a function to check if the given integer is a prime number.
assert prime_num(13)==True
"""

def prime_num(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

print(prime_num(13))<|endoftext|>