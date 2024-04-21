"""
Write a python function that takes in an integer n and finds the sum of the first n even natural numbers that are raised to the fifth power.
assert even_Power_Sum(2) == 1056
"""
def even_Power_Sum(n):
    sum = 0
    i = 0
    while n > 0:
        sum += (i**5)
        i += 1
        n -= 1 if i % 2 != 0 else 0
    return sum

assert even_Power_Sum(2) == 1056</s>