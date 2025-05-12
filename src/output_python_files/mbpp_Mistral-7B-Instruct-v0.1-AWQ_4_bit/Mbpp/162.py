"""
Write a function to calculate the sum (n - 2*i) from i=0 to n // 2, for instance n + (n-2) + (n-4)... (until n-x =< 0).
assert sum_series(6) == 12
"""

def sum_series(n):
    """
    Calculate the sum of the series (n - 2*i) from i=0 to n // 2
    """
    assert n % 2 == 0, "n must be even"
    return sum(range(n, 0, -2))


if __name__ == '__main__':
    print(sum_series(6))