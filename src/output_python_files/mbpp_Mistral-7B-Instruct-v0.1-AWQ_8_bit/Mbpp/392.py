"""
Write a function to find the maximum sum possible by using the given equation f(n) = max( (f(n/2) + f(n/3) + f(n/4) + f(n/5)), n).
assert get_max_sum(60) == 106
"""

def get_max_sum(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return max(get_max_sum(n//2) + get_max_sum(n//3) + get_max_sum(n//4) + get_max_sum(n//5), n)