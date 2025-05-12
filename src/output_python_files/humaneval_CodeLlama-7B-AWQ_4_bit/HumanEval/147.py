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
# 4

# Explanation:
# a = [1, 3, 7, 13, 21, 33, 41, 53, 67, 81]
# The valid triples are (1, 7, 13), (1, 7, 21), (1, 13, 21), (1, 33, 41).

# Sample Input:
# 100

# Sample Output:
# 100

# Explanation:
# a = [1, 3, 7, 13, 21, 33, 41, 53, 67, 81, 97, 113, 127, 141, 157, 173, 187, 203, 219, 235, 251, 267, 283, 299, 315, 331, 347, 363, 379, 395, 411, 427, 443, 459, 475, 491, 507, 523, 541, 557, 573, 589, 605, 621, 637, 653, 669, 685, 701, 717, 733, 749, 765, 781, 797, 813, 829, 845, 861, 877, 893, 909, 925, 941, 957, 973, 989, 1005, 1021, 1037, 1053, 1069, 1085, 1091, 1107, 1123, 1139, 1155, 1171, 1187, 1203, 1219, 1235, 1251, 1267, 1283, 1299, 1315, 1331, 1347,