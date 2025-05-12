"""
Write a python function to check whether the two numbers differ at one bit position only or not.
assert differ_At_One_Bit_Pos(13,9) == True
"""

def differ_At_One_Bit_Pos(num1, num2):
    bin1 = bin(num1)[2:]
    bin2 = bin(num2)[2:]
    if len(bin1) != len(bin2):
        return False
    count = 0
    for i in range(len(bin1)):
        if bin1[i] != bin2[i]:
            count += 1
        if count > 1:
            return False
    return True

print(differ_At_One_Bit_Pos(13,9)) # True
print(differ_At_One_Bit_Pos(15,9)) # False
print(differ_At_One_Bit_Pos(13,17)) # True
print(differ_At_One_Bit_Pos(13,16)) # False
print(differ_At_One_Bit_Pos(13,15)) # False
print(differ_At_One_Bit_Pos(13,14)) # True
print(differ_At_One_Bit_Pos(13,16)) # False
print(differ_At_One_Bit_Pos(13,15)) # False
print(differ_At_One_Bit_Pos(13,14)) # True
print(differ_At_One_Bit_Pos(13,17)) # True
print(differ_At_One_Bit_Pos(13,18)) # False
print(differ_At_One_Bit_Pos(13,19)) # False
print(differ_At_One_Bit_Pos(13,20)) # False
print(differ_At_One_Bit_Pos(13,21)) # False
print(differ_At_One_Bit_Pos(13,22)) # False
print(differ_At_One_Bit_Pos(13,23)) # False
print(differ_At_One_Bit_Pos(13,24)) # False
print(differ_At_One_Bit_Pos(13,25)) # False
print(differ_At_One_Bit_Pos(13,26)) # False
print(differ_At_One_Bit_Pos(13,27)) # False
print(differ_At_One_Bit_Pos(13,28)) # False
print(differ_At_One_Bit_Pos(13,29)) # False
print(differ_At_One_Bit_Pos(13,30)) # False
print(differ_At_One_Bit_Pos(13,31)) # False
print(differ_At_One_Bit_Pos(13,32)) # False
print(differ_At_One_Bit_Pos(13,33)) # False
print(differ_At_One_Bit_Pos(13,34)) # False
print(differ_At_One_Bit_Pos(13,35)) # False
print(differ_At_One_Bit_Pos(13,36)) # False
print(differ_At_One_Bit_Pos(13,37)) # False
print(differ_At_One_Bit_Pos(13,38)) # False
print(differ_At_One_Bit_Pos(13,39)) # False
print(differ_At_One_Bit_Pos(13,40)) # False
print(differ_At_One_Bit_Pos(13,41)) # False
print(differ_At_One_Bit_Pos(13,42)) # False
print(differ_At_One_Bit_Pos(13,43)) # False
print(differ_At_One_Bit_Pos(13,44)) # False
print(differ_At_