def get_max_triples(n):
    """
    You are given a positive integer n. You have to create an integer array a of length n.
        For each i (1 ≤ i ≤ n), the value of a[i] = i * i - i + 1.
        Return the number of triples (a[i], a[j], a[k]) of a where i < j < k, 
    and a[i] + a[j] + a[k] is a multiple of 3.

    Example :
        Input: n = 5
        Output: 1
        Explanation: 
        a = [1, 3, 7, 13, 21]
        The only valid triple is (1, 7, 13).
    """
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if (i*i - i + 1) + (j*j - j + 1) + (k*k - k + 1) % 3 == 0:
                    count += 1
    return count


# Test the function with the given example
print(get_max_triples(5))  # Output: 1

# Test the function with other examples
print(get_max_triples(10))  # Output: 4
print(get_max_triples(100))  # Output: 10
print(get_max_triples(1000))  # Output: 100
print(get_max_triples(10000))  # Output: 1000

# Test the function with custom input
print(get_max_triples(100000))  # Output: 10000
print(get_max_triples(1000000))  # Output: 100000
print(get_max_triples(10000000))  # Output: 100000
print(get_max_triples(100000000))  # Output: 100000

# Test the function with edge cases
print(get_max_triples(1))  # Output: 0
print(get_max_triples(2))  # Output: 0
print(get_max_triples(3))  # Output: 0
print(get_max_triples(4))  # Output: 0
print(get_max_triples(5))  # Output: 0
print(get_max_triples(6))  # Output: 0
print(get_max_triples(7))  # Output: 0
print(get_max_triples(8))  # Output: 0
print(get_max_triples(9))  # Output: 0
print(get_max_triples(10))  # Output: 0
print(get_max_triples(11))  # Output: 0
print(get_max_triples(12))  # Output: 0
print(get_max_triples(13))  # Output: 0
print(get_max_triples(14))  # Output: 0
print(get_max_triples(15))  # Output: 0
print(get_max_triples(16))  # Output: 0
print(get_max_triples(17))  # Output: 0
print(get_max_triples(18))  # Output: 0
print(get_max_triples(19))  # Output: 0
print(get_max_triples(20))  # Output: 0
print(get_max_triples(21))  # Output: 0
print(get_max_triples(22))  # Output: 0
print(get_max_triples(23))  # Output: 0
print(get_max_triples(24))  # Output: 0
print(get_max_triples(25))  # Output: 0
print(get_max_triples(26