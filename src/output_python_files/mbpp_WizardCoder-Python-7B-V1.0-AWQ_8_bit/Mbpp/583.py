"""
Write a function which returns nth catalan number.
assert catalan_number(10)==16796
"""

def catalan_number(n):
    def catalan(n):
        if n == 0:
            return 1
        else:
            return (2*n) * catalan(n-1) // (n+1)
    return catalan(n)

print(catalan_number(10))

# Another way to solve this problem using dynamic programming

def catalan_number_dp(n):
    if n == 0:
        return 1
    dp = [0] * (n+1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = (2*i) * dp[i-1] // (i+1)
    return dp[n]

print(catalan_number_dp(10))

# Another way to solve this problem using binomial coefficient

def catalan_number_binomial(n):
    return binomial(2*n, n) // (n+1)

def binomial(n, k):
    if k == 0 or k == n:
        return 1
    else:
        return factorial(n) // (factorial(k) * factorial(n-k))

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(catalan_number_binomial(10))

# Another way to solve this problem using matrix exponentiation

def matrix_exponentiation(n):
    MOD = 10**9 + 7
    def matrix_mul(a, b, n):
        result = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    result[i][j] = (a[i][k] * b[k][j]) % MOD
        return result

    def matrix_pow(a, n):
        if n == 1:
            return a
        if n % 2 == 0:
            half_pow = matrix_pow(a, n//2)
            return matrix_mul(half_pow, half_pow, n)
        else:
            return matrix_mul(matrix_pow(a, n//2), matrix_mul(a, half_pow, n), n)

    def catalan(n):
        if n == 0:
            return 1
        else:
            return (2*n) * catalan(n-1) // (n+1)

    def build_matrix(n):
        a = [[1, 1], [1, 0]]
        return matrix_pow(a, n-1)

    return catalan(n)

print(matrix_exponentiation(10))

# Another way to solve this problem using pascal's triangle

def pascal_triangle(n):
    def pascal(n):
        if n == 0:
            return [1]
        elif n == 1:
            return [1, 1]
        else:
            line = [1]
            for i in range(1, n):
                line_new = [1]
                for j in range(1, i):
                    line_new.append(line[j-1] + line[j])
                line_new.append(1)
                line = line_new
            return line

    def catalan(n):
        return pascal(n)[n] // (n+1)

    return catalan(n)

print(pascal_triangle(10))

# Another way to solve this problem using binomial coefficient using pascal's triangle

def binomial(n, k):
    if k == 0 or k == n:
        return 1
    else:
        return factorial(n) // (factorial(k) * factorial(n-k))

def factorial(n):
    if n == 0:
        return 1
    else:
        return n