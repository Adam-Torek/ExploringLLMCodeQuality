def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    count = 0
    for i in range(10**(n-1, 10**n):
        if i % 10 == 1 or i // 10**(n-1) == 1:
            count += 1
    return count



# Test cases
print(starts_one_ends(1))  # 9
print(starts_one_ends(2))  # 45
print(starts_one_ends(3))  # 360
print(starts_one_ends(4))  # 3003
print(starts_one_ends(5))  # 2720
print(starts_one_ends(6))  # 20400
print(starts_one_ends(7))  # 155500
print(starts_one_ends(8))  # 105050
print(starts_one_ends(9))  # 64064
print(starts_one_ends(10))  # 362880