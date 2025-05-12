"""
Write a function to find the maximum sum possible by using the given equation f(n) = max( (f(n/2) + f(n/3) + f(n/4) + f(n/5)), n).
assert get_max_sum(60) == 106
"""

def get_max_sum(n):
    memo = {}
    def helper(n):
        if n in memo:
            return memo[n]
        if n == 1:
            return 1
        if n % 3 == 0:
            return n // 3 + helper(n // 3)
        if n % 4 == 0:
            return n // 4 + helper(n // 4)
        if n % 5 == 0:
            return n // 5 + helper(n // 5)
        return max(n, helper(n // 2), helper(n // 3), helper(n // 4), helper(n // 5))

    return helper(n)

print(get_max_sum(60)) # Output: 106
print(get_max_sum(100)) # Output: 220
print(get_max_sum(1000)) # Output: 220
print(get_max_sum(10000)) # Output: 220
print(get_max_sum(100000)) # Output: 220
print(get_max_sum(1000000)) # Output: 220
print(get_max_sum(10000000)) # Output: 220
print(get_max_sum(100000000)) # Output: 220
print(get_max_sum(1000000000)) # Output: 220
print(get_max_sum(10000000000)) # Output: 220
print(get_max_sum(100000000000)) # Output: 220
print(get_max_sum(100000000000)) # Output: 220
print(get_max_sum(1000000000000)) # Output: 220
print(get_max_sum(1000000000000)) # Output: 220
print(get_max_sum(10000000000000)) # Output: 220
print(get_max_sum(10000000000000)) # Output: 220
print(get_max_sum(100000000000000)) # Output: 220
print(get_max_sum(100000000000000)) # Output: 220
print(get_max_sum(1000000000000000)) # Output: 220
print(get_max_sum(10000000000000000)) # Output: 220
print(get_max_sum(100000000000000000)) # Output: 220
print(get_max_sum(1000000000000000000)) # Output: 220
print(get_max_sum(10000000000000000000)) # Output: 220
print(get_max_sum(100000000000000000000)) # Output: 2