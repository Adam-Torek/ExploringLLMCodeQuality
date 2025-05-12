"""
Write a function to return the sum of all divisors of a number.
assert sum_div(8)==7
"""
def sum_div(n):
    sum = 0
    i = 1
    while i <= n:
        if n % i == 0:
            sum += i
        i += 1
    return sum

assert sum_div(8) == 7
print(sum_div(8))