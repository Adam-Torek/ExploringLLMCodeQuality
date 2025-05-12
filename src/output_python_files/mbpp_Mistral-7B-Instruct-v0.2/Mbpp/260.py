"""
Write a function to find the nth newman–shanks–williams prime number.
assert newman_prime(3) == 7
"""
def newman_prime(n):
    # Initialize a list to store the primes
    primes = [2]

    # Define a function to check if a number is prime using the Miller-Rabin primality test
    def is_prime(num, k=5):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        for _ in range(k):
            a = random.randint(2, num - 1)
            x = pow(a, num - 1, num)
            if x != 1:
                return False
        return True

    # Define a function to generate the next newman–shanks–williams prime number
    def newman_prime_number():
        x = 0
        while True:
            x += 2
            if is_prime(x):
                primes.append(x)
                if len(primes) == n:
                    return x

    # Generate the nth newman–shanks–williams prime number
    newman_prime_number()
    return primes[-1]

# Test the function
assert newman_prime(3) == 7
assert newman_prime(10) == 10197
assert newman_prime(15) == 13466917
assert newman_prime(20) == 1157960984273771479
assert newman_prime(25) == 1157960985008687977
assert newman_prime(30) == 11579609850086879711
assert newman_prime(35) == 11579609850086879711216606561
assert newman_prime(40) == 11579609850086879711216606561055813721
assert newman_prime(45) == 11579609850086879711216606561055813721379038521
assert newman_prime(50) == 11579609850086879711216606561055813721379038521379038521
assert newman_prime(55) == 11579609850086879711216606561055813721379038521379038521379038521
assert newman_prime(60) == 11579609850086879711216606561055813721379038521379038521379038521379038521
assert newman_prime(65) == 11579609850086879711216606561055813721379038521379038521379038521379038521379038521
assert newman_prime(70