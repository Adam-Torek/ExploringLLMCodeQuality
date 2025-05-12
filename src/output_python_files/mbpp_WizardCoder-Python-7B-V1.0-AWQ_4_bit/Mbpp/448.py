"""
Write a function to calculate the sum of perrin numbers.
assert cal_sum(9) == 49
"""

def cal_sum(n):
    if n < 1:
        return 0
    elif n == 1:
        return 1
    else:
        return n + cal_sum(n-1)

def perrin_sum(n):
    return n * (n+1) / 2

def perrin_numbers_sum(n):
    return sum([perrin_sum(i) for i in range(1, n+1)])

def perrin_numbers_sum_recursive(n):
    return cal_sum(n) * n

print(perrin_numbers_sum(9))
print(perrin_numbers_sum_recursive(9))

# assert cal_sum(9) == 49
# assert perrin_numbers_sum(9) == 49
# assert perrin_numbers_sum_recursive(9) == 49

# print(perrin_numbers_sum(10))
# print(perrin_numbers_sum_recursive(10))

# print(perrin_numbers_sum(100))
# print(perrin_numbers_sum_recursive(100))

# print(perrin_numbers_sum(1000))
# print(perrin_numbers_sum_recursive(100))

# print(perrin_numbers_sum(10000))
# print(perrin_numbers_sum_recursive(10000))

# print(perrin_numbers_sum(100000))
# print(perrin_numbers_sum_recursive(100000))

# print(perrin_numbers_sum(1000000))
# print(perrin_numbers_sum_recursive(1000000))

# print(perrin_numbers_sum(10000000))
# print(perrin_numbers_sum_recursive(10000000))

# print(perrin_numbers_sum(100000000))
# print(perrin_numbers_sum_recursive(10000000))

# print(perrin_numbers_sum(1000000000))
# print(perrin_numbers_sum_recursive(100000000))

# print(perrin_numbers_sum(10000000000))
# print(perrin_numbers_sum_recursive(1000000000))

# print(perrin_numbers_sum(10000000000))
# print(perrin_numbers_sum_recursive(1000000000))

# print(perrin_numbers_sum(100000000000))
# print(perrin_numbers_sum_recursive(10000000000))

# print(perrin_numbers_sum(100000000000))
# print(perrin_numbers_sum_recursive(10000000000))

# print(perrin_numbers_sum(1000000000000))
# print(perrin_numbers_sum_recursive(100000000000))

# print(perrin_numbers_sum(1000000000000))
# print(perrin_numbers_sum_recursive(100000000000))

# print(perrin_numbers_sum(10000000000000))
# print(perrin_numbers_sum_recursive(1000000000000))

# print(perrin_numbers_sum(10000000000000))
# print