"""
Write a python function to check whether the two numbers differ at one bit position only or not.
assert differ_At_One_Bit_Pos(13,9) == True
"""

def differ_At_One_Bit_Pos(num1, num2):
    if num1 == num2:
        return False
    else:
        for i in range(32):
            if (num1 >> i) & 1!= (num2 >> i) & 1:
                return True
        return False

# Test cases
print(differ_At_One_Bit_Pos(13,9)) # True
print(differ_At_One_Bit_Pos(12,13)) # False
print(differ_At_One_Bit_Pos(12,12)) # False<|endoftext|>