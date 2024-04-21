"""
Write a function to calculate the sum of perrin numbers.
assert cal_sum(9) == 49
"""
def cal_sum(n):
    sum = 0
    for i in range(1, n+1):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum

assert cal_sum(9) == 49</s>