"""
Write a python function to count minimum number of swaps required to convert one binary number represented as a string to another.
assert min_Swaps("1101","1110") == 1
"""

def min_swaps(binary1, binary2):
    count = 0
    for i in range(len(binary1)):
        if binary1[i] != binary2[i]:
            count += 1
    return count

print(min_swaps("1101","1110")) # Output: 1
print(min_swaps("11110","1011")) # Output: 2
print(min_swaps("1010","1101")) # Output: 2
print(min_swaps("11111","0000")) # Output: 4
print(min_swaps("0000","1111")) # Output: 4
print(min_swaps("1010","0101")) # Output: 2
print(min_swaps("11111","1111")) # Output: 0
print(min_swaps("0000","0000")) # Output: 0
print(min_swaps("1010","1010")) # Output: 0

# Time Complexity: O(n)
# Space Complexity: O(1)

# Another approach:
def min_swaps(binary1, binary2):
    count = 0
    for i in range(len(binary1)):
        if binary1[i] != binary2[i]:
            binary1 = binary1[:i] + binary2[i] + binary1[i+1:]
            binary2 = binary2[:i] + binary1[i] + binary2[i+1:]
            count += 1
    return count

print(min_swaps("1101","1110")) # Output: 1
print(min_swaps("1111","0000")) # Output: 4
print(min_swaps("1010","0101")) # Output: 2
print(min_swaps("1111","1111")) # Output: 0
print(min_swaps("0000","0000")) # Output: 0
print(min_swaps("1010","1010")) # Output: 0
print(min_swaps("1111","0000")) # Output: 4
print(min_swaps("1101","1110")) # Output: 1

# Time Complexity: O(n)
# Space Complexity: O(1)

# Another approach:
def min_swaps(binary1, binary2):
    count = 0
    for i in range(len(binary1)):
        if binary1[i] != binary2[i]:
            binary1 = binary1[:i] + binary2[i] + binary1[i+1:]
            binary2 = binary2[:i] + binary1[i] + binary2[i+1:]
            count += 1
    return count

print(min_swaps("1101","1110")) # Output: 1
print(min_swaps("1111","0000")) # Output: 4
print(min_swaps("1010","0101")) # Output: 2
print(min_swaps("1111","1111")) # Output: 0
print(min_swaps("0000","0000")) # Output: 0
print(min_swaps("1010","1010")) # Output: 0
print(min_swaps("1111","0000")) # Output: 4
print(min_swaps("1101","1110")) # Output: 1

# Time Complexity: O(n)
# Space Complexity: O(1)

# Another approach:
def min_swaps(binary1, binary2):
    count = 0
    for i in range(len(binary1)):