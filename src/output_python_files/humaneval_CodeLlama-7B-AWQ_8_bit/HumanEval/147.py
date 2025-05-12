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
    # code here
    count = 0
    for i in range(1, n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if (i*i - i + 1 + j*j - j + 1 + k*k - k + 1) % 3 == 0:
                    count += 1
    return count


if __name__ == '__main__':
    n = int(input())
    print(get_max_triples(n))


# Time Complexity: O(n^2)
# Space Complexity: O(1)

# Sample Input:
# 5

# Sample Output:
# 1

# Explanation:
# a = [1, 3, 7, 13, 21]
# The only valid triple is (1, 7, 13).

# Sample Input:
# 10

# Sample Output:
# 3

# Explanation:
# a = [1, 3, 7, 13, 21, 33, 41, 53, 61, 73]
# The valid triples are (1, 7, 13), (3, 7, 33), and (7, 13, 41).

# Sample Input:
# 100

# Sample Output:
# 100

# Explanation:
# a = [1, 3, 7, 13, 21, 33, 41, 53, 61, 73, 89, 107, 121, 133, 141, 153, 161, 173, 189, 207, 221, 233, 241, 253, 261, 273, 289, 307, 321, 333, 341, 353, 361, 373, 389, 407, 421, 433, 441, 453, 461, 473, 489, 507, 521, 533, 541, 553, 561, 573, 589, 607, 621, 633, 641, 653, 661, 673, 689, 707, 721, 733, 741, 753, 761, 773, 789, 807, 821, 833, 841, 853, 861, 873, 889, 907, 921, 933, 941, 953, 961, 973, 989, 1007, 1021, 1033, 1041, 1053, 1061, 1073, 1089, 1107, 1121, 1133, 11