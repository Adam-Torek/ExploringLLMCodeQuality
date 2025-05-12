def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # Your code here
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return int(str(10**n - 9*10**(n-1) + 10**(n-1))/10) + int(str(10**n - 1)/10)

# Test cases
print(starts_one_ends(0)) # 0
print(starts_one_ends(1)) # 1
print(starts_one_ends(2)) # 3
print(starts_one_ends(3)) # 6
print(starts_one_ends(4)) # 10
print(starts_one_ends(5)) # 15
print(starts_one_ends(6)) # 21
print(starts_one_ends(7)) # 28
print(starts_one_ends(8)) # 36
print(starts_one_ends(9)) # 45
print(starts_one_ends(10)) # 55
print(starts_one_ends(11)) # 66
print(starts_one_ends(12)) # 78
print(starts_one_ends(13)) # 91
print(starts_one_ends(14)) # 106
print(starts_one_ends(15)) # 122
print(starts_one_ends(16)) # 140
print(starts_one_ends(17)) # 160
print(starts_one_ends(18)) # 182
print(starts_one_ends(19)) # 206
print(starts_one_ends(20)) # 233
print(starts_one_ends(21)) # 263
print(starts_one_ends(22)) # 300
print(starts_one_ends(23)) # 341
print(starts_one_ends(24)) # 386
print(starts_one_ends(25)) # 436
print(starts_one_ends(26)) # 491
print(starts_one_ends(27)) # 551
print(starts_one_ends(28)) # 616
print(starts_one_ends(29)) # 686
print(starts_one_ends(30)) # 761
print(starts_one_ends(31)) # 841
print(starts_one_ends(32)) # 926
print(starts_one_ends(33)) # 1016
print(starts_one_ends(34)) # 1111
print(starts_one_ends(35)) # 1216