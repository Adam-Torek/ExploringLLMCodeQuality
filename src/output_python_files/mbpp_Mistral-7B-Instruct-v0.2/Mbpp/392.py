"""
Write a function to find the maximum sum possible by using the given equation f(n) = max( (f(n/2) + f(n/3) + f(n/4) + f(n/5)), n).
assert get_max_sum(60) == 106
"""
def get_max_sum(n):
    memo = {}
    def f(n):
        if n in memo:
            return memo[n]
        if n == 0 or n == 1:
            memo[n] = 0
            return 0
        memo[n] = max(n, sum(f(int(n/i)) for i in [2, 3, 4, 5] if n % i))
        return memo[n]
    return f(n)

assert get_max_sum(60) == 106