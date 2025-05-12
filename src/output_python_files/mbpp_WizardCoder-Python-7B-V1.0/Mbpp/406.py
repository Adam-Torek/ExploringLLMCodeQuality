"""
Write a python function to find whether the parity of a given number is odd.
assert find_Parity(12) == False
"""
def find_Parity(num):
    if num % 2 == 0:
        return False
    else:
        return True

print(find_Parity(12)) # False
print(find_Parity(11)) # True
print(find_Parity(0)) # False
print(find_Parity(1)) # True
print(find_Parity(2)) # False
print(find_Parity(3)) # True
print(find_Parity(4)) # False
print(find_Parity(5)) # True
print(find_Parity(6)) # False
print(find_Parity(7)) # True
print(find_Parity(8)) # False
print(find_Parity(9)) # True
print(find_Parity(10)) # False

# Test cases
# assert find_Parity(12) == False
# assert find_Parity(11) == True
# assert find_Parity(0) == False
# assert find_Parity(1) == True
# assert find_Parity(2) == False
# assert find_Parity(3) == True
# assert find_Parity(4) == False
# assert find_Parity(5) == True
# assert find_Parity(6) == False
# assert find_Parity(7) == True
# assert find_Parity(8) == False
# assert find_Parity(9) == True
# assert find_Parity(10) == False