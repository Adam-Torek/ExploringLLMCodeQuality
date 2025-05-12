"""
Write a python function to find the last digit in factorial of a given number.
assert last_Digit_Factorial(4) == 4
"""

def last_Digit_Factorial(n):
    if n == 0:
        return 1
    else:
        fact = 1
        for i in range(1, n+1):
            fact *= i
        return fact % 10

print(last_Digit_Factorial(4))
print(last_Digit_Factorial(10))
print(last_Digit_Factorial(100))
print(last_Digit_Factorial(1000))
print(last_Digit_Factorial(10000))
print(last_Digit_Factorial(100000))
print(last_Digit_Factorial(1000000))
print(last_Digit_Factorial(10000000))
print(last_Digit_Factorial(100000000))
print(last_Digit_Factorial(1000000000))
print(last_Digit_Factorial(10000000000))
print(last_Digit_Factorial(100000000000))
print(last_Digit_Factorial(100000000000))
print(last_Digit_Factorial(1000000000000))
print(last_Digit_Factorial(1000000000000))
print(last_Digit_Factorial(10000000000000))
print(last_Digit_Factorial(10000000000000))
print(last_Digit_Factorial(100000000000000))
print(last_Digit_Factorial(100000000000000))
print(last_Digit_Factorial(1000000000000000))
print(last_Digit_Factorial(1000000000000000))
print(last_Digit_Factorial(10000000000000000))
print(last_Digit_Factorial(100000000000000000))
print(last_Digit_Factorial(1000000000000000000))
print(last_Digit_Factorial(10000000000000000000))
print(last_Digit_Factorial(100000000000000000000))
print(last_Digit_Factorial(1000000000000000000000))
print(last_Digit_Factorial(10000000000000000000000))
print(last_Digit_Factorial(100000000000000000000000))
print(last_Digit_Factorial(100000000000000000