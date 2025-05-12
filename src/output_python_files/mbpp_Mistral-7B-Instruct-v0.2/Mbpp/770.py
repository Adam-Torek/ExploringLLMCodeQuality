"""
Write a python function to find the sum of fourth power of first n odd natural numbers.
assert odd_num_sum(2) == 82
"""
def odd_num_sum(n):
    sum = 0
    i = 1
    while n > 0:
        sum += (i**4)
        i += 2
        n -= 1
    return sum

assert odd_num_sum(2) == 82