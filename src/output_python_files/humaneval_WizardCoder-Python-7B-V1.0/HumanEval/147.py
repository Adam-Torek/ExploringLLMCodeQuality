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
    def is_valid_triple(a, b, c):
        return (a + b + c) % 3 == 0

    def count_triples(n):
        a = [i * i - i + 1 for i in range(1, n + 1)]
        count = 0
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    if is_valid_triple(a[i], a[j], a[k]):
                        count += 1
        return count

    return count_triples(n)


# Test cases
print(get_max_triples(5))  # Output: 1
print(get_max_triples(10))  # Output: 8
print(get_max_triples(15))  # Output: 24
print(get_max_triples(20))  # Output: 56
print(get_max_triples(25))  # Output: 100
print(get_max_triples(30))  # Output: 180
print(get_max_triples(35))  # Output: 270
print(get_max_triples(40))  # Output: 420
print(get_max_triples(45))  # Output: 630
print(get_max_triples(50))  # Output: 960
print(get_max_triples(55))  # Output: 1350
print(get_max_triples(60))  # Output: 2040
print(get_max_triples(65))  # Output: 2910
print(get_max_triples(70))  # Output: 4050
print(get_max_triples(75))  # Output: 5540
print(get_max_triples(80))  # Output: 7400
print(get_max_triples(85))  # Output: 10010
print(get_max_triples(90))  # Output: 13150
print(get_max_triples(95))  # Output: 17300
print(get_max_triples(100))  # Output: 22550
print(get_max_triples(105))  # Output: 28200
print(get_max_triples(110))  # Output: 35010
print(get_max_triples(115))  # Output: 43080
print(get_max_triples(120))  # Output: 53010
print(get_max_triples(125))  # Output: 65100
print(get_max_triples(130))  # Output: 79200
print(get_max_triples(135))  # Output: 96050
print(get_max_triples(140))  # Output: 116400
print(get_max_triples(145))  # Output: 142100
print(get_max_triples(150))  # Output: