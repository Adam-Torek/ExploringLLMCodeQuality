"""
Write a python function to check whether the two numbers differ at one bit position only or not.
assert differ_At_One_Bit_Pos(13,9) == True
"""

def differ_At_One_Bit_Pos(num1, num2):
    bin_num1 = bin(num1)[2:]
    bin_num2 = bin(num2)[2:]
    count = 0
    for i in range(len(bin_num1)):
        if bin_num1[i] != bin_num2[i]:
            count += 1
        if count > 1:
            return False
    return True if count == 1 else False

print(differ_At_One_Bit_Pos(13,9)) # True
print(differ_At_One_Bit_Pos(15,17)) # False
print(differ_At_One_Bit_Pos(10,11)) # True
print(differ_At_One_Bit_Pos(10,12)) # False
print(differ_At_One_Bit_Pos(10,13)) # True
print(differ_At_One_Bit_Pos(10,14)) # False
print(differ_At_One_Bit_Pos(10,15)) # False
print(differ_At_One_Bit_Pos(10,16)) # False
print(differ_At_One_Bit_Pos(10,17)) # False
print(differ_At_One_Bit_Pos(10,18)) # False
print(differ_At_One_Bit_Pos(10,19)) # False
print(differ_At_One_Bit_Pos(10,20)) # False
print(differ_At_One_Bit_Pos(10,21)) # False
print(differ_At_One_Bit_Pos(10,22)) # False
print(differ_At_One_Bit_Pos(10,23)) # False
print(differ_At_One_Bit_Pos(10,24)) # False
print(differ_At_One_Bit_Pos(10,25)) # False
print(differ_At_One_Bit_Pos(10,26)) # False
print(differ_At_One_Bit_Pos(10,27)) # False
print(differ_At_One_Bit_Pos(10,28)) # False
print(differ_At_One_Bit_Pos(10,29)) # False
print(differ_At_One_Bit_Pos(10,30)) # False
print(differ_At_One_Bit_Pos(10,31)) # False
print(differ_At_One_Bit_Pos(10,32)) # False
print(differ_At_One_Bit_Pos(10,33)) # False
print(differ_At_One_Bit_Pos(10,34)) # False
print(differ_At_One_Bit_Pos(10,35)) # False
print(differ_At_One_Bit_Pos(10,36)) # False
print(differ_At_One_Bit_Pos(10,37)) # False
print(differ_At_One_Bit_Pos(10,38)) # False
print(differ_At_One_Bit_Pos(10,39)) # False
print(differ_At_One_Bit_Pos(10,40)) # False
print(differ_At_One_Bit_Pos(10,41)) # False
print(differ_At_One_Bit_Pos(10,42)) # False
print(differ_At_One_Bit_Pos(10,43)) # False
print(differ_At_One_Bit_Pos(10,44)) # False
print(differ_At_One_Bit_Pos(10,45)) # False
print(differ_At_