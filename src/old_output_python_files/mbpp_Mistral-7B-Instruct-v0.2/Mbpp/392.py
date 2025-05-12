"""
Write a function to find the maximum sum possible by using the given equation f(n) = max( (f(n/2) + f(n/3) + f(n/4) + f(n/5)), n).
assert get_max_sum(60) == 106
"""
def get_max_sum(n):
    memo = {}
    def f(n):
        if n in memo:
            return memo[n]
        if n == 0:
            return 0
        if n <= 3:
            return n
        memo[n] = max(n, f(n//2) + f(n//3) + f(n//4) + f(n//5))
        return memo[n]
    return f(n)

assert get_max_sum(60) == 106