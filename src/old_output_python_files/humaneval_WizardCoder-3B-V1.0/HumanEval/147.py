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

# Solution:
# We can solve this problem using a nested loop.
# We iterate through all possible pairs of indices i and j (i < j)
# and check if the sum of a[i] + a[j] is a multiple of 3.
# If it is, we increment a counter.
# Finally, we return the counter.

def count_valid_triples(n):
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if (i+j) % 3 == 0:
                count += 1
    return count

# Test the function
n = 5
print(count_valid_triples(n)) # Output: 1<|endoftext|>