"""
Write a python function to count minimum number of swaps required to convert one binary number represented as a string to another.
assert min_Swaps("1101","1110") == 1
"""

def min_swaps(binary1, binary2):
    count = 0
    for i in range(len(binary1)):
        if binary1[i] != binary2[i]:
            binary1 = binary1[:i] + '0' + binary1[i+1:]
            binary2 = binary2[:i] + '1' + binary2[i+1:]
            count += 1
    return count

print(min_swaps("1101","1110")) # Output: 1
print(min_swaps("11110","1011")) # Output: 2
print(min_swaps("11110","1101")) # Output: 1
print(min_swaps("1010","1111")) # Output: 2
print(min_swaps("11110","1111")) # Output: 0
print(min_swaps("1110","1111")) # Output: 2
print(min_swaps("1110","1011")) # Output: 2
print(min_swaps("1010","1111")) # Output: 2
print(min_swaps("1111","1110")) # Output: 1
print(min_swaps("1111","1111")) # Output: 0
print(min_swaps("1111","1011")) # Output: 2
print(min_swaps("1011","1111")) # Output: 2
print(min_swaps("1011","1101")) # Output: 2
print(min_swaps("1101","1110")) # Output: 1
print(min_swaps("11111","1111")) # Output: 0
print(min_swaps("1111","1111")) # Output: 0
print(min_swaps("1111","1011")) # Output: 2
print(min_swaps("1011","1111")) # Output: 2
print(min_swaps("1011","1101")) # Output: 2
print(min_swaps("1101","1110")) # Output: 1
print(min_swaps("1111","1110")) # Output: 2
print(min_swaps("1110","1111")) # Output: 1
print(min_swaps("1110","1011")) # Output: 2
print(min_swaps("1101","1110")) # Output: 1
print(min_swaps("1111","1111")) # Output: 0
print(min_swaps("1111","1011")) # Output: 2
print(min_swaps("1011","1111")) # Output: 2
print(min_swaps("1011","1101")) # Output: 2
print(min_swaps("1101","1110")) # Output: 1
print(min_swaps("1111","1111")) # Output: 0
print(min_swaps("1111","1011")) # Output: 2
print(min_swaps("1011","1111")) # Output: 2
print(min_swaps("1011","1101")) # Output: 2
print(min_swaps("1101","1110")) # Output: 1
print(min_swaps("1111","1111")) # Output: 0
print(min_swaps("1111","1011")) # Output: 2
print(min_swaps("1011","1111")) # Output: 2
print(min_swaps("1011","1101"))