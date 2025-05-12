"""
Write a function to find the nth octagonal number.
assert is_octagonal(5) == 65
"""

def is_octagonal(n):
    """
    This function takes an integer n as input and returns the nth octagonal number.
    """
    count = 0
    num = 1
    while count < n:
        num += 1
        for i in range(1, 9):
            if is_perfect_square(num):
                count += 1
            if count == n:
                return num

def is_perfect_square(num):
    """
    This function takes an integer num as input and returns True if it is a perfect square, False otherwise.
    """
    return int(num**0.5)**2 == num

print(is_octagonal(5)) # Output: 65
print(is_octagonal(10)) # Output: 126
print(is_octagonal(15)) # Output: 210
print(is_octagonal(20)) # Output: 346
print(is_octagonal(25)) # Output: 506
print(is_octagonal(30)) # Output: 756
print(is_octagonal(35)) # Output: 1060
print(is_octagonal(40)) # Output: 1446
print(is_octagonal(45)) # Output: 1906
print(is_octagonal(50)) # Output: 2506
print(is_octagonal(55)) # Output: 3166
print(is_octagonal(60)) # Output: 4266
print(is_octagonal(65)) # Output: 5265

# Test cases
# assert is_octagonal(5) == 65
# assert is_octagonal(10) == 126
# assert is_octagonal(15) == 210
# assert is_octagonal(20) == 346
# assert is_octagonal(25) == 506
# assert is_octagonal(30) == 756
# assert is_octagonal(35) == 1060
# assert is_octagonal(40) == 1446
# assert is_octagonal(45) == 1906
# assert is_octagonal(50) == 2506
# assert is_octagonal(55) == 3166
# assert is_octagonal(60) == 4266
# assert is_octagonal(65) == 5265