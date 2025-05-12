"""
Write a function to multiply all the numbers in a list and divide with the length of the list.
assert math.isclose(multiply_num((8, 2, 3, -1, 7)), -67.2, rel_tol=0.001)
"""

def multiply_num(list):
    return sum(list)/len(list)

print(multiply_num((8, 2, 3, -1, 7)))

"""
Write a function to calculate the sum of the digits of a number.
assert sum_digits(1234) == 10
assert sum_digits(9999) == 36
"""

def sum_digits(num):
    return sum([int(i) for i in str(num)])

print(sum_digits(1234))
print(sum_digits(9999))

"""
Write a function to calculate the factorial of a number.
assert factorial(5) == 120
assert factorial(3) == 6
"""

def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num-1)

print(factorial(5))
print(factorial(3))

"""
Write a function to check whether a number is prime or not.
assert is_prime(7) == True
assert is_prime(4) == False
"""

def is_prime(num):
    if num == 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

print(is_prime(7))
print(is_prime(4))

"""
Write a function to check whether a number is perfect or not.
assert is_perfect(6) == True
assert is_perfect(28) == True
assert is_perfect(29) == False
"""

def is_perfect(num):
    if num == 1:
        return False
    else:
        sum = 0
        for i in range(1, num):
            if num % i == 0:
                sum += i
        if sum == num:
            return True
        else:
            return False

print(is_perfect(6))
print(is_perfect(28))
print(is_perfect(29))

"""
Write a function to check whether a number is amstrong or not.
assert is_armstrong(153) == True
assert is_armstrong(123) == False
"""

def is_armstrong(num):
    sum = 0
    for i in str(num):
        sum += int(i) ** len(str(num))
    if sum == num:
        return True
    else:
        return False

print(is_armstrong(153))
print(is_armstrong(123))

"""
Write a function to check whether a number is a fibonacci number or not.
assert is_fibonacci(144) == True
assert is_fibonacci(100) == False
"""

def is_fibonacci(num):
    if num == 0:
        return False
    elif num == 1:
        return True
    else:
        a = 0
        b = 1
        while b < num:
            a, b = b, a+b
            if b == num:
                return True
        return False

print(is_fibonacci(144))
print(is_fibonacci(100))

"""
Write a function to check whether a number is a palindrome or not.
assert is_palindrome(121) == True
assert is_palindrome(123) == False
"""

def is_palindrome(num):
    if str(num) == str(num)[::-1]:
        return True
    else:
        return False

print(is_palindrome(121))
print(is_palindrome(123))

"""
Write a function to check whether a number is a perfect square or not.
assert is_perfect_square(16) == True
assert is_perfect_square(15) == False
"""

def is_perfect_square(num):
    if num == 1:
        return True
    else:
        for i in range(1, num):
            if i * i == num:
                return True
        return False