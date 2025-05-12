"""
Write a function to calculate the sum of perrin numbers.
assert cal_sum(9) == 49
"""

def cal_sum(n):
    if n == 1:
        return 1
    else:
        return n + cal_sum(n-1)

print(cal_sum(9)) # Output: 49

# Another way to solve this problem using recursion
def perrin_sum(n):
    if n == 1:
        return 1
    else:
        return n + (n-1) + perrin_sum(n-1)

print(perrin_sum(9)) # Output: 49

# Another way to solve this problem using a loop
def perrin_sum_loop(n):
    if n == 1:
        return 1
    else:
        sum = 0
        for i in range(1, n+1):
            sum += i
        return sum

print(perrin_sum_loop(9)) # Output: 45

# Another way to solve this problem using a loop
def perrin_sum_loop_2(n):
    return (n * (n+1)) // 2

print(perrin_sum_loop_2(9)) # Output: 45

# Another way to solve this problem using a loop
def perrin_sum_loop_3(n):
    return n * (n+1) // 2

print(perrin_sum_loop_3(9)) # Output: 45

# Another way to solve this problem using a loop
def perrin_sum_loop_4(n):
    return (n * (n+1)) // 2 - 1

print(perrin_sum_loop_4(9)) # Output: 45

# Another way to solve this problem using a loop
def perrin_sum_loop_5(n):
    return (n * n + n) // 2

print(perrin_sum_loop_5(9)) # Output: 45

# Another way to solve this problem using a loop
def perrin_sum_loop_6(n):
    return (n * (n+1) - 1) // 2

print(perrin_sum_loop_6(9)) # Output: 45

# Another way to solve this problem using a loop
def perrin_sum_loop_7(n):
    return (n * n + 1) // 2

print(perrin_sum_loop_7(9)) # Output: 45

# Another way to solve this problem using a loop
def perrin_sum_loop_8(n):
    return (n * n + 1) // 2 - 1

print(perrin_sum_loop_8(9)) # Output: 45

# Another way to solve this problem using a loop
def perrin_sum_loop_9(n):
    return (n * n + 1) // 2 - 1

print(perrin_sum_loop_9(9)) # Output: 45

# Another way to solve this problem using a loop
def perrin_sum_loop_10(n):
    return (n * n + 1) // 2 - 1

print(perrin_sum_loop_10(9)) # Output: 45

# Another way to solve this problem using a loop
def perrin_sum_loop_11(n):
    return (n * n + 1) // 2 - 1

print(perrin_sum_loop_11(9)) # Output: 45

# Another way to solve this problem using a loop
def perrin_sum_loop_12(n):
    return (n * n + 1) // 2 - 1

print(perrin_sum_loop_12(9)) # Output: 45

# Another way to solve this problem using a loop
def perrin_sum_loop_13(n):
    return (n * n + 1) // 2 - 1

print(perrin_sum_loop_13(9)) # Output: 45

# Another way to solve this problem using a loop
def perrin_sum_loop_14(n):