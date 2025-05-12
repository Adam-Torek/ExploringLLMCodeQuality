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
assert min_Swaps("101010","011101") == 3
assert min_Swaps("111111","000000") == 11
assert min_Swaps("101010101010101010101010","0111011101110111011101110") == 20
assert min_Swaps("11111111111111111111111111111111","00000000000000000000000000000000") == 32
assert min_Swaps("11111111111111111111111111111111","00011110011100010110011001110110") == 15
assert min_Swaps("11111111111111111111111111111111","11110000000011111111000000001111") == 3
assert min_Swaps("11111111111111111111111111111111","11111111111111111111111111111101") == 1
assert min_Swaps("11111111111111111111111111111111","11111111111111111111111111111011") == 1
assert min_Swaps("11111111111111111111111111111111","11111111111111111111111111110111") == 1
assert min_Swaps("11111111111111111111111111111111","11111111111111111111111111101111") == 1
assert min_Swaps("11111111111111111111111111111111","11111111111111111111111111011111") == 1
assert min_Swaps("11111111111111111111111111111111","111111111111111111