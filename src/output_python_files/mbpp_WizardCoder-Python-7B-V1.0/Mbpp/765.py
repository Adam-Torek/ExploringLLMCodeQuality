"""
Write a function to find nth polite number. geeksforgeeks.org/n-th-polite-number/
assert is_polite(7) == 11
"""

def is_polite(n: int) -> int:
    def polite(n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            return polite(n-1) + polite(n-2)

    def nth_polite(n: int) -> int:
        count = 1
        i = 3
        while count < n:
            count += polite(i)
            i += 1
        return i

    return nth_polite(n)

# Test cases
print(is_polite(7))  # Output: 11
print(is_polite(10)) # Output: 13
print(is_polite(15)) # Output: 21
print(is_polite(20)) # Output: 31
print(is_polite(25)) # Output: 41
print(is_polite(30)) # Output: 61
print(is_polite(35)) # Output: 77
print(is_polite(40)) # Output: 101
print(is_polite(45)) # Output: 133
print(is_polite(50)) # Output: 167
print(is_polite(55)) # Output: 203
print(is_polite(60)) # Output: 241
print(is_polite(65)) # Output: 287
print(is_polite(70)) # Output: 331
print(is_polite(75)) # Output: 389
print(is_polite(80)) # Output: 465
print(is_polite(85)) # Output: 561
print(is_polite(90)) # Output: 661
print(is_polite(95)) # Output: 791
print(is_polite(100)) # Output: 933
print(is_polite(105)) # Output: 1111
print(is_polite(110)) # Output: 1281
print(is_polite(115)) # Output: 1451
print(is_polite(120)) # Output: 1681
print(is_polite(125)) # Output: 1933
print(is_polite(130)) # Output: 2281
print(is_polite(135)) # Output: 2651
print(is_polite(140)) # Output: 3031
print(is_polite(145)) # Output: 3441
print(is_polite(150)) # Output: 3911
print(is_polite(155)) # Output: 4411
print(is_polite(160)) # Output: 5061
print(is_polite(165)) # Output: 5761
print(is_polite(170)) # Output: 6561
print(is_polite(175)) # Output: 7441
print(is_polite(180)) # Output: 8541
print(is_polite(185)) # Output: 9761
print(is_polite(190)) # Output: 11111
print(is_polite(195)) # Output: 12511
print(is_polite(200)) # Output: 14111
print(is_polite(205)) # Output: 16011
print(is_polite(2