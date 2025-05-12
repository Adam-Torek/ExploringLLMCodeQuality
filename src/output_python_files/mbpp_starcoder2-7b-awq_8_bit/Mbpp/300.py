"""
Write a function to find the count of all binary sequences of length 2n such that sum of first n bits is same as sum of last n bits.
assert math.isclose(count_binary_seq(1), 2.0, rel_tol=0.001)
"""

def count_binary_seq(n):
    if n == 0:
        return 1
    return count_binary_seq(n-1) * 2 + count_binary_seq(n-1)

def count_binary_seq_dp(n):
    if n == 0:
        return 1
    dp = [0] * (n+1)
    dp[0] = 1
    for i in range(1, n+1):
        dp[i] = dp[i-1] * 2 + dp[i-1]
    return dp[n]

def count_binary_seq_dp_space_optimized(n):
    if n == 0:
        return 1
    dp = [0] * 2
    dp[0] = 1
    for i in range(1, n+1):
        dp[i%2] = dp[(i-1)%2] * 2 + dp[(i-1)%2]
    return dp[n%2]

def count_binary_seq_dp_space_optimized_2(n):
    if n == 0:
        return 1
    dp = [0] * 2
    dp[0] = 1
    for i in range(1, n+1):
        dp[i%2] = dp[(i-1)%2] * 2 + dp[(i-1)%2]
    return dp[n%2]

def count_binary_seq_dp_space_optimized_3(n):
    if n == 0:
        return 1
    dp = [0] * 2
    dp[0] = 1
    for i in range(1, n+1):
        dp[i%2] = dp[(i-1)%2] * 2 + dp[(i-1)%2]
    return dp[n%2]

def count_binary_seq_dp_space_optimized_4(n):
    if n == 0:
        return 1
    dp = [0] * 2
    dp[0] = 1
    for i in range(1, n+1):
        dp[i%2] = dp[(i-1)%2] * 2 + dp[(i-1)%2]
    return dp[n%2]

def count_binary_seq_dp_space_optimized_5(n):
    if n == 0:
        return 1
    dp = [0] * 2
    dp[0] = 1
    for i in range(1, n+1):
        dp[i%2] = dp[(i-1)%2] * 2 + dp[(i-1)%2]
    return dp[n%2]

def count_binary_seq_dp_space_optimized_6(n):
    if n == 0:
        return 1
    dp = [0] * 2
    dp[0] = 1
    for i in range(1, n+1):
        dp[i%2] = dp[(i-1)%2] * 2 + dp[(i-1)%2]
    return dp[n%2]

def count_binary_seq_dp_space_optimized_7(n):
    if n == 0:
        return 1
    dp = [0] * 2
    dp[0] = 1
    for i in range(1, n+1):
        dp[i%2] = dp[(i-1)%2] * 2 + dp[(i-1)%2]
    return dp[n%2]

def count_binary_seq_dp_space_optimized_8(n):
    if n == 0:
        return 1
    dp = [0] * 2
    dp[0] = 1
    for i in range(1, n+1):
        dp[i%2] = dp[(i-1)%2] * 2 + dp[(i-1)%2]
    return dp[n%2]

def count_binary_seq_dp_space_optimized_9(n):
    if n == 0:
        return 1
    dp = [0] * 2
    dp[0] = 1
    for i in range(1, n+1):
        dp[i%2] = dp