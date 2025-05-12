"""
Write a python function to check whether the given number can be represented as sum of non-zero powers of 2 or not.
assert is_Sum_Of_Powers_Of_Two(10) == True
"""
def is_Sum_Of_Powers_Of_Two(n):
    if n < 0:
        return False
    elif n == 0:
        return True
    elif (n & (n - 1)) == 0:
        return True
    else:
        for i in range(32):
            if (1 << i) & n:
                if (n - (1 << i)) % (1 << i) == 0:
                    n -= 1 << i
                    return is_Sum_Of_Powers_Of_Two(n)
        return False

# Test cases
assert is_Sum_Of_Powers_Of_Two(10) == True
assert is_Sum_Of_Powers_Of_Two(5) == False
assert is_Sum_Of_Powers_Of_Two(0) == True
assert is_Sum_Of_Powers_Of_Two(1) == True
assert is_Sum_Of_Powers_Of_Two(2) == True
assert is_Sum_Of_Powers_Of_Two(3) == False
assert is_Sum_Of_Powers_Of_Two(4) == True
assert is_Sum_Of_Powers_Of_Two(16) == True
assert is_Sum_Of_Powers_Of_Two(25) == True
assert is_Sum_Of_Powers_Of_Two(26) == False
assert is_Sum_Of_Powers_Of_Two(128) == True
assert is_Sum_Of_Powers_Of_Two(256) == True
assert is_Sum_Of_Powers_Of_Two(512) == True
assert is_Sum_Of_Powers_Of_Two(1024) == True
assert is_Sum_Of_Powers_Of_Two(1025) == False
assert is_Sum_Of_Powers_Of_Two(16777216) == True
assert is_Sum_Of_Powers_Of_Two(16777217) == False
assert is_Sum_Of_Powers_Of_Two(1073741824) == True
assert is_Sum_Of_Powers_Of_Two(1073741825) == False
assert is_Sum_Of_Powers_Of_Two(1099511627776) == True
assert is_Sum_Of_Powers_Of_Two(1099511627777) == False
assert is_Sum_Of_Powers_Of_Two(1125899906842624) == True
assert is_Sum_Of_Powers_Of_Two(1125899906842625) == False
assert is_Sum_Of_Powers_Of_Two(123456789012345678901234567890) == True
assert is_Sum_Of_Powers_Of_Two(123456789012345678901234567891) == False
assert is_Sum_Of_Powers_Of_Two(123456789012345678901234567892**2) == True
assert is_Sum_Of_Powers_Of_Two(123456789012345678901234567893**3) == True
assert is_Sum_Of_Powers_Of_Two(12345678901234567890123456