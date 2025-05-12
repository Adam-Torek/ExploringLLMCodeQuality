"""
Write a function to multiply all the numbers in a list and divide with the length of the list.
assert math.isclose(multiply_num((8, 2, 3, -1, 7)), -67.2, rel_tol=0.001)
"""
def multiply_num(list):
    return sum(list)/len(list)

"""
Write a function to calculate the sum of the digits in a number.
assert sum_digits(1234) == 10
assert sum_digits(5678) == 26
"""
def sum_digits(num):
    return sum([int(i) for i in str(num)])

"""
Write a function to calculate the factorial of a number.
assert factorial(5) == 120
"""
def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num-1)

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

"""
Write a function to check whether a number is perfect or not.
assert is_perfect(6) == True
assert is_perfect(28) == True
assert is_perfect(29) == False
"""
def is_perfect(num):
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i
    return sum == num

"""
Write a function to check whether a number is amstrong or not.
assert is_armstrong(153) == True
assert is_armstrong(123) == False
"""
def is_armstrong(num):
    sum = 0
    for i in str(num):
        sum += int(i) ** len(str(num))
    return sum == num

"""
Write a function to check whether a number is automorphic or not.
assert is_automorphic(5) == True
assert is_automorphic(10) == False
"""
def is_automorphic(num):
    return str(num ** 2).endswith(str(num))

"""
Write a function to check whether a number is a disarium or not.
assert is_disarium(89) == True
assert is_disarium(135) == True
assert is_disarium(125) == False
"""
def is_disarium(num):
    sum = 0
    for i in str(num):
        sum += int(i) ** len(str(num))
    return sum == num

"""
Write a function to check whether a number is happy or not.
assert is_happy(7) == True
assert is_happy(23) == True
assert is_happy(12) == False
"""
def is_happy(num):
    while num!= 1 and num!= 4:
        num = sum([int(i) ** 2 for i in str(num)])
    return num == 1

"""
Write a function to check whether a number is harshad or not.
assert is_harshad(171) == True
assert is_harshad(15) == False
"""
def is_harshad(num):
    return num % sum([int(i) for i in str(num)]) == 0

"""
Write a function to check whether a number is meander or not.
assert is_meander(5) == True
assert is_meander(10) == False
"""
def is_meander(num):
    return sum([int(i) for i in str(num)]) == sum([int(i) for i in str(num)[1:]])

"""
Write a function to check whether a number is narcissistic or not.
assert is_narcissistic(7) == True
assert is_narcissistic(371) == True
assert is_narcissistic(122) == False
"""
def is_narcissistic(num):
    return num == sum([int(i) ** len(str(num)) for i in str(num)])