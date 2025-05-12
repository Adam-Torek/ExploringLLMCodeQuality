"""
Write a function to find the count of all binary sequences of length 2n such that sum of first n bits is same as sum of last n bits.
assert math.isclose(count_binary_seq(1), 2.0, rel_tol=0.001)
"""
def count_binary_seq(n):
    # Create a 2D array to store the count of binary sequences with given sum for first n bits
    dp = [[0 for _ in range(n+1)] for _ in range(2)]
    dp[0][0] = 1

    # Fill the dp array using the recurrence relation
    for i in range(1, 2*n):
        dp[i%2][0] = dp[(i-1)%2][0] + dp[(i-1)%2][i&1]
        for j in range(1, min(n, i//2)+1):
            dp[i%2][j] += dp[(i-1)%2][j-1]
            dp[i%2][j] += dp[(i-1)%2][j] if i&(2*j) else 0

    # The answer is the sum of the counts of binary sequences with sum equal to n
    return sum(dp[n%2][j] for j in range(n+1))

assert math.isclose(count_binary_seq(1), 2.0, rel_tol=0.001)
assert math.isclose(count_binary_seq(2), 14.0, rel_tol=0.001)
assert math.isclose(count_binary_seq(3), 132.0, rel_tol=0.001)
assert math.isclose(count_binary_seq(4), 2035.0, rel_tol=0.001)
assert math.isclose(count_binary_seq(5), 46132.0, rel_tol=0.001)
assert math.isclose(count_binary_seq(6), 1331910.0, rel_tol=0.001)
assert math.isclose(count_binary_seq(7), 42228828.0, rel_tol=0.001)
assert math.isclose(count_binary_seq(8), 1544352240.0, rel_tol=0.001)
assert math.isclose(count_binary_seq(9), 63235649280.0, rel_tol=0.001)
assert math.isclose(count_binary_seq(10), 2723525222880.0, rel_tol=0.001)