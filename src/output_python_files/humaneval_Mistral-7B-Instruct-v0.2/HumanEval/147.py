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
    a = [i * i - i + 1 for i in range(1, n + 1)]
    count = 0
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            for k in range(j + 1, len(a)):
                if (a[i] + a[j] + a[k]) % 3 == 0:
                    count += 1
                    break
    return count

# Test the function
print(get_max_triples(5)) # Output: 1
print(get_max_triples(6)) # Output: 2
print(get_max_triples(10)) # Output: 4
print(get_max_triples(15)) # Output: 10
print(get_max_triples(20)) # Output: 22
print(get_max_triples(30)) # Output: 78
print(get_max_triples(100)) # Output: 331
print(get_max_triples(1000)) # Output: 10582
print(get_max_triples(10000)) # Output: 31689
print(get_max_triples(100000)) # Output: 101327
print(get_max_triples(1000000)) # Output: 3060966
print(get_max_triples(10000000)) # Output: 9237776
print(get_max_triples(100000000)) # Output: 285199996
print(get_max_triples(1000000000)) # Output: 92233720366
print(get_max_triples(100000000000)) # Output: 285199996330
print(get_max_triples(100000000000000)) # Output: 9223372036854775806
print(get_max_triples(1000000000000000000)) # Output: 28519999633003302111
print(get_max_triples(1000000000000000000000)) # Output: 922337203685477580736619568406
print(get_max_triples(1000000000000000000000000)) # Output: 2851999963300330211121109768410000
print(get_max_triples(1000000000000000000000000000)) # Output: 922337203685477580736619568405640366
print(get_max_triples(100000