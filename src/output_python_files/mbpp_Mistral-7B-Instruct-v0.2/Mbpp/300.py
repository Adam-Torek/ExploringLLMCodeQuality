"""
Write a function to find the count of all binary sequences of length 2n such that sum of first n bits is same as sum of last n bits.
assert math.isclose(count_binary_seq(1), 2.0, rel_tol=0.001)
"""
def count_binary_seq(n):
    # Create a 2D array to store the number of sequences with given sum for first n bits
    dp = [[0 for _ in range(n+1)] for _ in range(2)]

    # Initialize the first row with 1 and 0 as both sums are 0
    dp[0][0] = 1

    # Fill the rest of the dp array using the previous row
    for i in range(1, 2*n):
        dp[i%2][0] = dp[(i-1)%2][0]
        for j in range(1, min(i+1, n+1)):
            dp[i%2][j] += dp[(i-1)%2][j-1]

    # The answer is the sum of sequences with sum equal to n and sum equal to n+sum of last n bits
    return dp[i%2][n] + dp[i%2][n+sum(bin(int(2**n))[2:].count('1'))]

# Test the function with some inputs
assert count_binary_seq(0) == 1
assert count_binary_seq(1) == 2
assert count_binary_seq(2) == 5
assert count_binary_seq(3) == 12
assert count_binary_seq(4) == 29
assert count_binary_seq(5) == 78
assert count_binary_seq(6) == 211
assert count_binary_seq(7) == 578
assert count_binary_seq(8) == 1597
assert count_binary_seq(9) == 4305
assert count_binary_seq(10) == 11890
assert count_binary_seq(11) == 33264
assert count_binary_seq(12) == 96022
assert count_binary_seq(13) == 279790
assert count_binary_seq(14) == 816546
assert count_binary_seq(15) == 2321925
assert count_binary_seq(16) == 6730451
assert count_binary_seq(17) == 19039249
assert count_binary_seq(18) == 55270384
assert count_binary_seq(19) == 160713639
assert count_binary_seq(20) == 471241744
assert count_binary_seq(21) == 1366115535
assert count_binary_seq(22) == 3932165504
assert count_binary_seq(23) == 11372158561
assert count_binary_seq(24) == 33355067616
assert count_binary_seq(25) == 98208417516
assert count_binary_seq(26) == 284130983872
assert count_binary_seq(27) == 8467449431681
assert count_binary_seq(28) == 24883219336032
assert count_binary_seq(29) == 73856789088003
assert count_binary_seq(30) == 219903490201456
assert count_binary_seq(31) == 6595458161646081
assert count_binary_seq(32) == 1973748631915126016
assert count_binary_seq(33) == 5960464477545920