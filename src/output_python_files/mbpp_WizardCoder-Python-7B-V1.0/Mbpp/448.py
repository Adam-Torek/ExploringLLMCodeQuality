"""
Write a function to calculate the sum of perrin numbers.
assert cal_sum(9) == 49
"""

def cal_sum(n):
    sum = 0
    for i in range(1, n+1):
        sum += i**2
    return sum

print(cal_sum(9))