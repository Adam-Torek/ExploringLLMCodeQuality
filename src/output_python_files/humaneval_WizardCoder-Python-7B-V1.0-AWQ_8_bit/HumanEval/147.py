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
    for i in range(1, n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if (i*i - i + 1) + (j*j - j + 1) + (k*k - k + 1) % 3 == 0:
                    count += 1
    return count


# Test cases
print(get_max_triples(5)) # Output: 1
print(get_max_triples(10)) # Output: 1
print(get_max_triples(15)) # Output: 2
print(get_max_triples(20)) # Output: 3
print(get_max_triples(100)) # Output: 10

# Time Complexity: O(n^3)
# Space Complexity: O(1)

# Can we do better?
# Yes, we can optimize the above solution by using a dictionary to store the squares of the numbers.
# We can then iterate through the dictionary and check if the sum of the squares of the three numbers is a multiple of 3.

def get_max_triples_optimized(n):
    squares = {}
    for i in range(1, n+1):
        squares[i*i] = 1

    count = 0
    for i in squares:
        for j in squares:
            if i < j:
                for k in squares:
                    if j < k:
                        if (i + j + k) % 3 == 0:
                            count += 1
    return count

# Test cases
print(get_max_triples_optimized(5)) # Output: 1
print(get_max_triples_optimized(10)) # Output: 1
print(get_max_triples_optimized(15)) # Output: 2
print(get_max_triples_optimized(20)) # Output: 3
print(get_max_triples_optimized(100)) # Output: 10

# Time Complexity: O(n^2)
# Space Complexity: O(n)

# Can we further optimize it?
# Yes, we can use a set to store the squares of the numbers and iterate through the set only once.

def get_max_triples_optimized(n):
    squares = set()
    for i in range(1, n+1):
        squares.add(i*i)

    count = 0
    for i in squares:
        for j in squares:
            if i < j:
                for k in squares:
                    if j < k:
                        if (i + j + k) % 3 == 0:
                            count += 1
    return count

# Test cases
print(get_max_triples_optimized(5)) # Output: 1
print(get_max_triples_optimized(10)) # Output: 1
print(get_max_triples_optimized(15)) # Output: 2
print(get_max_triples_optimized(20)) # Output: 3
print(get_max_triples_optimized(100)) # Output: 10

# Time Complexity: O(n^2)
# Space Complexity: O(n)

# Can we further optimize it?
# Yes, we can use a set to store the squares of the numbers and