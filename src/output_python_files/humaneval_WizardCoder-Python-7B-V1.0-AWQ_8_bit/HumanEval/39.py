def prime_fib(n: int):
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    >>> prime_fib(1)
    2
    >>> prime_fib(2)
    3
    >>> prime_fib(3)
    5
    >>> prime_fib(4)
    13
    >>> prime_fib(5)
    89
    """
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    a, b = 0, 1
    count = 0
    while True:
        a, b = b, a + b
        if is_prime(b):
            count += 1
            if count == n:
                return b

def main():
    n = int(input("Enter the nth Fibonacci number to find: "))
    print(f"The {n}th prime Fibonacci number is: {prime_fib(n)}")

if __name__ == "__main__":
    main()