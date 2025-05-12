"""
Write a function to find the surface area of a sphere.
assert math.isclose(surfacearea_sphere(10), 1256.6370614359173, rel_tol=0.001)
"""

def surfacearea_sphere(radius):
    return 4 * math.pi * radius ** 2

def main():
    print(surfacearea_sphere(10))

if __name__ == "__main__":
    main()
/python/math/math_factorial.py
"""
Write a function to find the factorial of a number.
assert math.isclose(factorial(5), 120, rel_tol=0.001)
"""

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def main():
    print(factorial(5))

if __name__ == "__main__":
    main()
/python/math/math_fibonacci.py
"""
Write a function to find the nth number in the Fibonacci sequence.
assert math.isclose(fibonacci(10), 55, rel_tol=0.001)
"""

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def main():
    print(fibonacci(10))

if __name__ == "__main__":
    main()
/python/math/math_prime.py
"""
Write a function to determine if a number is prime.
assert prime(11)
assert not prime(12)
"""

def prime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def main():
    print(prime(11))
    print(prime(12))

if __name__ == "__main__":
    main()
/python/math/math_gcd.py
"""
Write a function to find the greatest common divisor of two numbers.
assert math.isclose(gcd(12, 18), 6, rel_tol=0.001)
"""

def gcd(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        return gcd(b, a % b)

def main():
    print(gcd(12, 18))

if __name__ == "__main__":
    main()
/python/math/math_lcm.py
"""
Write a function to find the least common multiple of two numbers.
assert math.isclose(lcm(12, 18), 36, rel_tol=0.001)
"""

def lcm(a, b):
    if a == 0 or b == 0:
        return 0
    else:
        return abs(a * b) // gcd(a, b)

def main():
    print(lcm(12, 18))

if __name__ == "__main__":
    main()
/python/math/math_is_prime.py
"""
Write a function to determine if a number is prime.
assert is_prime(11)
assert not is_prime(12)
"""

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def main():
    print(is_prime(11))
    print(is_prime(12))

if __name__ == "__main__":
    main()
/python/math/math_is_palindrome.py
"""
Write a function to determine if a number is a palindrome.
assert is_palindrome(121)
assert not is_palindrome(123)
"""

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def main():
    print(is_palindrome(121))
    print(is_palindrome(123))

if __name__ == "__main__":
    main()
/python/math/math_is_perfect.py