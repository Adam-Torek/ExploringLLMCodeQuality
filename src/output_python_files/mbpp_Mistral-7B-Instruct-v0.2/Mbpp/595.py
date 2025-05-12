"""
Write a python function to count minimum number of swaps required to convert one binary number represented as a string to another.
assert min_Swaps("1101","1110") == 1
"""
def min_Swaps(num1,num2):
    count = 0
    xor = int(num1,2)^int(num2,2)
    i = 0
    while xor:
        if num1[i] != num2[i]:
            count += 1
            num1 = swap(num1,i)
            num2 = swap(num2,i)
            xor = int(num1,2)^int(num2,2)
        i += 1
    return count

def swap(num,index):
    num_list = list(num)
    num_list[index] = str(int(num_list[index])^1)
    return ''.join(num_list)

assert min_Swaps("1101","1110") == 1
assert min_Swaps("101011","111100") == 3
assert min_Swaps("11111111","00000000") == 11
assert min_Swaps("101011","011101") == 3
assert min_Swaps("11111111","11110000") == 1
assert min_Swaps("11111111","00000000") == 11
assert min_Swaps("11111111","10101010") == 10
assert min_Swaps("11111111","11111101") == 1
assert min_Swaps("11111111","11111110") == 1
assert min_Swaps("11111111","11111111") == 0
assert min_Swaps("11111111","11111111") == 0
assert min_Swaps("11111111","11111111") == 0
assert min_Swaps("11111111","11111111") == 0
assert min_Swaps("11111111","11111111") == 0
assert min_Swaps("11111111","11111111") == 0
assert min_Swaps("11111111","11111111") == 0
assert min_Swaps("11111111","11111111") == 0
assert min_Swaps("11111111","11111111") == 0
assert min_Swaps("11111111","11111111") == 0
assert min_Swaps("11111111","11111111") == 0
assert min_Swaps("11111111","11111111") == 0
assert min_Swaps("11111111","11111111") == 0
assert min_Swaps("11111111","11111111") == 0
assert min_Swaps("11111111","11111111") == 0
assert min_Swaps("11111111","11111111") == 0
assert min_Swaps("11111111","11111111") == 0
assert min_Swaps("11111111","11111111") == 0
assert min_Swaps("11111111","11111111") == 0
assert min_Swaps("11