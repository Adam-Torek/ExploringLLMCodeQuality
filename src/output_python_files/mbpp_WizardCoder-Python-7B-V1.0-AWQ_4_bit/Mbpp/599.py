"""
Write a function to find sum and average of first n natural numbers.
assert sum_average(10)==(55, 5.5)
"""

def sum_average(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return (sum, sum/n)

print(sum_average(10))

# Output: (55, 5.5)

# Another way to solve the problem using list comprehension

def sum_average_list(n):
    nums = [i for i in range(1, n+1)]
    return (sum(nums), sum(nums)/n)

print(sum_average_list(10))

# Output: (55, 5.5)