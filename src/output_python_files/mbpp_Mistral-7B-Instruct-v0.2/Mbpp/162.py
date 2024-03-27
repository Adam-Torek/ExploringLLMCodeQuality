"""
Write a function to calculate the sum (n - 2*i) from i=0 to n // 2, for instance n + (n-2) + (n-4)... (until n-x =< 0).
assert sum_series(6) == 12
"""
def sum_series(n):
    """
    Calculate the sum of the series (n - 2*i) from i=0 to n // 2
    """
    sum = 0
    for i in range(n // 2 + 1):
        sum += (n - 2 * i)
    return sum

assert sum_series(6) == 12
print(sum_series(10))</s>